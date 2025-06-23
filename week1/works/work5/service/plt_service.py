import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

############### PltService ###############
# 시각화 클래스
class PltService:
    # 생성자
    def __init__(self, df):
        # 사용할 한글 폰트 경로 설정 (굴림체)
        self.fontPath = 'C:\\Windows\\Fonts\\gulim.ttc'
        # matplotlib에서 인식할 폰트 이름 추출
        self.font = fm.FontProperties(fname=self.fontPath).get_name()
        self.df = df

    # 시각화 실행 메서드
    def run(self):
        subject_means = self.df[['수학', '영어', '과학']].mean()            # 과목별 평균 점수 계산
        self.df['평균'] = self.df[['수학', '영어', '과학']].mean(axis=1)     # 학생별 평균 점수 컬럼 추가
        top5 = self.df.sort_values(by='평균', ascending=False).head(5)     # 평균 점수 기준 상위 5명 추출
        plt.rc('font', family=self.font)                                   # 한글 폰트 설정

        # 시각화 (과목별 평균 점수)
        plt.figure(figsize=(8, 6))                  # 그래프 크기 설정
        plt.bar(subject_means.index,                # 그래프 데이터 추가
                subject_means.values,
                color=['red', 'green', 'blue']
                )
        plt.title('과목별 평균 점수')                 # 축 제목 설정
        plt.xlabel('과목')                          # X축 레이블 설정
        plt.ylabel('평균 점수')                      # Y축 레이블 설정
        plt.ylim(50, 100)                          # y축 값의 범위를 50부터 100까지로 설정 (점수 범위 고정)
        plt.grid(True, linestyle='--', alpha=0.5)  # 그래프에 점선 형태의 격자선 추가 (반투명)
        plt.show()                                 # 그래프 출력

        # 시각화 (평균 점수 상위 5명)
        plt.figure(figsize=(8, 6))                   # 그래프 크기 설정
        plt.bar(top5['이름'],                        # 그래프 데이터 추가
                top5['평균'],
                color='purple'
                )
        plt.title('평균 성적 상위 5명')                 # 축 제목 설정
        plt.xlabel('이름')                            # X축 레이블 설정
        plt.ylabel('평균 점수')                        # Y축 레이블 설정
        plt.ylim(50, 100)                            # y축 값의 범위를 50부터 100까지로 설정 (점수 범위 고정)
        plt.grid(True, linestyle='--', alpha=0.5)    # 그래프에 점선 형태의 격자선 추가 (반투명)
        plt.show()                                   # 그래프 출력