"""This utilizes a python library that should help with using our APIs.
"""
import os
from dotenv import load_dotenv
from pprint import pprint

# This import was something I created, you can install this via `pip install mctc_hackathon_robot297`
from hackathon_helper.api.money_movement import MoneyMovement
from hackathon_helper.api.core_banking import CoreBanking


def money_movement():
    load_dotenv()  # if you have a .env file in your project, it'll load values in memory

    money_movement = MoneyMovement(
        api_key=os.getenv('api_key'),  # after loading your env variables, you can os.getenv the values
        api_secret=os.getenv('api_secret')  # to know the values, look in the `.env` file or `.env-template` file
    )

    payload = {  # sample payload to send to the library
        "accountID": "00000",
        "amount": 10,
        "checkNumber": "",
        "party": "Test"
    }

    response = money_movement.deposit_money(payload)  # this method will call api and will return the entire response

    print(response.status_code)
    pprint(response.json())


def core_banking():
    load_dotenv()  # if you have a .env file in your project, it'll load values in memory

    core_banking = CoreBanking(
        api_key=os.getenv('api_key'),  # after loading your env variables, you can os.getenv the values
        api_secret=os.getenv('api_secret')  # to know the values, look in the `.env` file or `.env-template` file
    )

    customer_id = '00000'

    response = core_banking.find_customer(customer_id)  # this method will call api and will return the entire response

    print(response.status_code)
    pprint(response.json())


if __name__ == '__main__':
    money_movement()
    core_banking()
