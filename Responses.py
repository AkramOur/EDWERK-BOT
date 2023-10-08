from datetime import datetime
import SeleniumScriptIp as sp


def simple_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hey, How can i help u"

    return "I dont understand u"

def addressIp_command():
    return sp.getIpAddress()