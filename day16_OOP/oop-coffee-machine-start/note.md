# 該注意的點
我在 main.py犯了一個錯誤

我應該像在solution.py中ㄧ樣

一開始就先呼叫：

* money_machine = MoneyMachine()
* coffee_maker = CoffeeMaker()
* menu = Menu()

而不是在while迴圈中，一再的呼叫MoneyMachine()...這樣子每
次的呼叫都是初始化它，並無助於程式class的記錄功能（我認為是如此）
