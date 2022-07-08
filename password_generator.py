from operator import length_hint
import random  


lower_case= "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPRQSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/"

Use_for= lower_case+upper_case+symbols+numbers
length_for_pass = 10

password = "".join(random.sample(Use_for, length_for_pass))

print(password)



