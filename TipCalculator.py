print("Welcome to the tip calculator")
totalBill = input("What was the total bill? \n$")
tipPercent = input("What percentage tip would you like to give? 10, 12, or 15? \n")
waysSplit = input("How many people should split the bill?\n")

tip = float(totalBill) * (int(tipPercent) / 100)
afterTip = float(totalBill) + tip
afterSplit = round(afterTip / float(waysSplit), 2)
afterSplitFormat = "{:.2f}".format(afterSplit)
print(f"Each person should pay: {afterSplitFormat}")