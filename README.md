# Euro 2020

## Data cleaning

### Teams dataset
  - Stage: First stage matches grouped on the same category.
  - Dates: Changed format to [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601).
  - Possession and won duels: Setted percentage string to a value between 0 and 1.
  - Pens_score: Setted to NULL false string when match is not solved by pens.
  - Spaces on strings: Start and end spaces removes from every categorical column.
  
### Generated dataset with events

  - We notice that there are data on event_result and event_player on PK events.
  - On type column, we set value to PK-Goal and PK-Missed in this cases
  - In this cases, event_player info will be setted on action_player_1
  - Dropped event_result, event_player columns
  - Event_time on type=PK setted to 120 (end time of extra time)
  - Event_team will store team_id instead home/away. This vale comes from the table created on 01_matches.ipynb
  - We notice incoherent data on action_player_2 (Own goal, Penalty) the same than in action_player_1

<hr>

## Tables Generation


![Tables](./readme-docs/tables.jpg)
## API endpoints

### /
  - Just to check connection.

### /events?type=aaa
  - Match events grouped by team from matches.
  - Returns type events summatory.

### /events-player?type=aaa&player=2
  - Match events grouped by player from matches.
  - Returns type events summatory. Query param player 2 defines assistant on a goal or outcome player in a substitution.
  
### /events-team/team?type=aaa&player=2
  - Match events grouped by players from a team.
  - Returns type events summatory. Query param player 2 defines assistant on a goal or outcome player in a substitution.

### /masters/<table>/<column>
  - Returns unique values form a column in a tabel

### /matches/<team>?team=aaa
  - Returns team events from a match.
  - If team=all return all events

### /penalty?type=[all, winner, looser]
  - If type=all returns all matches solved by pens.
  - Otherwise return teams winners/loosers by pens.

### /players-location
  - Returns players born city longitude and latitude.

### /players-location/<country>
  - Returns players born city longitude and latitude from a team.

### /players-club
  - Returns players summatory grouped by club.
### /players-club/<club>
  - Returns players from the same club.

## API structure

    |
    |__ \
        |----server.py         -> Entry point
        |----app.py            -> App instance creation
        |----config.py         -> App config file
        |----Dockerfile
        |----requeriments.txt  -> App dependencies
        |
        |____\controllers
        |     |----events-controller     -> events-endpoint
        |     |----masters-controller    -> masters-endpoint
        |     |----matches-controller    -> matches-endpoint
        |     |----penalty-controller    -> penalty-endpoint
        |     |----players-controller    -> players-endpoint
        |     |____root-controller       -> root-endpoint
        |
        |____\utils
              |----db-connetion     -> execute query function
              |----handle-error    -> error handler decorator
              |----json-response    -> return json from query function
              |----sql-queries    -> sql queries
              |____sql-utils       -> functions to configure queries