import numpy as np
import pandas as pd

############### Domain ###############
# SalesAnalysis 도메인 클래스
class SalesAnalysis:
    # 생성자
    def __init__(self):
        # 2024년 1월 1일부터 12월 31일까지 날짜 생성
        self.dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq='D')
        # 각 날짜에 대해 1000 ~ 10000 사이의 랜덤 매출 데이터 생성
        self.sales = np.random.randint(1000, 10001, size=len(self.dates))
        # 날짜와 매출을 데이터프레임으로 저장
        self.df = pd.DataFrame({'Date': self.dates, 'Sales': self.sales})

    # DataFrame 반환 메서드
    def getDf(self):
        return self.df