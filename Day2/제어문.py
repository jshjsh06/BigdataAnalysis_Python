class BMI :
    def __init__(self, height, weight):
        self.cal(height, weight)
        return

    def cal(self,height,weight):
        self.height = height
        self.weight = weight
        self.weightpow = weight**2
        self.bmi = self.height / self.weightpow

        return self.bmi

    def printbmi(self):
        print("안녕하세요")
        print("몸무게는 {0}kg, 키는 {1}cm, bmi지수는 {2} 입니다.".format(self.weight, self.height, self.bmi))

class BMI_Table :
    count = 0
    TOTAL_RANGE = 5

    def __init__(self):
        self.bmitable = []

        return

    def recordBMI(self, BMI):
        print(len(self.bmitable))
        self.bmitable.append(BMI)
        print(len(self.bmitable))
        return

    def printBMI(self):
        for bmi in self.bmitable:
            print(bmi)
            bmi.printbmi()
        return


class BMI_View :
    def __init__(self):
        self.bmi_table = BMI_Table()
        return

    def getInformation(self):
        height = float(input("키를 입력해주세요"))
        weight = float(input("몸무게를 입력해주세요"))
        bmi = BMI(height, weight)
        self.bmi_table.recordBMI(bmi)
        self.bmi_table.printBMI()
        return

if __name__ == "__main__" :
    bmi_table = BMI_Table()
    bmi_view = BMI_View()
    bmi_view.getInformation()
    # bmi_table.printBMI()

