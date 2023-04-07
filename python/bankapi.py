"""Python examples to help better understand how to connect to APIs.
"""
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import requests
import os


def find_customer():
    # This is where you'll put your api key and secret to authenticate
    # If you're using GitHub, you do not want to commit these secrets to your project.
    basic_auth = HTTPBasicAuth("Key", "Secret")

    # You need these headers so that the API knows what format you're sending you're data and what you expect.
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Base URL to help build our calls.
    # This is specific to the core banking API service
    base_uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/'

    customer_id = 000000  # This is just filler.

    response = requests.get(
        url=base_uat_url + f'customer/{customer_id}',  # the end point
        auth=basic_auth,  # The authorization we did like above
        headers=headers,  # including the headers
        timeout=60  # Not needed but helpful if you have connectivity issues.
    )

    print(response.status_code)  # Good to know that you got a 2XX when interacting with the API
    pprint(response.json())  # This just dumps the payload out


def deposit_money():
    # This is where you'll put your api key and secret to authenticate
    # If you're using GitHub, you do not want to commit these secrets to your project.
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('api_secret'))

    # You need these headers so that the API knows what format you're sending you're data and what you expect.
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    payload = {
        "accountID": "00000",
        "amount": 10,
        "checkNumber": "",
        "party": "Test"
    }

    # Base URL to help build our calls.
    # This is specific to the core banking API service
    base_uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/'
    response = requests.post(
        url=base_uat_url + 'activity/deposit',  # the end point
        auth=basic_auth,  # The authorization we did like above
        headers=headers,  # including the headers
        json=payload,  # The payload to send to the service
        timeout=60  # Not needed but helpful if you have connectivity issues.
    )

    print(response.status_code)  # Good to know that you got a 2XX when interacting with the API
    pprint(response.json())  # This just dumps the payload out


if __name__ == "__main__":
    find_customer()
    deposit_money()
