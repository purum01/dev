from django.test import TestCase

import uuid
print(uuid.uuid1())  #호스트ID, 시퀀스, 현재시간을 기준으로 uuid를 생성
print(uuid.uuid4())  #랜덤 UUID를 생성

'6b1a0b18-cab1-11eb-8078-a0c589ad880a'
'9859cc2b-e9d5-4a6f-ba91-9d1902564f14'
'b8890a3a-cab1-11eb-8026-a0c589ad880a'
'1157e2cb-1d4c-49e1-b2fa-2438b66a7d09'