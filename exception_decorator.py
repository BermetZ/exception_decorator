def exception(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if self.username is None:
            raise Exception('no username defined')
        elif self.password is None:
            raise Exception('no password given')
    return wrapper


class User():
    def __init__(self):
        self.username = None
        self.password = None

    @exception
    def get_account_balance(self):
        return self.username

    @exception
    def change_password(self):
        return self.password

u = User()
u.get_account_balance()
u.change_password()