import requests
import os
import json
import urllib3
from dotenv import load_dotenv
import time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import base64
import binascii

# .env 환경변수 로드
load_dotenv(verbose=True)
# requests warning OFF
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# knox 메시지 id 생성을 위한 밀리초 생성 함수
def current_time_millis(): return int(
    round(time.time() * 1000))


class AES256:
    #
    # KNOX 메시지 암호화를 위한 AES256암호화 / 복호화 클래스
    #
    def __init__(self, key, iv):
        self.key = binascii.unhexlify(key)
        self.iv = binascii.unhexlify(iv)

    def aes_encrypt(self, plaintext):
        return base64.b64encode(AES.new(self.key, AES.MODE_CBC, self.iv).encrypt(pad(plaintext.encode("utf8"), 16)))

    def aes_decrypt(self, ciphertext):
        return AES.new(self.key, AES.MODE_CBC, self.iv).decrypt(pad(base64.b64decode(ciphertext), 16))


class KnoxMessenger:
    # https://developers.samsung.net 참고
    # KNOX 메시지 발신을 위한 클래스
    def __init__(self):
        self.auth = f'Bearer{os.getenv("KNOX_TOKEN")}'  # basic auth for API
        self.base_url = os.getenv("KNOX_STAGE_URL")  # knox ip address 설정
        # knox 메시지 전송을 위한 Device 등록 API 호출
        self.device = self.register_device()["deviceServerID"]

        # knox AES 256암호화를 위한 key, iv를 받는 API 호출
        keyplusiv = self.get_cryptokey()["key"]
        self.key = keyplusiv[:64]  # AES256 key
        self.iv = keyplusiv[64:]  # AES256 iv

    def send_knox_messenger(self, target_user, message_text):
        pass
        # knox 메신저를 전송하는 메인함수
        # <knox 메세지 전송 프로세스>
        # 1. 유저_id 검색: knox id (ex. jebra.jeong)을 입력하면 시스템상 id값이 반환
        # 2. 대화방 생성: 해당 유저와의 대화방 생성 -> 대화방 정보가 AES256암호화되어 반환
        # 3. 대화방 정보 복호화: 대화방_id를 얻기 위해 서버의 응답을 복호화 -> chatroom_id에 저장
        # 4. 메세지 전송

    def send_message(self, chatroomId, message_text):
        # explain: knox 메세지 전송 API 호출
        # 인자설명
        # chatroomId - make_chatting_room 함수에서 반환한 대화방 id
        # message_text - 하고싶은 말
        #
        try:
            plaintext = json.dumps({
                "requestId": current_time_millis(),
                "chatroomId": chatroomId,
                "chatMessageParams": [{
                    "msgId": current_time_millis(),
                    "msgType": 0,
                    "chatMsg": message_text,
                    "msgTtl": 720
                }]
            })
            encrypted_data = AES256(self.key, self.iv).aes_encrypt(
                plaintext).decode('utf8')

            response = requests.post(
                # rest api 요청 주소
                f"{self.base_url}/messenger/message/api/v1.0/message/chatRequest",
                headers={
                    "Authorization": self.auth,
                    "Content-Type": "application/json",
                    "x-device-id": str(self.device),
                    "x-device-type": "relation",
                },
                data=encrypted_data,
                verify=False  # rest 통신 시 SSL 인증서를 검증하지 않음
            )
            return response._content

        except:
            print("ERROR OCCURED IN SEND_MESSAGE")
            return False
