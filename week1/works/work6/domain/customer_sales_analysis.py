############### Domain ###############
# CustomerSalesAnalysis 도메인 클래스
class CustomerSalesAnalysis:
    # 생성자
    def __init__(self, name, purchDate, prodName, amount, price):
        self.name = name                    # 고객명
        self.purchDate = purchDate          # 구매일자
        self.prodName = prodName            # 상품명
        self.amount = amount                # 수량
        self.price = price                  # 단가
    
    # 컬럼 명을 한글로 사용하기 위해 딕셔너리 자료구조로 변환
    def to_dict(self):
        return {
            '고객명': self.name,
            '구매일자': self.purchDate,
            '상품명': self.prodName,
            '수량': self.amount,
            '단가': self.price,
        }
    
    # 테스트를 위한 메서드
    def __str__(self):
        return f"{self.purchDate.date()} | {self.name} | {self.prodName} | 수량: {self.amount}개 | 단가: {self.price:,}원"