############### Domain ###############
# 요구사항 1 - 학생 도메인 클래스
# 외부로부터 이름, 점수를 전달받아 딕셔너리 형태로 저장
class StudentScores:
    # 요구사항 2 - 생성자
    def __init__(self):
        self.data = {} 

    # 요구사항 2 - 학생 데이터 딕셔너리에 저장
    def create(self, name, score):
        self.data[name] = score

    # 요구사항 3 - 학생 데이터 평균 점수 계산
    def calculate_average(self):
        return sum(self.data.values()) / len(self.data)

    # 요구사항 4 - 학생 데이터 평균 이상 리스트 반환
    # 보기 좋게 리스트 형태의 튜플로 반환하였습니다.
    def get_above_average(self):
        average = self.calculate_average()
        return [(name, score) for name, score in self.data.items() if score >= average]

    # 요구사항 6 - 평균 점수와 평균 이상 학생 리스트 출력
    def print_summary(self):
        average = self.calculate_average()
        above_avg = self.get_above_average()
        print(f"전체 평균 점수: {average:.2f}")
        print(f"평균 이상 학생 목록: {above_avg}")

    # 학생 데이터 딕셔너리 타입으로 읽기 - TBD
    def read(self):
        return self.data

    # 학생 데이터 수정 - TBD
    def update(self, name, score):
        pass

    # 학생 데이터 삭제 - TBD
    def delete(self, name):
        pass
######################################