import os
from datetime import datetime, timedelta
from calendar import isleap

Current_date = input("Enter a CURRENT DATE : YYYY-MM-DD ")

def create_folders_between_dates(Current_date):
    Convert_date_DATETIME = datetime.strptime(Current_date, "%Y-%m-%d")
    Current_Day_Number = Convert_date_DATETIME.timetuple().tm_yday
    year = Convert_date_DATETIME.year # Get year correctly
    total_days = 366 if isleap(year) else 365  # Check leap year properly
    
    Find_Remaining_Days = total_days - Current_Day_Number

    for i in range(1, Find_Remaining_Days + 1):
        Increase_Date = Convert_date_DATETIME + timedelta(days=i)
        s = Increase_Date.strftime("%Y-%m-%d")
        
        os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/2027_year_folder/{s}")
        

create_folders_between_dates(Current_date)