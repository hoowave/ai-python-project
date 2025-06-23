import pandas as pd

############### Mall Customers ###############
# Mall 도메인 클래스 (Data Frame)
class Mall:
    # 생성자
    def __init__(self, csvDataDto):
        self.df = pd.DataFrame(csvDataDto)