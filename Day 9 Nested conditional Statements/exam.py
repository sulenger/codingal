medical = input("medical cause? (Y/N):      ")
if medical=="Y":
    print("allowed")
else:
    attendance = int(input("attendance percantage:      "))
    if attendance >= 75:
        print("allowed")
    else:
        print("not allowed")
