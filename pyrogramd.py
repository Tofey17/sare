from pyrogram import Client, filters

bot_token = "6731536783:AAEAG7kqwpquRZRd5ZtxdYGFo5Jro7F0wJo"

api_id = 27726956
api_hash = "a9528fa819d420fc5c0b6d04a77e05f0"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

