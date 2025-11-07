import requests
from django.core.management.base import BaseCommand
from games.models import Team

class Command(BaseCommand):
    help = 'Fetch all NBA teams from ESPN API'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching NBA teams from ESPN API...')
        
        # ESPN API endpoint for NBA teams
        url = 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams?limit=100'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            teams_created = 0
            teams_updated = 0
            
            # Process each team
            for team_data in data.get('sports', [{}])[0].get('leagues', [{}])[0].get('teams', []):
                try:
                    team_info = team_data.get('team', {})
                    
                    # Extract team data
                    team_id = team_info.get('id')
                    full_name = team_info.get('displayName', '')
                    abbreviation = team_info.get('abbreviation', '')
                    city = team_info.get('location', '')
                    name = team_info.get('name', '')
                    
                    # Get conference and division from groups
                    conference = ''
                    division = ''
                    
                    groups = team_info.get('groups', {})
                    if groups:
                        # Conference is usually id 7 (Eastern) or 8 (Western)
                        conference_id = groups.get('id', '')
                        if 'eastern' in groups.get('name', '').lower():
                            conference = 'East'
                        elif 'western' in groups.get('name', '').lower():
                            conference = 'West'
                        
                        # Division
                        division_name = groups.get('name', '')
                        if 'atlantic' in division_name.lower():
                            division = 'Atlantic'
                        elif 'central' in division_name.lower():
                            division = 'Central'
                        elif 'southeast' in division_name.lower():
                            division = 'Southeast'
                        elif 'northwest' in division_name.lower():
                            division = 'Northwest'
                        elif 'pacific' in division_name.lower():
                            division = 'Pacific'
                        elif 'southwest' in division_name.lower():
                            division = 'Southwest'
                    
                    # If we couldn't get conference/division from groups, use hardcoded mapping
                    if not conference or not division:
                        conference, division = self.get_conference_division(abbreviation)
                    
                    # Create or update team
                    team, created = Team.objects.update_or_create(
                        api_id=team_id,
                        defaults={
                            'full_name': full_name,
                            'abbreviation': abbreviation,
                            'city': city,
                            'name': name,
                            'conference': conference,
                            'division': division,
                        }
                    )
                    
                    if created:
                        teams_created += 1
                        self.stdout.write(f'Created: {full_name} ({abbreviation})')
                    else:
                        teams_updated += 1
                        self.stdout.write(f'Updated: {full_name} ({abbreviation})')
                
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error processing team: {str(e)}'))
                    continue
            
            self.stdout.write(self.style.SUCCESS(
                f'\nCompleted! Created {teams_created} teams, Updated {teams_updated} teams'
            ))
            
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data from ESPN: {str(e)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
    
    def get_conference_division(self, abbr):
        """Hardcoded mapping of team abbreviations to conference and division"""
        mapping = {
            # Eastern Conference - Atlantic
            'BOS': ('East', 'Atlantic'),
            'BKN': ('East', 'Atlantic'),
            'NY': ('East', 'Atlantic'),
            'NYK': ('East', 'Atlantic'),
            'PHI': ('East', 'Atlantic'),
            'TOR': ('East', 'Atlantic'),
            
            # Eastern Conference - Central
            'CHI': ('East', 'Central'),
            'CLE': ('East', 'Central'),
            'DET': ('East', 'Central'),
            'IND': ('East', 'Central'),
            'MIL': ('East', 'Central'),
            
            # Eastern Conference - Southeast
            'ATL': ('East', 'Southeast'),
            'CHA': ('East', 'Southeast'),
            'MIA': ('East', 'Southeast'),
            'ORL': ('East', 'Southeast'),
            'WSH': ('East', 'Southeast'),
            'WAS': ('East', 'Southeast'),
            
            # Western Conference - Northwest
            'DEN': ('West', 'Northwest'),
            'MIN': ('West', 'Northwest'),
            'OKC': ('West', 'Northwest'),
            'POR': ('West', 'Northwest'),
            'UTA': ('West', 'Northwest'),
            
            # Western Conference - Pacific
            'GS': ('West', 'Pacific'),
            'GSW': ('West', 'Pacific'),
            'LAC': ('West', 'Pacific'),
            'LAL': ('West', 'Pacific'),
            'PHX': ('West', 'Pacific'),
            'SAC': ('West', 'Pacific'),
            
            # Western Conference - Southwest
            'DAL': ('West', 'Southwest'),
            'HOU': ('West', 'Southwest'),
            'MEM': ('West', 'Southwest'),
            'NO': ('West', 'Southwest'),
            'NOP': ('West', 'Southwest'),
            'SA': ('West', 'Southwest'),
            'SAS': ('West', 'Southwest'),
        }
        
        return mapping.get(abbr, ('', ''))

