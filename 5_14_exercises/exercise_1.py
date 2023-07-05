# /usr/bin/env python3


# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a function which is given the day number, and it returns the day name (a string).

def get_weekday(n):
    """ Returns the day of the week corresponding to n """

    weekdays = {0: 'Sunday',
                1: 'Monday',
                2: 'Tuesday',
                3: 'Wednesday',
                4: 'Thursday',
                5: 'Friday',
                6: 'Saturday'}

    if n < 0 or n > 6:
        return

    return weekdays.get(n)


if __name__ == '__main__':

    user_input = input("Enter the number of the weekday: ")
    error_message = "Please enter a positive number between 0 and 6 including!"

    if not user_input.isdigit():
        print(error_message)
        exit(1)

    day = int(user_input)

    if day < 0 or day > 6:
        print(error_message)
        exit(2)

    print(get_weekday(day))
