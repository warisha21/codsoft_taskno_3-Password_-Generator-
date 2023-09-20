# User input for desired length of password
lenght_of_pswd = int(input( print(f"Enter number of digits in Password ")))

# Import Random
import random as  rd

# Generate Password randomly
def password(lenght_of_pswd):
     # Defining the list of choices of characters.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    # Initializing an empty string to store the password.
    password = ""

    for i in range(lenght_of_pswd):
        # randomly selecting one character and appending it to the resultant password string
        password += rd.choice(characters)

    return password


# Display Password
print (f" Your randomly generated Password is {password(lenght_of_pswd)}")
