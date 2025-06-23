import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

############### PltService ###############
# 시각화 클래스
class PltService:
    # 생성자
    def __init__(self, df):
        # 사용할 한글 폰트 경로 설정 (굴림체)
        self.fontPath = 'C:\\Windows\\Fonts\\gulim.ttc'
        # matplotlib에서 인식할 폰트 이름 추출
        self.font = fm.FontProperties(fname=self.fontPath).get_name()
        self.df = df

    # 시각화 실행 메서드
    def run(self):
        self.df['총매출'] = self.df['수량'] * self.df['단가']                   # 총매출 = 수량 * 단가
        self.df['구매월'] = self.df['구매일자'].dt.to_period('M').astype(str)   # 구매월 추출 (YYYY-MM 형태)
        monthly_sales = self.df.groupby('구매월')['총매출'].sum()               # 월별 총매출 집계

        plt.rc('font', family=self.font)                                      # 한글 폰트 설정
        # 막대그래프: 월별 총매출 시각화
        plt.figure(figsize=(10, 6))                                           # 그래프 크기 설정
        plt.bar(monthly_sales.index,                                          # 그래프 데이터 추가
                monthly_sales.values,
                color='skyblue')   
        plt.title('월별 총매출')                                                # 제목 설정
        plt.xlabel('구매월')                                                   # X축 레이블
        plt.ylabel('총매출(원)')                                               # Y축 레이블
        plt.xticks(rotation=45)                                               # X축 레이블 회전
        plt.grid(True, linestyle='--', alpha=0.5)                             # 그리드 추가
        plt.tight_layout()                                                    # 레이아웃 자동 조정
        plt.show()                                                            # 그래프 출력

        # 3. 고객별 누적 매출 파이 차트
        customer_sales = self.df.groupby('고객명')['총매출'].sum()

        plt.figure(figsize=(8, 8))                                            # 그래프 크기 설정
        plt.pie(customer_sales,                                               # 그래프 데이터 추가
                labels=customer_sales.index,                                  
                autopct='%1.1f%%',
                startangle=140)
        plt.title('고객별 누적 매출 비중')                                       # 제목 설정
        plt.tight_layout()                                                    # 레이아웃 자동 조정
        plt.show()                                                            # 그래프 출력