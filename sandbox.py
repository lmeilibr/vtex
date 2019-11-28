from vtex import Vtex
import os

account_name = os.getenv("ACCOUNTNAME")


client = Vtex(account_name, environment, app_key, app_token)
