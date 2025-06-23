############### Custom Exception ###############
# 에러 핸들링 - 부모
class ExceptionHandler(Exception):
    pass

# 에러 핸들링 - 다양한 에러 처리
class BaseException(ExceptionHandler):
    def __init__(self):
        super().__init__("프로그램 내부 에러! 관리자에게 문의주세요.")

# 에러 핸들링 - 학생 데이터가 없을 경우
class FileNotExistException(ExceptionHandler):
    def __init__(self):
        super().__init__("데이터 파일을 찾을 수 없습니다!")

# 에러 핸들링 - 학생 데이터 내부 점수가 잘못된 경우
class ScoreException(ExceptionHandler):
    def __init__(self):
        super().__init__("데이터 파일 내부 에러!\n 점수는 0~100점으로 사용해야 합니다.")

# 에러 핸들링 - 학생 데이터 내부 구조가 잘못된 경우
class ValueException(ExceptionHandler):
    def __init__(self):
        super().__init__("데이터 파일 내부 에러!\n 이름,점수 순으로 사용해야 합니다.")
##############################################