from datetime import date, datetime, timedelta
def get_current_datetime():
    current_datetime = datetime.now()
    print(current_datetime.today(),"today date")
    print(current_datetime.weekday(),"weekday")
    print(current_datetime.strftime("%d/%m/%Y %H:%M:%S"))
    # formatted datetime object with additional information
    print(current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    # display in 12 hours format
    print(current_datetime.strftime("%I:%M:%S %p"))
    print(f"Current date and time: {current_datetime}")
    return current_datetime

get_current_datetime()

# Add 3 weeks to a date
new_date = datetime.now() + timedelta(weeks=3)

def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

birthday = date(1971, 7, 21)
print(calculate_age(birthday)) 

''''
format codes: 
"%a"- short version of the day of the week (e.g., Wed)
"%A"- full name of the day of the week (e.g., Wednesday)
"%b"- short version of the month (e.g., Sep)
"%B"- full name of the month (e.g., September)

"%y"- two-digit year (e.g., 18,22,24,25)
"%Y"- four-digit year (e.g., 2018,2022,2024,2025)
"%d"- two-digit day of the month (e.g., 01,02,12,32)
"%H"- two-digit hour in 24-hour format (e.g., 00,01,12,13,23)
"%I"- two-digit hour in 12-hour format (e.g., 01,02,12,13,11)
"%m"- two-digit month (e.g., 01,02,11,12)
"%M"- two-digit minute (e.g., 00,01,59) 

"%p"- either AM or PM
"%S"- two-digit second (e.g., 00,01,59)
"%Z" - time zone abbreviation (e.g., EST, PST, MST)
"%z" - time zone offset from GMT (e.g., -0500, +0530, -0400)

'''