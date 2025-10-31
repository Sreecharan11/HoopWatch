import requests
import time
import os
from django.core.management.base import BaseCommand
from games.models import Team
from players.models import Player


class Command(BaseCommand):
    help = 'Fetches NBA teams and players from BallDontLie API'

    def handle(self, *args, **kwargs):
        # Get API key from environment variable or prompt
        api_key = os.environ.get('BALLDONTLIE_API_KEY')
        if not api_key:
            api_key = input("Enter your BallDontLie API key: ")
        
        headers = {
            'Authorization': api_key
        }
        
        self.stdout.write(self.style.SUCCESS('Starting to fetch NBA data...'))
        
        # Fetch Teams
        self.stdout.write('Fetching teams...')
        try:
            response = requests.get(
                'https://api.balldontlie.io/v1/teams',
                headers=headers
            )
            response.raise_for_status()
            teams_data = response.json()
            
            teams_created = 0
            for team_data in teams_data.get('data', []):
                Team.objects.update_or_create(
                    api_id=team_data['id'],
                    defaults={
                        'abbreviation': team_data.get('abbreviation', ''),
                        'city': team_data.get('city', ''),
                        'conference': team_data.get('conference', ''),
                        'division': team_data.get('division', ''),
                        'full_name': team_data.get('full_name', ''),
                        'name': team_data.get('name', ''),
                    }
                )
                teams_created += 1
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created/Updated {teams_created} teams'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching teams: {str(e)}'))
            return
        
        # Fetch Players (paginated)
        self.stdout.write('Fetching players...')
        try:
            page = 1
            players_created = 0
            
            while page <= 3:  # Fetch first 3 pages (300 players) to avoid rate limit
                self.stdout.write(f'  Fetching page {page}...')
                response = requests.get(
                    f'https://api.balldontlie.io/v1/players?per_page=100&page={page}',
                    headers=headers
                )
                response.raise_for_status()
                players_data = response.json()
                
                # Sleep for 12 seconds to respect rate limit (5 requests/minute)
                if page < 3:
                    self.stdout.write('  Waiting 12 seconds (rate limit)...')
                    time.sleep(12)
                
                data = players_data.get('data', [])
                if not data:
                    break
                
                for player_data in data:
                    # Get team if exists
                    team = None
                    if player_data.get('team'):
                        team_id = player_data['team'].get('id')
                        if team_id:
                            try:
                                team = Team.objects.get(api_id=team_id)
                            except Team.DoesNotExist:
                                pass
                    
                    Player.objects.update_or_create(
                        api_id=player_data['id'],
                        defaults={
                            'first_name': player_data.get('first_name', ''),
                            'last_name': player_data.get('last_name', ''),
                            'position': player_data.get('position', ''),
                            'height': player_data.get('height', ''),
                            'weight_pounds': player_data.get('weight', ''),
                            'jersey_number': player_data.get('jersey_number', ''),
                            'college': player_data.get('college', ''),
                            'country': player_data.get('country', 'USA'),
                            'draft_year': player_data.get('draft_year'),
                            'draft_round': player_data.get('draft_round'),
                            'draft_number': player_data.get('draft_number'),
                            'team': team,
                        }
                    )
                    players_created += 1
                
                page += 1
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created/Updated {players_created} players'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching players: {str(e)}'))
            return
        
        self.stdout.write(self.style.SUCCESS('\n🎉 Done! Check Django admin to see your data!'))
        self.stdout.write(self.style.SUCCESS('Visit: http://localhost:8000/admin'))

