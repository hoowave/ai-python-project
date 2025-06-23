import pandas as pd

############### Customer ###############
# Customer 도메인 클래스 (Data Frame)
class Customer:
    # 생성자
    def __init__(self, csvDataDto):
        self.df = pd.DataFrame(csvDataDto)
        print(self.df.describe())