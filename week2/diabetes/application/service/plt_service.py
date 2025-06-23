import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from application.service.csv_service import CsvService

############### PltService ###############
# 데이터 처리 클래스
class PltService:
    # 생성자
    def __init__(self):
        self.csvService = CsvService()
        dto = self.csvService.getCsvDataDto()
        self.entity = dto.toEntity()
    
    # 결측치 처리
    def step1(self):
        cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
        # 0을 NaN으로 치환
        self.entity.df[cols_with_zero] = self.entity.df[cols_with_zero].replace(0, np.nan)
        # 각 열 평균으로 NaN 대체
        self.entity.df[cols_with_zero] = self.entity.df[cols_with_zero].apply(lambda x: x.fillna(x.mean()))

    # 이상치 처리
    def step2(self):
        for col in ['SkinThickness', 'Insulin']:
            threshold = self.entity.df[col].quantile(0.99)
            mean_val = self.entity.df[col].mean()
            self.entity.df[col] = self.entity.df[col].apply(lambda x: mean_val if x > threshold else x)

    # 정규화 처리
    def step3(self):
        scaler = MinMaxScaler()
        df_scaled = pd.DataFrame(
            scaler.fit_transform(self.entity.df.drop('Outcome', axis=1)),
            columns=self.entity.df.columns[:-1]
        )
        df_scaled['Outcome'] = self.entity.df['Outcome'].values
        self.entity.df = df_scaled

    # 각 열의 결측치 개수 출력
    def eda1(self):
        print("각 열의 NaN 개수:")
        print(self.entity.df.isnull().sum())
        print("\n각 열의 0 값 개수:")
        print((self.entity.df == 0).sum())

    # Outcome 별 Gluecose 평균 출력
    def eda2(self):
        print("\nOutcome 별 Glucose 평균:")
        print(self.entity.df.groupby('Outcome')['Glucose'].mean())

    # 전처리 후 데이터프레임 상위 5개 행 출력
    def eda3(self):
        print("\n전처리 완료 후 데이터프레임 상위 5개:")
        print(self.entity.df.head())