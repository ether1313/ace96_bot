# Ace96au Promo Bot 🎰

A full-featured Telegram marketing bot with Web App inline window, custom keyboard, promotional message push, and more.

## ✨ Features

- 🎯 **Main Menu** - Display main menu when users send `/start`
- ⌨️ **Custom Keyboard** - Interactive buttons at the bottom
- 🌐 **Web App Inline Window** - `TRY LUCK` button opens inline website
- 📢 **Promotional Messages** - Send promotional messages with text
- 🔘 **Interactive Buttons** - Inline buttons in messages that can jump to external links or channels

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your configuration:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
WEB_APP_URL=https://your_webapp_deployment_url
TELEGRAM_CHANNEL=https://t.me/your_channel
FREE_SPIN_URL=https://your_free_spin_link
FREE_CREDIT_URL=https://your_free_credit_link
```

### 3. Get Bot Token

1. Search for `@BotFather` in Telegram
2. Send `/newbot` to create a new bot
3. Follow the prompts to set bot name and username
4. Copy the Bot Token to the `.env` file

### 4. Deploy Web App

The Web App needs to be deployed to a publicly accessible URL. You can use:

- **GitHub Pages** (Free)
- **Vercel** (Free)
- **Netlify** (Free)
- **Your own server**

Upload the files in the `webapp/` directory to your server and ensure they are accessible via HTTPS.

### 5. Run Bot

```bash
python bot.py
```

## 📁 Project Structure

```
ace96_bot/
├── bot.py              # Main bot file
├── config.py           # Configuration file
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables example
├── .env                # Environment variables (needs to be created)
├── README.md           # Project documentation
└── webapp/             # Web App files
    └── index.html      # Main page (iframe embedding website)
```

## 🎮 Usage

### Bot Commands

- `/start` - Display main menu

### Button Functions

1. **TRY LUCK ✨** - Opens inline Web App, displays website (https://ace96au.com/)
2. **GET FREE SPIN ON COLA13 ✨** - Shows free spin promotional information
3. **HOT GAME TIPS CHANNEL ☎️** - Shows hot game tips channel information

### Web App Function

- Embeds website (https://ace96au.com/) in Telegram Web App window
- Fullscreen iframe display
- Integrated with Telegram Web App API

## 🔧 Customization

### Modify Promotional Text

Edit the text content in the `bot.py` file:

```python
# Modify in handle_get_free_spin() function
promo_text = """Your promotional text..."""
```

### Modify Web App

Edit `webapp/index.html` to customize the embedded website URL or add additional features.

## 📝 Notes

1. **Web App URL must be HTTPS** - Telegram requires Web App to be accessible via HTTPS
2. **Keep Bot Token secret** - Do not commit `.env` file to Git
3. **Server requirements** - Bot needs to run continuously, recommend using a server or cloud service
4. **Web App domain** - Need to configure allowed domains in Bot settings (via @BotFather)

## 🛠️ Deployment Recommendations

### Local Testing

```bash
python bot.py
```

### Server Deployment

Recommend using `systemd` or `supervisor` to manage the bot process, ensuring 24/7 operation.

### Web App Deployment

1. Upload the `webapp/` directory to your server
2. Configure Nginx or Apache to provide HTTPS access
3. Fill in the URL in the `WEB_APP_URL` field of the `.env` file

## 📞 Support

If you encounter issues, please check:
- Whether the Bot Token is correct
- Whether the Web App URL is accessible (must be HTTPS)
- Whether the network connection is normal
- Error messages in log files

## 📄 License

MIT License

---

**Ace96au Promo Bot** - Making marketing simpler! 🚀
