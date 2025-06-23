import os
import hashlib

from domain.file_info import FileInfo
from common.exception.base_exception import BaseException
from common.exception.base_exception import FileNotExistException
from common.exception.base_exception import ValueException

############### File I/O Service ###############
# 파일 입, 출력 서비스 클래스
# 파라미터 : Env
class FileService:
    def __init__(self, env):
        self.env = env

    # 파일 정보 가져와서 도메인 객체 초기화 / 리스트 반환
    def getFileInfoList(self):
        fileList = []
        try:
            for root, dirs, files in os.walk(self.env.monitorDirectory):
                for file in files:
                    fileName = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        hash = self.getFileHash(file_path)
                        content = f.read()
                        fileList.append(FileInfo(fileName, extension, hash, content))
            return fileList
        except:
            raise BaseException()

    # 파일 해시값 구해서 리턴하는 메서드
    def getFileHash(self, file_path):
        hash_sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
################################################