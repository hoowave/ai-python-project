from application.service.plt_service import PltService

############### CustomerController ###############
# 사용자 요청 입력 처리

class CustomerController:
    # 생성자
    def __init__(self):
        self.pltService = PltService()
        self.menu = {
        '1': lambda: self.pltService.processEda1(),
        '2': lambda: self.pltService.processEda2(),
        '3': lambda: self.pltService.processEda3()
    }

    def handler(self):
        while True:
            print('\n1. 성별에 따른 평균 소비 점수  | 2. 연 소득 구간별 평균 소비 점수 | 3. 연령대별 평균 소비 점수 | 0. 종료')
            choice = input('선택: ')
            if choice == '0':
                print('프로그램을 종료합니다.')
                break
            action = self.menu.get(choice)
            if action:
                action()
            else:
                print('잘못된 선택입니다.')