from Pages import PageFactory, DriverFactory
from Pages.DriverFactory import WebdriverFactory

def lienru(browser, sauce_flag, browser_version, platform):

    #datos para la creación y login en la pagina
    username = "123456789"
    password = "123456789"
    documento = "123456789"
    telefono = "123456789"
    correo = "123456789"

    #inicialización de la pagina web
    driver_obj = WebdriverFactory("chrome")
    driver = driver_obj.get_web_driver(browser, sauce_flag, browser_version, platform)
    driver.maximize_window()

    # Inicia el proceso en la pagina de registro
    registro_obj = PageFactory.get_page_object("registro", driver)
    if registro_obj.registro(username, password, documento, telefono, correo):
        msg = "Registro Satisfactorio"
        registro_obj.write(msg)
    else:
        msg = "Registro Falló"
        registro_obj.write(msg)

    login_obj = PageFactory.get_page_object("login", driver)
    if login_obj.login(documento, password):
        msg = "Login Satisfactorio"
        login_obj.write(msg)
    else:
        msg = "Login Falló"
        login_obj.write(msg)