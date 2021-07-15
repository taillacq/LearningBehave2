from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fixtures import *
from steps.actionwords import Actionwords


def before_all(context):
    context.actionwords = Actionwords()

#def after_all(context):
    #Actionwords()._driver.close()


