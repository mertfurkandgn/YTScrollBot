# YouTube Liked Videos Auto Scroll

A Python script that automatically scrolls through your YouTube liked videos playlist to load all videos.

## 🚀 Features

- Automatic scrolling of YouTube liked videos page
- Connects to existing Chrome session using Selenium WebDriver
- Dynamic content loading support
- Bilingual support (Turkish/English)

## 📋 Requirements

- Python 3.x
- Google Chrome
- Required Python packages:
  ```
  selenium
  PySocks
  webdriver-manager
  ```

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/youtube_liked_auto_scroll.git
   cd youtube_liked_auto_scroll
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. Start Chrome in debug mode:

   **For Windows:**
   ```bash
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebugSession"
   ```

   **For macOS:**
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug"
   ```

2. Run the script:
   ```bash
   python main.py
   ```

## ⚠️ Notes

- The Chrome session opened in debug mode won't affect your existing Chrome profile
- The script will automatically scroll through your YouTube liked videos page
- The script will stop automatically when it reaches the bottom of the page

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 📧 Contact

Feel free to open an issue for any questions or suggestions.
