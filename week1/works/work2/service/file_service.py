import os
from collections import Counter

from domain.ip_counter import IpCounter
from common.exception.base_exception import BaseException
from common.exception.base_exception import FileNotExistException
from common.exception.base_exception import ValueException

############### File I/O Service ###############
# 파일 입, 출력 서비스 클래스
# 파라미터 : Env
class FileService:
    def __init__(self, env):
        self.env = env

    # 요구사항 1 - 사용자 입력: 로그 파일 경로
    def loadLogData(self, logPath):
        # 파일 존재 여부 확인
        if not os.path.exists(logPath):
            raise FileNotExistException()
        try:
            with open(logPath, 'r', encoding='utf-8') as file :
                 logData = file.read()
                 ipCounter = IpCounter(logData)
            return ipCounter
        except ValueError:
            raise ValueException()
        except:
            raise BaseException()
    
    # 요구사항 4 - 분석 결과 CSV 저장
    def saveLogData(self, ipCounter):
        with open(self.env.saveDataFile, 'w', encoding='utf-8-sig') as f:
            f.write("전체 IP 주소 빈도:\n")
            f.write(ipCounter.getAllCount())
            f.write("\n\n상위 3개 IP 주소:\n")
            f.write(ipCounter.getTopCount())
            print(f"평균 미만 학생 목록이 '{self.env.saveDataFile}'에 저장되었습니다.")
################################################