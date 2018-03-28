import sys
if __name__ == "__main__":
    numberOfClock = int(sys.stdin.readline().strip())
    listOfTime = []
    for i in range(numberOfClock):
        line = sys.stdin.readline().strip()
        lines = line.split()
        listOfTime.append(int(lines[0]))
        listOfTime.append(int(lines[1]))
    needTime = int(sys.stdin.readline().strip())
    classTimetemp = sys.stdin.readline().strip().split()
    classTime = []
    classTime.append(int(classTimetemp[0]))
    classTime.append(int(classTimetemp[1]))
    list2 = []
    for j in range(numberOfClock):
        minite = listOfTime[2*j+1] + needTime
        hour = listOfTime[2*j]
        while minite >= 60:
            minite -= 60
            hour += 1
        if hour > classTime[0] or (hour == classTime[0] and minite > classTime[1]):
            list2.append(10000)
        else:
            if minite > classTime[1]:
                lastTime = classTime[1] + 60 - minite + (classTime[0] - 1 - hour) * 60
            else:
                lastTime = classTime[1] - minite + (classTime[0] - hour) * 60
            list2.append(lastTime)
    number = list2.index(min(list2))
    print(str(listOfTime[2*number]) + " " + str(listOfTime[2*number+1]))