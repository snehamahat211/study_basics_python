import random
import my_module
random_integer=random.randint(1,20)
print(random_integer)
print(my_module.pi)

random_float=random.random()
print(random_float)  #random=0.000000 to 0.999999999
randomfloat1=random.random()*5 #multiplying by 5 to get upto 5
print(randomfloat1)

love_score=random.randint(65,100)
print(f"love_score is {love_score}")

