from domain.customer import Customer

############### CsvDataDto ###############
# 계층 간 전달 DTO 클래스
class CsvDataDto:
    def __init__(self, csvData):
        self.csvData = csvData

    def toEntity(self):
        return Customer(self.csvData)