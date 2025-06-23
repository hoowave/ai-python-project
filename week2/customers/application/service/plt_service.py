import pandas as pd

from application.service.csv_service import CsvService
from infrastructure.outbound.customer_output import CustomerOutput

############### PltService ###############
# 데이터 처리 클래스
class PltService:
    # 생성자
    def __init__(self):
        self.csvService = CsvService()
        self.output = CustomerOutput()
        dto = self.csvService.getCsvDataDto()
        self.entity = dto.toEntity()
        
    def processEda1(self):
        print("성별에 따른 평균 소비 점수")
        self.output.showTable(self.entity.df, 'Gender', 'Spending Score (1-100)')
        self.output.showChart(self.entity.df, 'Gender', 'Spending Score (1-100)', kind='pie')

    def processEda2(self):
        print("연 소득 구간별 평균 소비 점수")
        bins = [0, 30, 60, 90, 120, 150]
        labels = ['0-30', '30-60', '60-90', '90-120', '120-150']
        self.entity.df['IncomeGroup'] = pd.cut(self.entity.df['Annual Income (k$)'], bins=bins, labels=labels)
        self.output.showTable(self.entity.df, 'IncomeGroup', 'Spending Score (1-100)')
        self.output.showChart(self.entity.df, 'IncomeGroup', 'Spending Score (1-100)', kind='line')
    
    def processEda3(self):
        print("연령대별 평균 소비 점수")
        bins = [0, 20, 30, 40, 50, 60, 100]
        labels = ['10대', '20대', '30대', '40대', '50대', '60대+']
        self.entity.df['AgeGroup'] = pd.cut(self.entity.df['Age'], bins=bins, labels=labels)
        self.output.showTable(self.entity.df, 'AgeGroup', 'Spending Score (1-100)')
        self.output.showChart(self.entity.df, 'AgeGroup', 'Spending Score (1-100)', kind='line')
