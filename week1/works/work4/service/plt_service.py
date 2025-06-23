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
        # 날짜에서 월 단위로 그룹화하여 월별 총 매출 계산
        monthly_sales = self.df.groupby(self.df['Date'].dt.month)['Sales'].sum()
        plt.rc('font', family=self.font)              # matplotlib에 한글 폰트 적용
        plt.figure(figsize=(10, 6))                   # 그래프 크기 설정
        plt.plot(monthly_sales.index,                 # 핵심!! 꺾은선 그래프 그리기
                 monthly_sales.values,
                 marker='o',
                 linestyle='-',
                 color='blue',
                 label='월별 총매출')
        plt.xticks(monthly_sales.index)             # x축 눈금 설정 (1~12월)
        plt.xlabel('월')                            # X축 레이블 설정
        plt.ylabel('총 매출 (원)')                   # Y축 레이블 설정
        plt.title('2024년 월별 총매출')               # 축 제목 설정
        plt.grid(True, linestyle='--', alpha=0.5)   # 그리드 추가 (보조선)
        plt.legend()                                # 범례 추가
        plt.show()                                  # 그래프 출력