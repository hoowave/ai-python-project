import re

############### Domain ###############
# 요구사항 2,3 - IP 주소 추출 및 빈도 계산
class FileInfo:
    def __init__(self, fileName, extension, hash, content):
        self._fileName = fileName
        self._extension = extension
        self._hash = hash

        # 정규식 패턴
        self._commentPattern = re.compile(r'(#.*$|//.*$|/\*.*?\*/)', re.MULTILINE | re.DOTALL)
        self._emailPattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        self._sqlPattern = re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE)\b', re.IGNORECASE)

        # 검사 결과 저장
        self._hasPy = self._extension == '.py'
        self._hasJs = self._extension == '.js'
        self._hasClass = self._extension == '.class'
        self._hasComment = bool(self._commentPattern.search(content))
        self._hasEmail = bool(self._emailPattern.search(content))
        self._hasSql = bool(self._sqlPattern.search(content))
        
        self._isCaution = self._hasPy or self._hasJs or self._hasClass
        self._isWarning = self._hasComment or self._hasEmail or self._hasSql

        # 어떤 항목이 탐지되었는지 기록
        self._cautionReasons = []
        if self._hasPy: self._cautionReasons.append('Python 파일')
        if self._hasJs: self._cautionReasons.append('JavaScript 파일')
        if self._hasClass: self._cautionReasons.append('Class 파일')

        # 사용자 알림을 위해서!!
        self._warningReasons = []
        if self._hasComment: self._warningReasons.append('주석 포함')
        if self._hasEmail: self._warningReasons.append('이메일 포함')
        if self._hasSql: self._warningReasons.append('SQL 문장 포함')

    
    def to_OX(value: bool) -> str:
        return "O" if value else "X"

    def __str__(self):
        status = []
        if self._isCaution:
            status.append(f"주의파일({', '.join(self._cautionReasons)})")
        if self._isWarning:
            status.append(f"민감정보탐지({', '.join(self._warningReasons)})")
        if not status:
            status.append("정상")

        return (
            f"{self._fileName}{self._extension} | 상태: {' / '.join(status)} "
        )
######################################