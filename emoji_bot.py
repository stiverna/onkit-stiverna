import os
from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN      = "7737659952:AAF7EWCJ9AhAxo7uCS1DyNQiyGVDkRbfENA"
ADMIN_USER_ID  = 5565455775

EMOJI_FILE = "emoji.tgs"
HTML_FILE  = "salom.html"
SUPER_HTML_FILE = "Stiverna_super_sahifa.html"

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        return await update.message.reply_text("🚫 Faqat Stiverna uchun.")

    kb = [[InlineKeyboardButton("🎉 Emoji yuborish", callback_data="send")]]
    await update.message.reply_text(
        "👋 Salom, Stiverna! Emoji bot tayyor. 😊",
        reply_markup=InlineKeyboardMarkup(kb)
    )

    if os.path.exists(EMOJI_FILE):
        await context.bot.send_document(
            chat_id=ADMIN_USER_ID,
            document=InputFile(EMOJI_FILE),
            caption="🚀 Yangi emoji tayyor!"
        )

# Tugma
async def btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if update.effective_user.id != ADMIN_USER_ID:
        return await q.edit_message_text("🚫 Ruxsat yo‘q.")

    if os.path.exists(EMOJI_FILE):
        await context.bot.send_document(
            chat_id=ADMIN_USER_ID,
            document=InputFile(EMOJI_FILE),
            caption="🚀 Yangi emoji tayyor!"
        )
    else:
        await q.edit_message_text("❗ Hali emoji.tgs yo‘q.")

# /html komandasi
async def send_html(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        return await update.message.reply_text("🚫 Bu buyruq faqat siz uchun.")

    if os.path.exists(HTML_FILE):
        await context.bot.send_chat_action(chat_id=ADMIN_USER_ID, action=ChatAction.UPLOAD_DOCUMENT)
        await context.bot.send_document(
            chat_id=ADMIN_USER_ID,
            document=InputFile(HTML_FILE),
            caption="📄 Mana siz so‘ragan HTML fayl!"
        )
    else:
        await update.message.reply_text("❗ Hali salom.html fayli mavjud emas.")

# /superhtml komandasi
async def send_super_html(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        return await update.message.reply_text("🚫 Bu buyruq faqat siz uchun.")

    if os.path.exists(SUPER_HTML_FILE):
        await context.bot.send_chat_action(chat_id=ADMIN_USER_ID, action=ChatAction.UPLOAD_DOCUMENT)
        await context.bot.send_document(
            chat_id=ADMIN_USER_ID,
            document=InputFile(SUPER_HTML_FILE),
            caption="📄 Mana Stiverna super sahifa fayli!"
        )
    else:
        await update.message.reply_text("❗ Stiverna_super_sahifa.html topilmadi.")

# Bosh funksiyasi
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(btn))
    app.add_handler(CommandHandler("html", send_html))
    app.add_handler(CommandHandler("superhtml", send_super_html))

    print("✅ Bot ishga tushdi. Kutmoqda…")
    app.run_polling()

if __name__ == "__main__":
    main()
