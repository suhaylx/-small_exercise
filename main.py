user_name = input("Please enter  your username ")
username_password = input("Please enter your password ")

len_of_password = len(username_password)
stars = '*' * len_of_password

print(f"{user_name}, your password {stars} is  {len_of_password} letter long")