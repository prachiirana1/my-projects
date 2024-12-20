import time


def countdown_timer():
    try:
        countdown_time = int(input("Enter countdown time in seconds: "))
        print("\n your time starts now..!!  u can work until your time's up.. \n")
        while countdown_time > 0:
            mins, secs = divmod(countdown_time, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            countdown_time -= 1

        print("\n     Time's up!     \n")
        print("\n  !!..  stop doing..your time is over  ..!!  \n")
    except ValueError:
        print("Please enter a valid number.")


countdown_timer()
