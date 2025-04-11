import requests
import pyperclip
import time
import config # type: ignore
chat_id = config.chatid
TOKEN = "7745947395:AAGA43r6kc_9xajySwxXsNTI_wZGJlJjzkk"
#you can give info with telegram @userinfobot use id line / TR infoyu telegram @userinfobot botu ile alabilirsiniz id satırını kullanıcaksınız
link = pyperclip.paste()

# Linki gönder
send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": chat_id, "text": link}
response = requests.post(send_url, data=data)
print("Link gönderildi:", response.status_code)

# Gelen mesajları dinle
last_update_id = None

while True:
    updates_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    if last_update_id:
        updates_url += f"?offset={last_update_id + 1}"

    res = requests.get(updates_url)
    updates = res.json()

    if "result" in updates:
        for result in updates["result"]:
            last_update_id = result["update_id"]
            message = result.get("message", {})
            sender_id = str(message.get("from", {}).get("id", ""))
            text = message.get("text", "")

            if sender_id == chat_id:
                print(f"Gelen mesaj: {text}")

    time.sleep(2)
