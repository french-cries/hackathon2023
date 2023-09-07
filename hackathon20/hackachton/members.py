class member:
    count = 0

    def __init__(self, first_name, last_name, email, password):
        member.count += 1
        self.__user_id = member.count
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.todo_list = []

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_password(self):
        return self.__password



    def get_email(self):
        return self.__email



    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name =first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_password(self,password):
        self.__password =password

    def set_email(self, email):
        self.__email = email


    def add_item(self,item):
        self.todo_list.append(item)

    def add_todo_item(self, name, category,description):
        todo_item = ToDoItem(name, category,description)
        self.add_item(todo_item)

    def remove_todo_item(self, index):
        if 0 <= index < len(self.todo_list):
            self.todo_list.pop(index)

    def get_todo_list(self):
        return self.todo_list

    def complete_todo_item(self, index):
        if 0 <= index < len(self.todo_list):
            self.todo_list[index].mark_completed()

    def incomplete_todo_item(self, index):
        if 0 <= index < len(self.todo_list):
            self.todo_list[index].mark_incomplete()




class ToDoItem:
    def __init__(self, name, category,description):
        self.name = name
        self.category = category
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False


class Product:
    def __init__(self, product_name, product_price,product_quantity):
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_product_price(self, product_price):
        self.__product_price = product_price

    def set_product_quantity(self, product_quantity):
        self.__product_quantity = product_quantity


    def get_product_name(self):
        return self.__product_name

    def get_product_price(self):
        return self.__product_price

    def get_product_quantity(self):
        return self.__product_quantity