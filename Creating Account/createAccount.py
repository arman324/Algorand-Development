from algosdk import mnemonic, account
import json

private_key, public_address = account.generate_account()
FirstAccountAddress = public_address
print("First account address:")
print(FirstAccountAddress)
FirstMnemonic = mnemonic.from_private_key(private_key)

print("\nSecond account address:")
private_key, public_address = account.generate_account()
SecondAccountAddress = public_address
print(SecondAccountAddress)
SecondMnemonic = mnemonic.from_private_key(private_key)

print("\nThird account address:")
private_key, public_address = account.generate_account()
ThirdAccountAddress = public_address
print(ThirdAccountAddress)
ThirdMnemonic = mnemonic.from_private_key(private_key)

print("\n****Fund these accounts with the TestNet faucet****\n")

print("These are the mnemonics of your three accounts:")

print("First mnemonic = \"{}\"\n".format(FirstMnemonic))
print("Second mnemonic = \"{}\"\n".format(SecondMnemonic))
print("Third mnemonic = \"{}\"\n".format(ThirdMnemonic))
