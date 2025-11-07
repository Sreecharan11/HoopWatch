import requests
from django.core.management.base import BaseCommand
from games.models import Team, Game
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch NBA games from ESPN API'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching NBA games from ESPN API...')
        
        # ESPN API endpoint for NBA schedule
        # This gets the current season's schedule
        url = 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            games_created = 0
            games_updated = 0
            
            # Process each game
            for event in data.get('events', []):
                try:
                    # Extract game data
                    game_id = event.get('id')
                    game_date = event.get('date')
                    status = event['status']['type']['name']
                    
                    # Map ESPN status to our status
                    if status in ['STATUS_SCHEDULED', 'STATUS_POSTPONED']:
                        game_status = 'upcoming'
                    elif status in ['STATUS_IN_PROGRESS', 'STATUS_HALFTIME']:
                        game_status = 'in_progress'
                    elif status in ['STATUS_FINAL', 'STATUS_FINAL_OVERTIME']:
                        game_status = 'finished'
                    else:
                        game_status = 'upcoming'
                    
                    # Get teams
                    competitions = event.get('competitions', [])
                    if not competitions:
                        continue
                    
                    competition = competitions[0]
                    competitors = competition.get('competitors', [])
                    
                    if len(competitors) != 2:
                        continue
                    
                    # ESPN has home team first, away team second
                    home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), None)
                    away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), None)
                    
                    if not home_competitor or not away_competitor:
                        continue
                    
                    # Get team abbreviations
                    home_abbr = home_competitor['team']['abbreviation']
                    away_abbr = away_competitor['team']['abbreviation']
                    
                    # Find teams in our database
                    try:
                        home_team = Team.objects.get(abbreviation=home_abbr)
                    except Team.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Home team not found: {home_abbr}'))
                        continue
                    
                    try:
                        visitor_team = Team.objects.get(abbreviation=away_abbr)
                    except Team.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Visitor team not found: {away_abbr}'))
                        continue
                    
                    # Get scores (if game is finished or in progress)
                    home_score = None
                    visitor_score = None
                    
                    if game_status in ['finished', 'in_progress']:
                        home_score = int(home_competitor.get('score', 0))
                        visitor_score = int(away_competitor.get('score', 0))
                    
                    # Parse date
                    game_datetime = datetime.fromisoformat(game_date.replace('Z', '+00:00'))
                    
                    # Create or update game
                    game, created = Game.objects.update_or_create(
                        api_id=game_id,
                        defaults={
                            'date': game_datetime,
                            'home_team': home_team,
                            'visitor_team': visitor_team,
                            'home_team_score': home_score,
                            'visitor_team_score': visitor_score,
                            'status': game_status,
                            'season': 2024,  # Current season
                        }
                    )
                    
                    if created:
                        games_created += 1
                        self.stdout.write(f'Created: {visitor_team.abbreviation} @ {home_team.abbreviation}')
                    else:
                        games_updated += 1
                        self.stdout.write(f'Updated: {visitor_team.abbreviation} @ {home_team.abbreviation}')
                
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error processing game: {str(e)}'))
                    continue
            
            self.stdout.write(self.style.SUCCESS(
                f'\nCompleted! Created {games_created} games, Updated {games_updated} games'
            ))
            
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data from ESPN: {str(e)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))

