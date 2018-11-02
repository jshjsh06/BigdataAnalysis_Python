from datetime import datetime

class dateView :
    today = datetime.now()
    tmp = []

    def __init__(self):
        self.input()

    def input(self):
        print("기념일 계산 프로그램에 오신 것을 환영합니다!")
        self.mDayInput = input("기념일을 입력해주세요(yyyy-mm-dd) : ")
        self.mem_day = input("기념일명을 입력해주세요(ex. \"태어난 날\") : ")

        self.mDaySplit = self.mDayInput.split("-")
        self.year = self.mDaySplit[0]
        self.month = self.mDaySplit[1]
        self.day = self.mDaySplit[2]

        self.mDay = datetime(int(self.year), int(self.month), int(self.day))
        self.elapsed = self.today - self.mDay
        self.elapsedDay = self.elapsed.days

        self.print()

    def print(self):
        self.strElapsedDay = str(self.elapsedDay)
        for i in range(len(self.strElapsedDay)) :
            self.tmp.append(self.strElapsedDay[i])

        self.flag = len(self.tmp)
        if len(self.tmp) >= 4 :
            self.tmp.insert(self.flag-3, ",")

        self.finalElapsedDay = ""
        for k in range(len(self.tmp)) :
            self.finalElapsedDay += self.tmp[k]

        print("오늘은 \"{0}\"로부터 연 수는 {1:.0f}년, 달 수는 {2:.0f}개월, 일 수는 {3}일이 경과되었습니다!".format(self.mem_day, self.elapsedDay / 365, self.elapsedDay / 30, self.finalElapsedDay))

if __name__ == "__main__" :
    dateview = dateView()
