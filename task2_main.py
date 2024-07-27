import django_setup
from task2.models import User,Status,Task

# Створення статусів та користувачів 

# Status.objects.create(name=Status.IN_RPOCESS)
# Status.objects.create(name=Status.DONE)
# Status.objects.create(name=Status.DUSTED)

# User(name='User1').save()
# User(name='User2').save()
# User(name='User3').save()
# User(name='User4').save()

# Отримання користувачів та статусів
status_in_process = Status.objects.get(id=1)
status_done = Status.objects.get(id=2)
status_dusted = Status.objects.get(id=3)

user1 = User.objects.get(id=1)
user2 = User.objects.get(id=2)
user3 = User.objects.get(id=3)
user4 = User.objects.get(id=4)


# Створення Завдань

# Task(name='Task1',
#      description = " ",
#      status = status_in_process,
#      user = user3).save()

# Task(name='Task2',
#      description = " ",
#      status = status_done,
#      user = user2).save()

# Task(name='Task3',
#      description = " ",
#      status = status_dusted,
#      user = user1).save()

# Task(name='Task4',
#      description = " ",
#      status = status_in_process,
#      user = user4).save()

# Зміна статуса з "В процесі" на "Виконаний"

change_status_of_task = Task.objects.get(id = 4)
change_status_of_task.status = status_done
# change_status_of_task.save()

# Призначення 2 завдання 3 користувачу

change_user_of_task = Task.objects.get(id=2)
change_user_of_task.user = user3
# change_user_of_task.save()


# Зміна опису 1 завдання

change_description_of_task = Task.objects.get(id=1)
change_description_of_task.description = "First text"
# change_description_of_task.save()
start_description = change_description_of_task.description
change_description_of_task.description = start_description+" Second text"
# change_description_of_task.save()










