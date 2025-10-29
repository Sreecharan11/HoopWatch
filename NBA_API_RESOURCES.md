# 🏀 NBA API Resources

## Free NBA APIs for Integration

### 1. BallDontLie API (Recommended)
- **URL:** https://www.balldontlie.io/
- **Documentation:** https://docs.balldontlie.io/
- **Features:**
  - Player stats
  - Team information
  - Game data
  - Season stats
- **Rate Limit:** 60 requests/minute (free tier)
- **Authentication:** No API key required

**Example Endpoints:**
```
GET https://www.balldontlie.io/api/v1/players
GET https://www.balldontlie.io/api/v1/teams
GET https://www.balldontlie.io/api/v1/games
GET https://www.balldontlie.io/api/v1/stats
```

### 2. NBA API (Unofficial)
- **GitHub:** https://github.com/swar/nba_api
- **Type:** Python library
- **Features:**
  - Live game data
  - Player stats
  - Team stats
  - Historical data
- **Installation:** `pip install nba_api`

**Example Usage:**
```python
from nba_api.stats.endpoints import playercareerstats

# Get player career stats
career = playercareerstats.PlayerCareerStats(player_id='203999')
print(career.get_data_frames()[0])
```

### 3. The Sports DB
- **URL:** https://www.thesportsdb.com/
- **Documentation:** https://www.thesportsdb.com/api.php
- **Features:**
  - Team information
  - Player details
  - Event schedules
  - League information
- **Free Tier:** Limited endpoints
- **Paid Tier:** $3/month for full access

### 4. ESPN API (Unofficial)
- **Base URL:** http://site.api.espn.com/apis/site/v2/sports/basketball/nba/
- **Features:**
  - Scores
  - Teams
  - News
  - Schedules
- **Note:** Unofficial, no documentation, may change

**Example Endpoints:**
```
GET http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard
GET http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams
```

## Integration Strategy

### Phase 1: Basic Setup
1. Start with BallDontLie API (easiest, no auth)
2. Create Django management commands to fetch and cache data
3. Store frequently accessed data in your SQLite database

### Phase 2: Data Management
```python
# Example Django management command
# backend/players/management/commands/fetch_players.py

from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Fetch NBA players from API'

    def handle(self, *args, **kwargs):
        response = requests.get('https://www.balldontlie.io/api/v1/players')
        players = response.json()['data']
        
        for player_data in players:
            Player.objects.update_or_create(
                api_id=player_data['id'],
                defaults={
                    'first_name': player_data['first_name'],
                    'last_name': player_data['last_name'],
                    'team': player_data['team']['full_name'],
                    # ... more fields
                }
            )
```

### Phase 3: Caching Strategy
- Cache API responses in Django cache or database
- Refresh data periodically (daily for player info, hourly for games)
- Use Django Celery for scheduled tasks (optional)

## Example API Calls

### Fetch Players
```javascript
// Frontend
import axios from 'axios';

const fetchPlayers = async () => {
  try {
    const response = await axios.get('https://www.balldontlie.io/api/v1/players');
    return response.data.data;
  } catch (error) {
    console.error('Error fetching players:', error);
  }
};
```

### Fetch Games
```javascript
const fetchTodayGames = async () => {
  const today = new Date().toISOString().split('T')[0];
  const response = await axios.get(
    `https://www.balldontlie.io/api/v1/games?dates[]=${today}`
  );
  return response.data.data;
};
```

## Best Practices

1. **Rate Limiting:**
   - Implement rate limiting on your backend
   - Cache responses to minimize API calls
   - Use Django's cache framework

2. **Error Handling:**
   - Handle API downtime gracefully
   - Implement retry logic
   - Show user-friendly error messages

3. **Data Freshness:**
   - Player data: Update daily
   - Game schedules: Update twice daily
   - Live scores: Update every 30 seconds (during games)

4. **Performance:**
   - Store frequently accessed data in your database
   - Use pagination for large datasets
   - Implement lazy loading in frontend

## Sample Django Model

```python
# backend/players/models.py

from django.db import models

class Player(models.Model):
    api_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    team = models.CharField(max_length=100)
    height_feet = models.IntegerField(null=True)
    height_inches = models.IntegerField(null=True)
    weight_pounds = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Game(models.Model):
    api_id = models.IntegerField(unique=True)
    date = models.DateTimeField()
    home_team = models.CharField(max_length=100)
    visitor_team = models.CharField(max_length=100)
    home_team_score = models.IntegerField(null=True)
    visitor_team_score = models.IntegerField(null=True)
    status = models.CharField(max_length=20)  # upcoming, live, final
    season = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor_team} @ {self.home_team} - {self.date}"
```

## Testing APIs

Use these tools to test APIs before integration:
- **Postman:** https://www.postman.com/
- **Insomnia:** https://insomnia.rest/
- **curl:** Command line tool

Example curl command:
```bash
curl "https://www.balldontlie.io/api/v1/players?search=lebron"
```

---

**Note:** Always check the API's terms of service and rate limits before integration. For production apps, consider upgrading to paid tiers for better reliability and higher rate limits.

