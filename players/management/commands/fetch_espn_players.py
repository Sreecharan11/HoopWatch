import requests
from django.core.management.base import BaseCommand
from players.models import Player
from games.models import Team

class Command(BaseCommand):
    help = 'Fetch NBA players from ESPN API for all teams'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching NBA players from ESPN API...')
        
        # First, get all teams
        teams = Team.objects.all()
        
        if not teams.exists():
            self.stdout.write(self.style.ERROR(
                'No teams found in database. Please run "python manage.py fetch_espn_teams" first.'
            ))
            return
        
        players_created = 0
        players_updated = 0
        
        # Fetch roster for each team
        for team in teams:
            self.stdout.write(f'\nFetching roster for {team.full_name}...')
            
            # ESPN API endpoint for team roster
            url = f'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{team.api_id}/roster'
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                
                # Get athletes from roster
                athletes = data.get('athletes', [])
                
                for athlete_data in athletes:
                    try:
                        # Check if this is the right structure
                        if 'athlete' in athlete_data:
                            athlete = athlete_data.get('athlete', {})
                        else:
                            athlete = athlete_data
                        
                        # Extract player data
                        player_id = athlete.get('id')
                        
                        # Skip if no player ID
                        if not player_id:
                            self.stdout.write(self.style.WARNING(f'  Skipping player with no ID'))
                            continue
                        
                        first_name = athlete.get('firstName', '')
                        last_name = athlete.get('lastName', '')
                        
                        # Skip if no name
                        if not first_name and not last_name:
                            self.stdout.write(self.style.WARNING(f'  Skipping player {player_id} with no name'))
                            continue
                        
                        # Get position
                        position_data = athlete.get('position', {})
                        position = position_data.get('abbreviation', '') if position_data else ''
                        
                        # Get jersey number
                        jersey = athlete.get('jersey', '')
                        
                        # Get height (comes as string like "6' 8\"")
                        height = athlete.get('displayHeight', '')
                        
                        # Get weight (comes as integer)
                        weight = athlete.get('weight', '')
                        if weight:
                            weight = str(weight)
                        
                        # Get college
                        college = ''
                        experience = athlete.get('experience', {})
                        if experience:
                            college = experience.get('displayValue', '')
                        
                        # Get birthplace (for country)
                        country = 'USA'  # Default
                        birthplace = athlete.get('birthPlace', {})
                        if birthplace:
                            country = birthplace.get('country', 'USA')
                        
                        # Create or update player
                        player, created = Player.objects.update_or_create(
                            api_id=player_id,
                            defaults={
                                'first_name': first_name,
                                'last_name': last_name,
                                'position': position,
                                'height': height,
                                'weight_pounds': weight,
                                'jersey_number': jersey,
                                'college': college,
                                'country': country,
                                'team': team,
                            }
                        )
                        
                        if created:
                            players_created += 1
                            self.stdout.write(f'  Created: {first_name} {last_name} ({position})')
                        else:
                            players_updated += 1
                            self.stdout.write(f'  Updated: {first_name} {last_name} ({position})')
                    
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'  Error processing player: {str(e)}'))
                        continue
                
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f'  Error fetching roster: {str(e)}'))
                continue
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  Unexpected error: {str(e)}'))
                continue
        
        self.stdout.write(self.style.SUCCESS(
            f'\nCompleted! Created {players_created} players, Updated {players_updated} players'
        ))

