import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

from application.service.csv_service import CsvService

############### PltService ###############
# 데이터 처리 클래스
class PltService:
    # 생성자
    def __init__(self):
        self.csvService = CsvService()
        dto = self.csvService.getCsvDataDto()
        self.entity = dto.toEntity()
    
    # 1. 데이터 전처리
    def step1(self):
        data = self.entity.df[['Annual Income (k$)', 'Spending Score (1-100)']]
        self.scaler = StandardScaler()
        self.scaled_data = self.scaler.fit_transform(data)

    # 2. 학습/테스트 분리
    def step2(self):
        self.X_train, self.X_test = train_test_split(self.scaled_data, test_size=0.2, random_state=42)

    # 3. 최적 K 결정 및 시각화
    def step3(self):
        inertias = []
        k_range = range(2, 11)
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(self.X_train)
            inertias.append(kmeans.inertia_)

        plt.figure(figsize=(8, 5))
        plt.plot(k_range, inertias, 'o-')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Inertia')
        plt.title('Elbow Method')
        plt.show()

    # 4. 최적 K 선택 후 KMeans 학습
    def step4(self, optimal_k=5):
        print(f"KMeans 학습(k = {optimal_k})")
        self.kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
        self.kmeans.fit(self.X_train)
        self.train_labels = self.kmeans.labels_
        self.test_labels = self.kmeans.predict(self.X_test)

    # 5. 모델 평가
    def step5(self):
        silhouette = silhouette_score(self.X_train, self.train_labels)
        print(f"Silhouette Score (Train): {silhouette:.4f}")

    # 6. 학습 데이터 결과 시각화
    def step6(self):
        print("학습 데이터 클러스터 시각화")
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X_train[:, 0], self.X_train[:, 1], c=self.train_labels, cmap='viridis', s=30)
        plt.scatter(self.kmeans.cluster_centers_[:, 0], self.kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centers')
        plt.title('KMeans Clustering (Train)')
        plt.xlabel('Annual Income (scaled)')
        plt.ylabel('Spending Score (scaled)')
        plt.legend()
        plt.show()

    # 7. 테스트 데이터 결과 시각화
    def step7(self):
        print("테스트 데이터 클러스터 시각화")
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X_test[:, 0], self.X_test[:, 1], c=self.test_labels, cmap='viridis', s=30)
        plt.scatter(self.kmeans.cluster_centers_[:, 0], self.kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centers')
        plt.title('KMeans Clustering (Test)')
        plt.xlabel('Annual Income (scaled)')
        plt.ylabel('Spending Score (scaled)')
        plt.legend()
        plt.show()

    # 8. 클러스터 특징 분석
    def step8(self):
        print("각 클러스터 특징 요약")
        train_df = pd.DataFrame(self.scaler.inverse_transform(self.X_train), columns=['Annual Income', 'Spending Score'])
        train_df['Cluster'] = self.train_labels
        cluster_summary = train_df.groupby('Cluster').mean()
        print(cluster_summary)