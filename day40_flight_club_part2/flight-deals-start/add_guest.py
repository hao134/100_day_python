import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/9c3d8bbf95114f4832af9a29ce8aa9f0/myWorkouts/users"
user_input = True

while user_input:
    print("Welcome to Angela's Flight Club.")
    print("We find the best flight deals and email you")
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    email = input("What is your email?")
    check_email = input("Type your email ")
    if email == check_email:
        comfirmed_email = check_email
        sheet_inputs = {
            "user": {
                "firstName": first_name,
                "lastName": last_name.title(),
                "email": comfirmed_email,
            }
        }
        sheet_response = requests.post(
            SHEETY_USERS_ENDPOINT,
            json=sheet_inputs,
            # auth=(
            #     SHT_USER,
            #     SHT_PASSW,
            # )
        )

        print(sheet_response.text)
        user_input = False
    else:
        print("wrong email, please enter again.")