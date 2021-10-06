# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)

weeks_in_90 = 90 * 52
days_in_90 = 365 * 90
months_in_90 = 90 * 12

weeks_in_age = age_int * 52
days_in_age = 365 * age_int
months_in_age = age_int * 12

days = days_in_90 - days_in_age
weeks = weeks_in_90 - weeks_in_age
months = months_in_90 - months_in_age

print("Your Life in Weeks\n")

print(f"You have {days} days, {weeks} weeks, {months} months left.")
