from User import User


class Admin(User):
    def __init__(self):
        super().__init__(123, "Admin", "admin@gmail.com", "Dhaka", "admin_account", 0)
        self.set_password("admin123")
