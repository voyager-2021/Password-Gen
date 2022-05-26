import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nuber = "0123456789"
symbols = "@#$%&*/\?!€;:()-_=+[]{}.,'"

Use_For = lower_case + upper_case + nuber + symbols
length_for_pass = 8

password ="".join(random.sample(Use_For, length_for_pass))

print("You Generated Password is :" + password)
