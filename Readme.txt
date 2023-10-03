OSU MOTO Parking Locator Bot ReadME

This is a simple Discord bot written in Python using the discord.py library. The bot is designed to calculate the Euclidean distance between a user-specified location and a list of predefined coordinates. It can also generate links to view the closest coordinate on Apple Maps or Google Maps.
Prerequisites

Before you can use this bot, you will need the following:

    Python 3: Make sure you have Python 3.x installed on your system.

    Discord Bot Token: You must have a Discord bot token to run this bot. You can obtain one by creating a new bot application on the Discord Developer Portal.

    Required Python Libraries: Install the necessary Python libraries by running the following command:

    bash

    pip install discord.py

Setup

    Clone or download this repository to your local machine.

    Replace 'ENTER YOUR BOT TOKEN' in the code with your actual bot token obtained from the Discord Developer Portal:

    python

    TOKEN = 'YOUR_BOT_TOKEN'

    Customize the list of coordinates in the coordinates variable. You can add or remove coordinates as needed.

    Save the changes to the code.

Usage

    Invite your bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.

    Run the bot script using the following command:

    bash

python3 moto.py

Once the bot is running, you can use the !nearest command followed by a location in one of the supported formats:

    (44.5704414, -123.2792012) format
    44.71306° N, 123.00436° W format

Example usage:

diff

    !nearest (44.5704414, -123.2792012)
    !nearest 44.71306° N, 123.00436° W

    The bot will respond with the closest coordinate to the specified location, along with the distance and a link to view it on Apple Maps or Google Maps.

Supported Location Formats

The bot supports two location formats:

    (44.5704414, -123.2792012) format: Specify the latitude and longitude within parentheses and separated by a comma.

    44.71306° N, 123.00436° W format: Specify the latitude in degrees and minutes with N (North) or S (South) and the longitude in degrees and minutes with E (East) or W (West).

Credits

ChatGPT + Me 
