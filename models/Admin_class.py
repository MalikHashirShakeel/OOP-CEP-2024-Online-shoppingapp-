class Admin:

    def __init__(self,admin_name,admin_password):
        self.__name = admin_name
        self.__password = admin_password

    def __str__(self):
        return f"{self.__name},{self.__password}"
    
    def get_admin_name(self):
        return self.__name
    
    def get_admin_password(self):
        return self.__password
    
    @staticmethod
    def from_str(admin_str):
        username, password = admin_str.split(',')
        return Admin(username, password)