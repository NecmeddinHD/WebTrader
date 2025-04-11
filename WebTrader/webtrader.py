def main():

    import requests
    import pyperclip
    import config

    TOKEN = "7745947395:AAGA43r6kc_9xajySwxXsNTI_wZGJlJjzkk"
    chat_id = config.chatid
    link = pyperclip.paste()

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": link}

    response = requests.post(url, data=data)

if __name__ == "__main__":
    main()