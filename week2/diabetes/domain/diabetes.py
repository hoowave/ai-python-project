import pandas as pd

############### Diabetes ###############
# Diabetes 도메인 클래스 (Data Frame)
class Diabetes:
    # 생성자
    def __init__(self, csvDataDto):
        self.df = pd.DataFrame(csvDataDto)