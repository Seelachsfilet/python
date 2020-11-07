import phonenumbers
from phonenumbers import geocoder, carrier

nummer = input("Please enter the phone number e.g. +491523777702: ")

phoneNumber = phonenumbers.parse(nummer)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')
print(f"| Country | Contract |\n|-----------------------|\n| {Region}  |  {Carrier}")
