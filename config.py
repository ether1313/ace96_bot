import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "7448111121:AAH90DYMs-thwmnEAnQkoZJFZkPVO9x6GA8")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/ace96au")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://ace96au.com/RFACE96AUBOT9")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://ace96au.com/RFACE96AUBOT9")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Ace96au Promo Bot"
BOT_DESCRIPTION = "Ace96au Marketing Assistant - Provides latest promotions and event information"
