def isValidLength(time):
    return len(time) == 4 or len(time) == 5

def colonInProperPosition(time):
    return len(time) == 4 and time.find(':') == 1 or len(time) == 5 and time.find(':') == 2

def hourProper(time):
    hourPos = time.find(':')
    hour = time[:hourPos]
    return hour.isdigit() and int(hour) in range(0, 24)

def minuteProper(time):
    minutePos = time.find(':')
    minute = time[minutePos + 1:]
    return minute.isdigit() and int(minute) in range(0, 60)

def timeIsValid(time):
    return isValidLength(time) and colonInProperPosition(time) and hourProper(time) and minuteProper(time)

def choice():
    print("if you want to contine, please input 1, if not please input 0:")
    choose = input()
    if choose == '0':
        return False
    elif choose == '1':
        return True
    else:
        print("choose is not valid, choice again")
        choice()

def main():
    while True:
        print("Please input time following the format 'hour:minute':")
        time = input()
        if timeIsValid(time):
            print("The time is Valid")
        else:
            print("The time is Not Valid")

        if not choice():
            return

if __name__ == '__main__':
    main()