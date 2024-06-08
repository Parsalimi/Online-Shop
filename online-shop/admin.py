from users import Users

class Admin(Users):
    def __init__(self, id, username, password, fname, lname, phone, isPhoneVerifyed, nationalId, dateOfBirth):
        super().__init__(id, username, password, fname, lname, phone, isPhoneVerifyed, nationalId, dateOfBirth)