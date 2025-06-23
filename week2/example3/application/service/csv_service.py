import pandas as pd

from env import Env
from application.dto.csv_data_dto import CsvDataDto

############### CsvService ###############
# CSV 로딩 클래스
class CsvService:
    def __init__(self):
        self.env = Env()
        self.csvData = pd.read_csv(self.env.dataPath + self.env.dataName, encoding='cp949', low_memory=False)

    def getCsvDataDto(self):
        return CsvDataDto(self.csvData)