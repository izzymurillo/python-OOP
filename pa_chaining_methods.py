# Chaining Methods


class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return 
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enough points.")
            return self
        self.gold_card_points = self.gold_card_points - amount

user_izzy = User("Izzy", "Murillo", "myemail@gmail.com", 26)

print(user_izzy.last_name)

user_izzy.display_info()

user_izzy.enroll()
print(user_izzy.gold_card_points)
print(user_izzy.is_rewards_member)

user_izzy.enroll().spend_points(50).display_info() # User already a member
# user_izzy.spend_points(50)
# user_izzy.display_info()

user_mike = User("Mike", "Tyson", "impregnable@gmail.com", 52)
user_manny = User("Manny", "Pacquiao", "pacman@gmail.com", 44)

user_mike.display_info()
user_manny.display_info()

user_mike.enroll().display_info()
# user_mike.display_info()

user_mike.spend_points(80).display_info().spend_points(200)
# user_mike.display_info()
# user_mike.spend_points(200)



