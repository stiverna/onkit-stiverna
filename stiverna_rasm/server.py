from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '6751101177:AAFZkSVkD7Vt8YH1f0XWxq2OR9kkUc4rbk0'  # <-- Bu yerga tokeningizni yozing
CHANNEL_ID = '@foydalanuvchilarombori'  # Kanal username yoki -100... ko‘rinishidagi ID

@app.route("/upload", methods=["POST"])
def upload():
    photo = request.files.get("photo")
    if not photo:
        return "❌ Rasm topilmadi", 400

    telegram_api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {"photo": (photo.filename, photo.read())}
    data = {"chat_id": CHANNEL_ID}
    r = requests.post(telegram_api, files=files, data=data)

    if r.ok:
        return "✅ Kanalga yuborildi!"
    else:
        return f"❌ Xato: {r.text}", 500

if __name__ == "__main__":
    app.run(port=5002)
