#!/usr/bin/env python3 

from exercise_1 import get_weekday

# You are leaving on day number 3 (a Wednesday), and return home after 137 sleeps. 
# Write a general version of the program which asks for the starting day number, 
# and the length of your stay, and it will tell you the name of day of the week you will return on.

start_day = 3 
days_away = 137 
return_day = (start_day + days_away) % 7

start_weekday = get_weekday(start_day)
return_weekday = get_weekday(return_day)

print(f"You left on {start_weekday}, and stayed away for {days_away} day(s). You return on {return_weekday}.")
