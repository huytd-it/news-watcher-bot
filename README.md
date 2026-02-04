# News Watcher Bot 📰

Bot tự động theo dõi tin tức từ website trường ĐH Khoa học Tự nhiên (HCMUS) và gửi thông báo qua Telegram.

## 🚀 Tính năng

- 🕵️ **Theo dõi tin tức**: Tự động kiểm tra các bài viết mới tại chuyên mục [Tốt nghiệp](https://hcmus.edu.vn/tag/tot-nghiep/).
- 📢 **Thông báo Telegram**: Gửi tin nhắn chứa tiêu đề, ngày đăng và link bài viết ngay khi có tin mới.
- 🔄 **Tự động hóa**: Chạy định kỳ vào 9:00 sáng hàng ngày thông qua GitHub Actions.
- 💾 **Lưu trạng thái**: Ghi nhớ tin tức cuối cùng đã xử lý để tránh gửi trùng lặp.

## 🛠 Cài đặt & Chạy cục bộ

### Yêu cầu

- Python 3.11+
- Tài khoản Telegram và Bot Token.

### Các bước thực hiện

1. **Clone repository**:

   ```bash
   git clone https://github.com/huytd-it/news-watcher-bot.git
   cd news-watcher-bot
   ```

2. **Cài đặt thư viện**:

   ```bash
   pip install -r requirements.txt
   ```

   _Lưu ý: Nếu chưa có file `requirements.txt`, bạn có thể cài thủ công:_

   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

3. **Cấu hình biến môi trường**:
   Tạo file `.env` tại thư mục gốc và thêm thông tin bot của bạn:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   CHAT_ID=your_telegram_chat_id
   ```

4. **Chạy thử**:
   ```bash
   python bot.py
   ```

## ⚙️ Cấu hình GitHub Actions

Project đã được cấu hình sẵn để chạy trên GitHub Actions.

1. Vào repository của bạn trên GitHub.
2. Vào **Settings** > **Secrets and variables** > **Actions**.
3. Thêm 2 secret mới:
   - `BOT_TOKEN`: Token của bot Telegram.
   - `CHAT_ID`: ID của người nhận hoặc group chat.

Bot sẽ tự động chạy vào 9h sáng mỗi ngày (theo cấu hình trong `.github/workflows/news.yml`).

## 📂 Cấu trúc dự án

- `bot.py`: Script chính thực hiện việc cào dữ liệu và gửi thông báo.
- `last.txt`: File lưu link của bài viết mới nhất đã xử lý (được Bot tự động cập nhật).
- `.github/workflows/news.yml`: Cấu hình GitHub Actions.

## 📝 Lưu ý

- File `last.txt` sẽ được GitHub Actions tự động commit và push sau mỗi lần chạy để lưu trạng thái.
- Nếu muốn thay đổi nguồn tin, bạn có thể sửa biến `URL` và selector trong `bot.py`.
