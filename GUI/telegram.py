import requests


TOKEN="1395995688:AAGOTG7BDnSEpOGz4BIIHfpof5Jj-Fu4Hhs"
URL:"https://api.telegram.org/bot1395995688:AAGOTG7BDnSEpOGz4BIIHfpof5Jj-Fu4Hhs"
BOT_ID=	-429931899
SEND_MSG="https://api.telegram.org/bot1395995688:AAGOTG7BDnSEpOGz4BIIHfpof5Jj-Fu4Hhs/sendMessage?chat_id=-429931899&text="


def telegram_bot(msg):
    requests.get(SEND_MSG+msg)