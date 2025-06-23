############### Domain ###############
# StudentScoreAnalysis 도메인 클래스
class StudentScoreAnalysis:
    # 생성자
    def __init__(self, name, math, eng, science):
        self.name = name            # 학생 이름
        self.math = math            # 수학 점수
        self.eng = eng              # 영어 점수
        self.science = science      # 과학 점수
    
    # 중요!! 컬럼 명을 한글로 사용하기 위해 딕셔너리 자료구조로 변환
    def to_dict(self):
        return {
            '이름': self.name,
            '수학': self.math,
            '영어': self.eng,
            '과학': self.science
        }

    # 테스트를 위한 메서드
    def __str__(self):
        return f"{self.name} | 수학: {self.math}, 영어: {self.eng}, 과학: {self.science}"