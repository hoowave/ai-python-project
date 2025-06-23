import pandas as pd
import matplotlib.pyplot as plt

from env import Env

############### PltService ###############
# 시각화 클래스
class PltService:
    # 생성자
    def __init__(self, env):
        self.env = env
        csvData = pd.read_csv(env.dataPath, encoding='cp949', low_memory=False)     # CSV 불러오기
        self.df = pd.DataFrame(csvData)                                             # 교통사고 데이터 분석을 위한 DataFrame 초기화

    # 데이터 처리 메서드
    def process(self):
        grouped = self.df.groupby('가해자법규위반')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum().reset_index()   # 가해자법규위반별 총합
        grouped['주야'] = '총합'
        result = pd.concat([self.df, grouped], ignore_index=True)                                                                 # 원본 데이터 + grouped 합치기
        result = result.sort_values(by=['가해자법규위반', '주야']).reset_index(drop=True)                                            # 보기 좋게 정렬
        total_sum = result[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum().to_frame().T                          # 전체 총합 구하기
        total_sum.insert(0, '가해자법규위반', '전체합계')
        total_sum.insert(1, '주야', '총합')
        self.df = pd.concat([result, total_sum], ignore_index=True)                                                               # 전체 총합 행 추가

    # 시각화 실행 메서드
    def run(self):
        plt.rcParams['font.family'] = self.env.fontFamily
        plt.figure(figsize=(12, 8))
        plt.barh(self.df['가해자법규위반'], self.df['사고건수'], color='skyblue')
        plt.xlabel('사고 건수')
        plt.ylabel('가해자 법규 위반')
        plt.title('부산광역시 가해운전자 법규 위반별 사고 건수')
        plt.tight_layout()
        plt.show()