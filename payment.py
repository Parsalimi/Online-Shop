class Payment():
    def __init__(self, payment_id,amount,status,type):
        self.payment_id = payment_id
        self.amount = amount
        self.status = status
        self.type = type

    @classmethod
    def create_new_payment(cls,amount):
        payment_id = cls.getId()
        status = 'Done'
        type = 'Online-Payment'
        selectedPayment = cls(payment_id, amount, status, type)
        with open("DB\\payment_db\\payment.txt", "a") as file:
            file.write(f'{selectedPayment.__dict__}\n')

        cls.update_last_payment_id(payment_id)

        return payment_id # return id of created payment
    
    @staticmethod
    def getId():
        with open("DB\\payment_db\\id_last_pay_created.txt","r") as file:
            last_payment_id = file.read()
            if last_payment_id != "":
                last_payment_id = int(last_payment_id) + 1
                return last_payment_id
            else:
                return 1
            
    def update_last_payment_id(new_payment_id):
        with open("DB\\payment_db\\id_last_pay_created.txt","w") as file:
            file.write(str(new_payment_id))