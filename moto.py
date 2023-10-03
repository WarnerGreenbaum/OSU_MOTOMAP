import discord
from discord.ext import commands
import math
import re

# Bot token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
TOKEN = 'ENTER YOUR BOT TOKEN'

# Intents for your bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# List of different coordinate locations
coordinates = [
    (44.56667921708827, -123.2721488226325),
    (44.5673343988714, -123.27444806723545),
    (44.5675781980027, -123.27524629342523),
    (44.567502680615206, -123.27694645851079),
    (44.567413065645994, -123.28593287187336),
    (44.56734822718914, -123.28955158980895),
    (44.56555195204904, -123.28838532788599),
    (44.564895948203045, -123.29346345867661),
    (44.564100008442004, -123.29097696874636),
    (44.563890411083655, -123.28892426141329),
    (44.56668781184314, -123.28619928055136),
    (44.56596353947806, -123.28420973985313),
    (44.564624682697044, -123.28287870763403),
    (44.56253811340572, -123.28533793303887),
    (44.56313170267141, -123.27952065477571),
    (44.5583474758176, -123.29025089644635),
    (44.55788649000577, -123.29068967727667),
    (44.557736642749035, -123.2858855345511),
    (44.55757364732466, -123.28525838754325),
    (44.5594538755843, -123.28532666571239),
    (44.559899511457274, -123.28387539544411),
    (44.560937781581956, -123.27603876399728),
    (44.56418694707502, -123.27587211097355),
    (44.56325998864593, -123.27430725658303),
    (44.56360677122006, -123.27389668347823),
    (44.56245789690233, -123.27395716199207),
    (44.564462165267564, -123.27077290587373)
]


# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to calculate Euclidean distance between two points
def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to parse latitude and longitude from various formats
def parse_coordinates(location):
    # Pattern for matching latitude and longitude in (44.5704414, -123.2792012) format
    pattern1 = r'\((-?\d+\.\d+), (-?\d+\.\d+)\)'

    # Pattern for matching latitude and longitude in 44.71306° N, 123.00436° W format
    pattern2 = r'(-?\d+\.\d+)° ([NS]), (-?\d+\.\d+)° ([WE])'

    # Try to match each pattern
    match1 = re.match(pattern1, location)
    match2 = re.match(pattern2, location)

    if match1:
        lat, lng = map(float, match1.groups())
        return lat, lng, False  # False indicates non-Apple Maps format
    elif match2:
        lat, lat_dir, lng, lng_dir = match2.groups()
        lat = float(lat)
        lng = float(lng)
        if lat_dir == 'S':
            lat *= -1
        if lng_dir == 'W':
            lng *= -1
        return lat, lng, True  # True indicates Apple Maps format
    else:
        raise ValueError("Invalid location format")

@bot.command()
async def nearest(ctx, *, location: str):
    # Extract latitude, longitude, and format indicator using the parse_coordinates function
    try:
        lat, lng, is_apple_maps_format = parse_coordinates(location)
    except ValueError:
        await ctx.send("Invalid location format. Please use one of the following formats: " +
                       "(44.5704414, -123.2792012), 44.71306° N, 123.00436° W")
        return

    user_coordinates = (lat, lng)

    # Initialize variables to track the closest coordinate and its distance
    closest_coordinate = None
    closest_distance = float('inf')  # Initialize with positive infinity

    # Iterate through the coordinate list to find the closest one
    for coordinate in coordinates:
        distance = calculate_distance(user_coordinates, coordinate)
        if distance < closest_distance:
            closest_coordinate = coordinate
            closest_distance = distance

    # Generate a link for Apple Maps or Google Maps based on the format
    if is_apple_maps_format:
        maps_link = f"https://maps.apple.com/?q={closest_coordinate[0]},{closest_coordinate[1]}"
    else:
        maps_link = f"https://www.google.com/maps?q={closest_coordinate[0]},{closest_coordinate[1]}"

    await ctx.send(f"The closest coordinate to your location is {closest_coordinate} with a distance of {closest_distance}.\n{maps_link}")

# Run the bot
bot.run(TOKEN)
