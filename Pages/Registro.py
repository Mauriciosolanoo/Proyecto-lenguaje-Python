from Pages.Page import Page

class Registro_Page(Page):
    "Page object for the Login page"

    def start(self):
        self.url = "registro"
        self.open(self.url)

        "Xpath of all the field"
        # Registro
        self.registro_nombre = "//*[@id='mat-input-4']"
        self.registro_documento = "//*[@id='mat-input-5']"
        self.registro_telefono = "//*[@id='mat-input-6']"
        self.registro_correo = "//*[@id='mat-input-7']"
        self.registro_password = "//*[@id='mat-input-8']"
        self.registro_terminos = "/html/body/app-root/app-auth-register/div/div[2]/div/div/div[1]/div/form/div[2]/div/app-checkbox[1]/div/div/div]"
        self.registro_tratamientoDatos = "/html/body/app-root/app-auth-register/div/div[2]/div/div/div[1]/div/form/div[2]/div/app-checkbox[2]/div/div"
        self.btn_registro = "/html/body/app-root/app-auth-register/div/div[2]/div/div/div[1]/div/form/div[3]/button"
        self.screenShot()

    def registro(self, username, password, documento, telefono, correo):
        "Login using credentials provided"
        self.set_registro_nombre(username)
        self.set_registro_documento(documento)
        self.set_registro_telefono(telefono)
        self.set_registro_correo(correo)
        self.set_registro_password(password)

    def set_registro_nombre(self, username):
        "Set the username on the login screen"

    def set_registro_documento(self, documento):
        "Set the username on the login screen"

    def set_registro_telefono(self, telefono):
        "Set the username on the login screen"

    def set_registro_correo(self, correo):
        "Set the username on the login screen"

    def set_registro_password(self, password):
        "Set the username on the login screen"

    def registro_terminos(self):
        "Selecciona aceptar terminos y condiciones"

    def registro_tratamientoDatos(self):
         "Selecciona aceptar tratamiento de datos"

    def btn_registro(self):
        "Envia el formulario"

    def screenShot(self, driver):
        driver.save_screenshot("Registro.png")