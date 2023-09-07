import shelve

class Customer:
    # count_id = 0
    def __init__(self, first_name, last_name, email, phone_number, subject, questions):
        # Customer.count_id += 1
        self.__customer_id = self.get_next_customer_id()
        # self.__customer_id = Customer.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__subject = subject
        self.__questions = questions
        self.__status = "pending"

    def reset_customer_id(self):
        db = shelve.open('customer_data.db', writeback=True)
        db['last_customer_id'] = 0
        db.close()


    def get_next_customer_id(self):
        db = shelve.open('customer_data.db')
        if 'last_customer_id' not in db:
            db['last_customer_id'] = 0
        last_customer_id = db['last_customer_id']

        # Reset customer_id to 0 if the database is empty
        if not db.keys():
            next_customer_id = 0
        else:
            next_customer_id = last_customer_id + 1

        db['last_customer_id'] = next_customer_id
        db.close()
        return next_customer_id

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_subject(self):
        return self.__subject

    def get_questions(self):
        return self.__questions

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_subject(self, subject):
        self.__subject = subject

    def set_questions(self, questions):
        self.__questions = questions

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


