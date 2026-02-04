import requests
from bs4 import BeautifulSoup
import os

URL = "https://example.com/news"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

html = requests.get(URL, timeout=15).text
soup = BeautifulSoup(html, "html.parser")

# ⚠️ sửa selector cho đúng website
latest_title = soup.select_one(".news-title a").text.strip()

last_file = "last.txt"
last_title = ""

if os.path.exists(last_file):
    last_title = open(last_file).read().strip()

if latest_title != last_title:
    send_telegram(f"📰 Tin mới:\n{latest_title}")
    open(last_file, "w").write(latest_title)
