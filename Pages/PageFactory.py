from Pages.Registro import Registro_Page
from Pages.LoginPage import Login_Page

def get_page_object(page_name, driver, base_url='www.avanza.com/'):
    "Verifica con la url si debe realizar login o registro"
    test_obj = None
    page_name = page_name.lower()
    if page_name == "registro":
        test_obj = Registro_Page(driver, base_url=base_url)
    elif page_name == "login":
        test_obj = Login_Page(driver, base_url=base_url)

    return test_obj