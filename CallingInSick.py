
from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = None

if actually_sick == True and sick_days > 0:
    calling_in_sick = True
    print("You calling")
elif kinda_sick == True and hate_your_job == True and sick_days > 0:
    calling_in_sick = True
    print("You calling")
else:
    calling_in_sick = False
    print("You not calling")

