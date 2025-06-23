import re

from collections import Counter

############### Domain ###############
# 요구사항 2,3 - IP 주소 추출 및 빈도 계산
class IpCounter:
    # 요구사항 - re 모듈을 사용해 IP 정규 표현식 정의
    # 요구사항 - Counter로 빈도 계산
    def __init__(self, logData):
        ip_pattern = re.compile(r'(\d{1,3}(?:\.\d{1,3}){3})')
        ip_list = ip_pattern.findall(logData)
        self._counter = Counter(ip_list)

    def getAllCount(self):
        return '\n'.join([f"{ip} : {count}" for ip, count in self._counter.items()])

    def getTopCount(self):
        return '\n'.join([f"{ip} : {count}" for ip, count in self._counter.most_common(3)])

######################################