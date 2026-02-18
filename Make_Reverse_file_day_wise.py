import os
from datetime import datetime, timedelta
from calendar import isleap,Day
import calendar

Current_date = input("Enter a CURRENT DATE : YYYY-MM-DD ")
file_list = [".txt",".html",".java",".js"]
def create_folders_between_dates(Current_date):
    Convert_date_DATETIME = datetime.strptime(Current_date, "%Y-%m-%d")
    Current_Day_Number = Convert_date_DATETIME.day
    print(Current_Day_Number)
    year = Convert_date_DATETIME.year # Get year correctly
    Current_month = Convert_date_DATETIME.month
    
    base_path = "C:/Users/hemanshu.marwadi/Desktop/OS_MAKE_DIR"  
    for month in range(Current_month,13):
        # Find_Remaining_Days = total_days - Current_Day_Number 
        total_days = calendar.monthrange(year,month)[1]

        for i in range(Current_Day_Number, total_days + 1):
            current_date_obj = datetime(year, month, i)
            s = current_date_obj.strftime("%Y-%m-%d")
            folder_path = os.path.join(base_path, s)
            os.makedirs(folder_path, exist_ok=True)
            
            Find_Current_day = current_date_obj.day
            find = total_days - Find_Current_day + 1
            Reverse_date = datetime(year,month,find)
            for ext in file_list:
                file_name = Reverse_date.strftime("%Y-%m-%d") + ext
                file_path = os.path.join(folder_path, file_name)
            
                with open(file_path, "w") as f:
                    f.write(f"Done {file_name}")

            
create_folders_between_dates(Current_date)




