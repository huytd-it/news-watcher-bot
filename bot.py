import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://hcmus.edu.vn/tag/tot-nghiep/"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

html = requests.get(URL, headers=headers, timeout=15).text
soup = BeautifulSoup(html, "html.parser")


# ⚠️ sửa selector cho đúng website
items = soup.select(".cmsmasters_archive_type")

last_file = "last.txt"
last_seen = ""

if os.path.exists(last_file):
    with open(last_file, encoding="utf-8") as f:
        last_seen = f.read().strip()

new_posts = []

for item in items:
    title_el = item.select_one(".cmsmasters_archive_item_title.entry-title a")
    if not title_el:
        continue

    title = title_el.text.strip()
    link = title_el.get("href")
    date_el = item.select_one(".published.cmsmasters_archive_item_date")
    date = date_el.text.strip() if date_el else "??"

    # Chống trùng lặp: check link HOẶC title (để tương thích ngược với file cũ)
    if link == last_seen or title == last_seen:
        break

    new_posts.append({
        "title": title,
        "link": link,
        "date": date
    })

# Nếu chạy lần đầu (chưa có last_file) hoặc mất dấu, chỉ lấy tin mới nhất để tránh spam
if not last_seen and new_posts:
    new_posts = [new_posts[0]]

if new_posts:
    # Gửi từ tin cũ nhất đến mới nhất trong danh sách mới
    for post in reversed(new_posts):
        msg = f"📰 Tin mới: {post['title']}\n📅 Ngày đăng: {post['date']}\n🔗 Link: {post['link']}"
        send_telegram(msg)
    
    # Lưu lại link của tin mới nhất
    with open(last_file, "w", encoding="utf-8") as f:
        f.write(new_posts[0]["link"])
