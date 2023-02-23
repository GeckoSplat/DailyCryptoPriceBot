# Telegram Bot to send crypto coin prices to a Telegram group after aquiring them from the coinmarketcap.com API.

1. Clone or download this project.
2. Create a virtual environment with python in the same directory as this project.
3. Run the virtual environment, then in the terminal type "pip install -r requirements.txt"
4. Rename the "examples" folder to "json".
5. In the newly named json folder remove the "ex_" prefix from each file it contains.
6. Input your api keys in the correct json files in the json folder (open the json files for instructions).


You will need to create or have an existing Telegram group you want to send the messages to .
Get the Chat ID of this group by inviting GetIDs Bot to it . Copy Chat ID from the information that produces within the group. You can then remove GetIDs Bot from the group.

Your Telegram bot will run when commanded on a terminal for testing purposes but it's intended to be used as a cron job on a server or AWS lambda.

To use on AWS you will need to compile it to an AWS package and upload it . There are many youtube video's on this.

Once done you can set it to run as a cron job at what ever time and interval you wish on AWS lambda.
 
You can change the coin prices you send by ammending the list here in the main.py file on line 30 :


    `coinlist = ["DOGE", "BONK", "ADA"]`

If you change this directly on AWS you will not have to compile a package for it every time.

If using AWS there are some additonal lines of code that are commented out in the main.py file. There are instructions in the file on what to comment out to make the bot run on AWS.
