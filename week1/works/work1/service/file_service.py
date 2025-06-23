from domain.student_scores import StudentScores
from common.exception.base_exception import BaseException
from common.exception.base_exception import FileNotExistException
from common.exception.base_exception import ValueException
from common.exception.base_exception import ScoreException

############### File I/O Service ###############
# 파일 입, 출력 서비스 클래스
# 파라미터 : Env
class FileService:
    def __init__(self, env):
        self.env = env
        self.studentScores = StudentScores()

    # 로컬에 위치한 학생 txt 데이터 로드
    def loadLocalData(self):
        try:
            with open(self.env.readDataFile, 'r', encoding='utf-8') as file :
                lines = file.readlines()
                for line in lines:
                    line = line.strip()  # 줄 끝 공백 제거
                    if not line:        # 빈 줄 무시
                        continue
                    name, score_str = line.split(',')
                    score = int(score_str)  # 점수는 정수로 변환
                    if score < 0 or score > 100:
                        raise ScoreException()
                    self.studentScores.create(name, score)
                return self.studentScores
        except FileNotFoundError:
            raise FileNotExistException()
        except ValueError:
            raise ValueException()
        except:
            raise BaseException()
    
    # 요구사항 5 - 학생 데이터 평균 미만 학생 저장
    def save_below_average(self, studentScores):
        average = studentScores.calculate_average()
        with open(self.env.saveDataFile, 'w', encoding='utf-8') as file:
            for name, score in studentScores.data.items():
                if score < average:
                    file.write(f'{name},{score}\n')
        print(f"평균 미만 학생 목록이 '{self.env.saveDataFile}'에 저장되었습니다.")
        pass
        
    # 원격에 위치한 학생 데이터 로드 - TBD
    def loadRemoteData(self):
        pass
################################################