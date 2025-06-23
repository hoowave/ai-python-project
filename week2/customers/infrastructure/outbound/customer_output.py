import matplotlib.pyplot as plt
import seaborn as sns

from env import Env

############### CustomerOutput ###############
# 사용자 요청 출력 처리

class CustomerOutput:

    def __init__(self):
        self.env = Env()
    
    def showTable(self, df, groupby_cols, agg_col):
        result = df.groupby(groupby_cols)[agg_col].agg('mean').reset_index()
        print(result.to_string(index=False))

    # 시각화 실행 메서드
    def showChart(self, df, groupby_cols, agg_col, kind='bar'):
        plt.rcParams['font.family'] = self.env.fontFamily
        result = df.groupby(groupby_cols)[agg_col].mean().reset_index()

        plt.figure(figsize=(10, 6))

        if kind == 'bar':
            sns.barplot(x=groupby_cols, y=agg_col, data=result)
        elif kind == 'pie':
            plt.pie(result[agg_col], labels=result[groupby_cols], autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
        elif kind == 'line':
            sns.lineplot(x=groupby_cols, y=agg_col, data=result, marker='o')
        else:
            raise ValueError(f"지원하지 않는 그래프 종류입니다: {kind}")

        plt.title(f"{groupby_cols}별 {agg_col} 평균 ({kind})")
        plt.xlabel(groupby_cols)
        plt.ylabel(agg_col)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()