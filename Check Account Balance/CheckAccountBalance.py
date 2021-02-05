from algosdk.v2client import algod
import json

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
client = algod.AlgodClient(algod_token, algod_address)

public_key = input("Please enter your public key:\n")

account_info = client.account_info(public_key)
print('\nYour account information:\n')
print(json.dumps(account_info, indent=4))

account_balance = account_info.get('amount')
print('\nAccount balance: {} microAlgos'.format(account_balance))

