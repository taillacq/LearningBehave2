from behave import *
from actionwords import *
from actionwords import Actionwords

# This should be added to environment.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords()

use_step_matcher('re')


@given(r'G_open_browser "(.*)" "(.*)"')
def impl(context, element_label = "CloudFare", url = "https://auth-sop3.dev-open-payment.fr/auth/realms/sop3/protocol/openid-connect/auth?client_id=CloudFareWeb&redirect_uri=https%3A%2F%2Festatemanagement-sop3.dev-open-payment.fr%2Fsignin-oidc&response_type=code&scope=openid%20profile%20roles&code_challenge=_3V4u-ZB3EwZ7OG5-fjYefU_o22-jSmAw5dNkIwv7Q8&code_challenge_method=S256&response_mode=form_post&nonce=637616706782311375.Zjg2YWIxNzEtZGI5MC00Y2Q5LWEwMjctYmVjZDE4MmQ3ZGNiMWI4ZGM5ZWQtYTViZC00ZTA3LTlhNDUtZWE0ODBkNTVlMTA1&state=CfDJ8E-qlkOrg11LlKtujeNUprUbNiuZgZOGc8u8X3ac4AVH80LAGXdWaLC6o2b2gscoMpnCOkh1VzhcmIS5PDoGM9oFHEfVhIt7P52LY1jzzL2HiMk1X2stWgYjr3DyJHTbI34ogjipbxDGM7Yqvqd0fWfUBhQpzXmVZ0lXOTiRlZOqzwoEkBvwPziKrH46YxGgsKncFnTuiYbWofC4SIwUkbQa7oTqcqX728cjwHBYrYvPjE-MdYcELRsw4tmz6V05ksGA5tT_lVsRkldeE7T8Cq1eyaQu2lYkN19pWWuQFpNfSy-iM52fQifohD1YJFKuDa5senUQN5LjE36l79JuDLpiTIY92BAsTvCgoao8roJuBA0eLZIBWeaMYsmbU1dI1Q7V0tZkUFk6dgNcV1GqBOjDQ-STuL4XxXGvrfZXPtPw&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=5.5.0.0"):
    context.actionwords.g_open_browser(element_label, url)
    pass


@when(r'W_click_on_element "(.*)" "(.*)"')
def impl(context, element_label, wrt_element_type):
    context.actionwords.w_click_on_element(element_label, wrt_element_type)
    pass

@when(r'W_insert_element "(.*)" "(.*)"')
def impl(context, element_type, wrt_additional_informations):
    context.actionwords.w_insert_element(element_type, wrt_additional_informations)
    pass

@then(r'T_open_session "(.*)" "(.*)"')
def impl(context, session, wrt_additional_informations = ""):
    context.actionwords.t_open_session(session, wrt_additional_informations)
    pass





















































































































































































































































































































































































































