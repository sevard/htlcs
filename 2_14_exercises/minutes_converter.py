#!/usr/bin/env python3

import time


# time_tuple = time.gmtime()
# print("GMT: ", time.asctime(time.gmtime()))
# print("EST: ", time.asctime(time.localtime()))

# print("GMT: ", time.strftime('%s', time.gmtime()))
# print("EST: ", time.strftime('%s', time.localtime()))

input_total_seconds = int(time.strftime('%s', time.gmtime()))
# total_seconds = 10800 + 1800 + 33


def convert_seconds(total_seconds):
    """ Convert given seconds into 
        Whole hours, minutes, and seconds """
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 3600) % 60
    return {'hours': hours, 'minutes': minutes, 'seconds': seconds}


print(convert_seconds(input_total_seconds))
print(convert_seconds(10800 + 1800 + 33))
print(convert_seconds(7200 + 3600 + 3))
if __name__ == '__main__':

    assert convert_seconds(
        10800 + 1800 + 33) == {'hours': 3, 'minutes': 30, 'seconds': 33}
    assert convert_seconds(
        7200 + 3600 + 3) == {'hours': 3, 'minutes': 0, 'seconds': 3}
