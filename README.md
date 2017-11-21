
# hackeybot

**Requirements:**
  Python 3.6.1

**How to run:**  
    1. Clone or download this repository on a folder  
    2. Access the folder from the terminal and run "pip install -r requirements.txt" (this will install mlbgame api, praw(reddit api), tweepy(twitter api) and others)  
    3. After the install is complete create a file in the main folder called 'reddit.auth.py'
    4. Register an app on reddit/prefs/apps and add the following code to it:

    import praw

    reddit = praw.Reddit(client_id='your-client-id',
                         client_secret='your-client-secret',
                         password='your-password',
                         user_agent='<macOS>:<1>:<0> (by /u/<username>)',
                         username='your-username')


    5. run python bot.py  


**MLB Commands List:**

    !score team_name - posts the score for the team name in the argument  
    !pitching team_name - posts the current pitcher for the current game of the team in argument  
    !batting team_name - posts the current pitcher for the current game of the team in argument  
    !line team_name -  posts the pitching line for the starting pitcher of the game from the team in argument  
    !record team_name posts the current W/L record for the team in arguments  
    !time team_name - posts the start time of today’s game of the team in arguments  
    !last_ab team_name - posts the description for the last at bat occurred in current inning of teams game in argument  
    !ondeck team_name - posts the current player on deck on team_name game  
    !inhole team_name - posts the current player in the hole on team_name game  
    !dueup team_name - posts the due up batters oon team_name game  
    !starting team_name - posts the starting pitcher for the team_name game  
    !stats team_name player_name - posts the game stats for the player_name in the arguments  
    !seasonstats team_name player_name - posts the season stats for player_name in the arguments  
    !mugshot team_name player_name - posts the mugshot for given player

**use without team_name parameter to get command for favorite_team**  

**NHL Commands**  

    $show player_last_name - shows player picture
    $score team_name - shows score of current game for given team
    $record team_name - shows team record for given team
    $sog team_name - shows shots on goal for current game of given team
    $stats player_last_name - show games played, goals, assists for given player
    $pp team_name - shows powerplay percentage and league rank for given team
    $pk team_name - shows penalty kill percentage and league rank for given team


**Hackey commands:**  

    !username - posts a random message for username in parameter (If you're not there feel free to create a pull request and add yourself or ask me and i'll do it)  
    !gif - posts a random gif blue jays related  
    !faggot - posts pic of pillar screaming the word "faggot"  
    !biglenny - posts big lenny  
    !13reasons - posts Ross 13 reasons to kill himself  
    !venn - posts hackey chat venn diagram  
    !consent - posts age of consent in canada  
    !gibby - posts a random gibby image  
    !shapoo - screams SHAPOOOO  
    !penny - posts a random Penny Oleksiak picture  
    !pennyage - posts penny's age on the current day (buggy)  
    !pennydance - posts epic penny's dance gif  
    !doggo - posts a random doggo from the dog.ceo api  
    !doggo breed - posts a random doggo by breed from the dog.ceo api  
    !fap - posts a random pic from the /r/gentlemanboners subreddit  
    !brazzers - posts a random pic from the /r/brazilianbabes subreddit (NSFW)  
    !dome - posts if the dome is open or not in the blue jays game  
    !tip - posts a random tip from /r/ShittyLifeProTips  
    !thought - posts a random thought from /r/Showerthoughts  
    !joke - posts a random joke from /r/Jokes  
    !motivation - posts a motivation image from /r/GetMotivated  
    !quote - posts a random quote from /r/quotes  
    !countdown - posts the countdown for leafs 2017 preseason  
    !brad - brad meme
    !dasit - dasit mane meme (thx natty)
    !cock - babcock memes
    !no - no meme


**memegen:**   

        !go2bed chatango_username or team_name player_name   
        !hang chatango_username or team_name player_name   
        !kill chatango_username or team_name player_name  
        !golf chatango_username or team_name player_name   
        !poop chatango_username or team_name player_name   
        !trash chatango_username or team_name player_name   
        !baby chatango_username or team_name player_name   
        !penbox chatango_username or team_name player_name   

        - Creates the desired meme from 46.228.199.201/mdoublee/memegen2/ Credits to mdoublee

**Whats to come:**

    NHL module (dank leafs memes and live game stats commands) (I'll try to make it work for other teams too)  
    suggestions/bug reporting page  
