class member_login:
    count = 0
    def __init__(self, phonenumber, password):
        member_login.count +=1
        self.__id = member_login.count
        self.__phonenumber = phonenumber
        self.__password = password


    def get_count(self):
        return self.__id

    def get_phone_number(self):
        return self.__phonenumber

    def get_password(self):
        return self.__password

    def set_phone_number(self,phonenumber):
        self.__phonenumber = phonenumber

    def set_password(self,password):
        self.__password = password

    def set_count(self, count):
        self.__id = count
