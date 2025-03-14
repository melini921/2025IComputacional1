# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:07:39 2025

@author: Melissa Niño
"""

import calendar
from datetime import datetime

current_year = datetime.now().year

# Imprimir el calendario del año completo
print(calendar.calendar(current_year))

import calendar
from datetime import date, datetime

def colombian_holidays(year):
  """Returns a list of Colombian holidays for the given year."""
  holidays = [
      date(year, 1, 1),  # New Year's Day
      date(year, 1, 6),
      date(year, 3, 21),
      date(year, 4, 17),
      date(year, 4, 18),
      date(year, 5, 1),  # Labor Day
      date(year, 6, 2),
      date(year, 6, 23),
      date(year, 6, 30),
      date(year, 7, 20), # Independence Day
      date(year, 8, 7),  # Battle of Boyaca
      date(year, 8, 15), # Assumption of Mary
      date(year, 8, 18),
      date(year, 10, 12),# Columbus Day
      date(year, 11, 1), # All Saints' Day
      date(year, 11, 3), 
      date(year, 11, 11),# Independence of Cartagena
      date(year, 11, 17),
      date(year, 12, 8), # Immaculate Conception
      date(year, 12, 25) # Christmas Day
  ]
  return holidays

def print_calendar_with_holidays(year):
  cal = calendar.Calendar()
  for month in range(1, 13):
    print(calendar.month_name[month], year)
    for week in cal.monthdays2calendar(year, month):
      row = ""
      for day, weekday in week:
        if day == 0:
          row += "    "
          continue
        holiday_text = "*" if date(year, month, day) in colombian_holidays(year) else " "
        row += f"{day:2}{holiday_text} "
      print(row)
    print()

current_year = datetime.now().year
print_calendar_with_holidays(current_year)