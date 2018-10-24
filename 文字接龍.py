number_fail=0
print("五次失敗就會退出遊戲")
strNewStr = input("請輸入一個字串")
strSumStr = strNewStr
print("上一個字串是 "+strSumStr)
strNewStr = input("請輸入-"+strSumStr[-1]+"-開始的字串")
while True:
    if strNewStr[0] == strSumStr[-1]:
        strSumStr = strSumStr+"-"+strNewStr
        print("上一個字串是 " + strSumStr)
        strNewStr = input("請輸入-" + strSumStr[-1] + "-開始的字串")
    else:
        number_fail += 1
        if number_fail>=5:
            break
        strNewStr = input("輸入錯誤，請輸入-" + strSumStr[-1] + "-開始的字串")
print("錯超過5次")