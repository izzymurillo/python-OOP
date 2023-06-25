# Assignment: User

# For this assignment you will create the user class and add a couple methods!
# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:
# first_name
# last_name
# email
# age
# Also include default attributes:
# is_rewards_member - default value of False
# gold_card_points = 0

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self): # QUESTION: IS THERE AN EASIER WAY TO DO THIS????***************
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enough points.")
            return
        self.gold_card_points = self.gold_card_points - amount

user_izzy = User("Izzy", "Murillo", "myemail@gmail.com", 26)

print(user_izzy.last_name)

user_izzy.display_info()

user_izzy.enroll()
print(user_izzy.gold_card_points)
print(user_izzy.is_rewards_member)

user_izzy.enroll() # User already a member

user_izzy.spend_points(50)
user_izzy.display_info()

user_mike = User("Mike", "Tyson", "impregnable@gmail.com", 52)
user_manny = User("Manny", "Pacquiao", "pacman@gmail.com", 44)

user_mike.display_info()
user_manny.display_info()

user_mike.enroll()
user_mike.display_info()

user_mike.spend_points(80)
user_mike.display_info()

user_mike.spend_points(200)



#QUESTION: WHERE IS THE 0 COMING FROM???***********
