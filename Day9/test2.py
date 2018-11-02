class Lotto() :
    def __init__(self, count, numbers):
        self.count = count
        self.numbers = numbers
        self.numbers.sort()

    def LottoPrint(self):
        print("{}번째 로또 입력 값은 {}입니다. \n".format(self.count, self.numbers))

class lottoController() :
    lotto_List = []
    def __init__(self):

        return

    def record(self, count, numbers):
        lotto = Lotto(count, numbers)
        self.lotto_List.append(lotto)
        return

    def lottoControllerPrint(self):
        for lotto in self.lotto_List :
            lotto.LottoPrint()

class lottoView() :
    def __init__(self):
        self.lottocontroller = lottoController()
        self.input()
        return

    def input(self) :
        self.count = 1
        self.flag = input("로또를 주문하시려면 아무 키를 눌러주십시오(끝내시려면 \"end\"를 입력해주십시오) : ")
        while(self.count <= 10 and self.flag != 'end') :
            self.numbers = []
            for i in range(6) :
                self.lottoOrder = input("[{}]값을 입력해주세요 : ".format(i+1))
                self.numbers.append(int(self.lottoOrder))
            self.lottocontroller.record(self.count, self.numbers)
            self.count += 1
            self.flag = input("로또를 주문하시려면 아무 키를 눌러주십시오(끝내시려면 \"end\"를 입력해주십시오) : ")

        print("종료합니다. 로또값을 출력합니다.")

        self.lottocontroller.lottoControllerPrint()



if __name__ == "__main__" :
    lottoview = lottoView()