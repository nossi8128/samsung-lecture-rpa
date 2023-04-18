import requests
import os
import json
import urllib3
from base64 import b64encode
from dotenv import load_dotenv

# .env 환경변수 로드
load_dotenv(verbose=True)
# requests warning OFF
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# api docs: https://developers.samsung.net/ 참고
class KnoxEmail:
    def __init__(self):
        # basic auth for API - 결재 승인 시 발급됨
        self.auth = f'Bearer {os.getenv("KNOX_TOKEN")}'
        # knox ip address 설정 - 결재 승인 시 발급됨
        self.base_url = os.getenv("KNOX_BASE_URL")
        self.id = os.getenv("KNOX_ID")

    def imageContent(filename):
        return "<P><img src='data:image\/png;base64, {}'/></P>".format(b64encode(open(filename, 'rb').read()).decode())

    # Knox 메시지 전송 API호출
    # sender - 발신인의 knox id
    # recipients - 수신인의 knox id list
    # cc - 참조 수신인의 knox id list
    # mail_title - 메일 제목
    # mail_text - 하고싶은말
    def send_knox_email(self, sender, recipients, cc, mail_title, mail_text):
        try:
            recipient_list = [{
                "emailAddress": f"{recipient}@samsung.com",
                "recipientType": "TO",
            } for recipient in recipients]

            cc_list = [{
                "emailAddress": f"{c}@samsung.com",
                "recipientType": "cc",
            } for c in cc]

            payload = {
                "subject": mail_title,
                "contents": mail_text,
                "contentType": "HTML",
                "docsecuType": "OFFICIAL",
                "sender": {
                    "emailAddress": f"{sender}@samsung.com",
                },
                "recipients": recipient_list
            }

            requests.post(f"developers.samsung.net/mail/api/v2.0/mails/send?userId={sender}", data,


                          )
