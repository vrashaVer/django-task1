import django_setup
from task1.models import Role,User


# Створення і збереження ролей

# admin_role = Role.objects.create(name=Role.ADMIN)
# user_role = Role.objects.create(name=Role.USER)




# Створення нових користувачів та присвоєння ролі

role_user = Role.objects.get(id=2)
role_admin = Role.objects.get(id=1)

# user1 = User(name="User1",
#              email = "example1@gmail.com",
#              role = role_admin)
# user2 =User(name="User2",
#              email = "example2@gmail.com",
#              role = role_user)
# user3 = User(name="User3",
#              email = "example3@gmail.com",
#              role = role_user)

# user1.save()
# user2.save()
# user3.save()


# Зміна ролі


# user_test1 = User.objects.get(id=2)
# user_test1.role = role_admin
# user_test1.save()



