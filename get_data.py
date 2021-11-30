# ------------------------------------------------------------------------------
# Imports
import robin_stocks.robinhood as robin
import credentials

# ------------------------------------------------------------------------------
# Setup

def GetRobinHoodTotal(test):
    login = robin.login(credentials.RH_Login, credentials.RH_Pass, store_session=True)
    data = robin.load_phoenix_account()
# print(data)
# ------------------------------------------------------------------------------
# Printing

    final_data = data["portfolio_equity"]["amount"]
    return ("Total Data : ", final_data)
