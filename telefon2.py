import phonenumbers

number = input("Please enter the phone number e.g. +491523777702: ")


phone_number = phonenumbers.parse(number)
valid = phonenumbers.is_valid_number(phone_number)
possible = phonenumbers.is_possible_number(phone_number)

print("If | TRUE | that's a yes if | FALSE | a no")
print("Is the number assigned:", valid)
print("Can you assign the number:", possible)
