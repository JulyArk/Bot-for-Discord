# Discord   
This is a simple implementation of a discord bot using the discord.py rewrite library.      
In order to run the bot you will need to generate a discord bot token as well as a reddit API app. They're free and easy to generate.            
Discord bot token: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord       
Reddit API info: https://stackoverflow.com/a/42304034         
# Commands:   
CopyPasta = Bot responds to keywords by posting a message    
    -addpasta:  Add response to keyword    
    -eatpasta:  Removes one of the copypastas   
    -pastabits: Changes if the trigger messages gets deleted     
              
Dictionary = Parsing trough urban dictionary   
    -define:    UrbanDict definiton of a certain word   
    -wotd:      Word of the day on UrbanDictionary  
          
DiscordBotVoice = Supposed to play music but it'll be added later   
    -join:      Bot joins the voice channel the user is in   
    -leave:     Bot leaves voice   
         
DiscordRateGirl (BETA) = Generates 2 PRNG values that stay consistent depending on day   
    -rategirl:  Rates @User by 2 values, Hot and Crazy    
         
Miscellaneous = For filler commands that don't deserve their own class   
    -avm:       Print avatar of pinged User   
    -badbot:    Same as goodbot   
    -changelog:    
    -cm:        Turns cm (height) to ft + inch (metric to imperial) by approximation   
    -dice:      Rolls 2 dice ( returns 2 values between 1-6)   
    -erase:     Erase N messages (admin only)   
    -ft:        Turns height ft.inch (Eg: 5.11) to cm (imperial to metric)      
    -gimg:      Searcher for a random image from google         
    -goodbot:   Filler command. Bot sends a message on call.      
    -hide:      Removes the messages of a user from a channel      
    -kg:        Turn kg into lb (metric to imperial)      
    -killbot:   Turns the bot off (admin only)   
    -lb:        Turn lb into kg (imperial to metric)   
         
Reactions = Bot adds a reaction to a message that contains certain keywords   
    -addreact:  Add a reaction to a keyword/keywords   
    -rmreact:   Removes a reaction to a keyword/keywords   
        
Reddit = Parsing reddit for you   
    -rbon:      Best Of N from a subreddit   
    -rrand:     Random search result from a subreddit   
    -rrsearch:  Random post from search results      
    -rsearch:   Top post from reddit search      
    -rtop:      Top post from hot section of subreddit   
         
Youtube = Parsing Youtube         
    -randyt:    Random result of a topic from youtube      
    -yt:        First result from youtube of a topic      
     
# Known bugs:      
-Encoding problems in logging the messages.          
-Certain subreddits cause unexpected behaviour in the random function.       
   
# TODO:   
- TODO make bot save images   
- TODO MAKE bot play music - bot can currently join/leave channels   
