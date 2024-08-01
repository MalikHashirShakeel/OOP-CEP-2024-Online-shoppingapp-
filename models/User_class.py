class User:
    ID = 0
    def __init__(self, first_name, last_name, username, email, password, phone_number):
        User.ID += 1
        self.user_id = User.ID
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password
        self.__phone_number = phone_number

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_email(self):
        return self.__email
    
    def reset_password(self, new_password):
        try:
            pw = input("\nEnter your current password: ")
            assert pw == self.__password
        except AssertionError:
            print("\nIncorrect password!!....")
        else:
            self.__password = new_password
            print("\nPassword changed successfully!!")
        
    def __str__(self):
        return (
                    "---------------------------------\n"
                    "|         User Details          |\n"
                    "---------------------------------\n"
                    f"| ID         | {self.user_id:<20} |\n"
                    "---------------------------------\n"
                    f"| First Name | {self.__first_name:<20} |\n"
                    "---------------------------------\n"
                    f"| Last Name  | {self.__last_name:<20} |\n"
                    "---------------------------------\n"
                    f"| Username   | {self.__username:<20} |\n"
                    "---------------------------------\n"
                    f"| Email      | {self.__email:<20} |\n"
                    "---------------------------------\n"
                    f"| Phone      | {self.__phone_number:<20} |\n"
                    "---------------------------------\n"

        )


    @staticmethod
    def from_str(user_str):
        first_name, last_name, username, email, password, phone_number = user_str.split(',')
        return User(first_name, last_name, username, email, password, phone_number)
    


class Admin(User):
    def __init__(self, username, password, privilege_level=0):
        self.username = username
        self.password = password
        self.privilege_level = privilege_level
        
    def get_username(self):
        return super().get_username()
    
    def get_password(self):
        return super().get_password()
    
    def privileges(self):
        return self.privilege_level
