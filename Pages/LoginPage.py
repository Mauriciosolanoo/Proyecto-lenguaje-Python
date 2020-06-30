from Pages.Page import Page

class Login_Page(Page):
    "Page object for the Login page"

    def start(self):
        self.url = "iniciar-sesion"
        self.open(self.url)

        "Xpath of all the field"
        # Login
        self.login_documento = "//*[@id='mat-input-9']"
        self.login_password = "//*[@id='mat-input-10']"

    def login(self, documento, password):
        "Login using credentials provided"
        self.set_login_documento(documento)
        self.set_login_password(password)
        self.submit_login()

    def set_login_documento(self, documento):
        "Set the username on the login screen"

    def set_login_password(self, password):
        "Set the password on the login screen"

    def submit_login(self):
        "Envia el inicio de sesion"

    def screenShot(self, driver):
        driver.save_screenshot("Login.png")