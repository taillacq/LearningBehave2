# encoding: UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Actionwords:
    def __init__(self):
        self._driver = webdriver.Chrome()



    def g_open_browser(self, element_label, url):
        # TODO: Implement action: "%s est ouvert à l'adresse : %s" % (element_label, url)
            self._driver.get(url)
            self._driver.find_element_by_id("username").clear()
            self._driver.find_element_by_id("password").clear()


    def w_insert_element(self, element_type, wrt_additional_informations):
        # TODO: Implement action: "Insérer %s %s" % (element_type, wrt_additional_informations)
        if element_type == "etaillacq":
            self._driver.find_element_by_id("username").send_keys(element_type)
        else:
            self._driver.find_element_by_id("password").send_keys(element_type)


    def w_click_on_element(self, element_label = "", wrt_element_type = ""):
        # TODO: Implement action: "Cliquer sur %s %s" % (wrt_element_type, element_label)
        self._driver.find_element_by_id("kc-login").send_keys(Keys.RETURN)



    def t_open_session(self, element_value, wrt_additional_informations = ""):
        # TODO: Implement result: "La demande de connexion est %s" % (element_value)
        # TODO: Implement result: "%s" % (wrt_additional_informations)
        assert element_value == self._driver.find_element_by_id("sidebarProfileName").text
