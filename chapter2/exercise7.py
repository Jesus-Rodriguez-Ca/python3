"""You look at the clock and it is exactly 2pm. You set an alarm to go off in. You set an alarm to go off in 51 hours. 
At what time does the alarm go off? (Hint: you could count on your fingers, but this is not what we're after. If you are tempted
to count on your fingers, change the 51 to 5100)"""


def main():
    time = 2
    alarm = 51 % 24
    print((time  + alarm) % 12)
main()