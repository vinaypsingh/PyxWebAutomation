import requests


# install requests module to use/make a http methods

def Get_info_users():
    # GET request - URL
    response_body = requests.get("https://reqres.in/api/users/2")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if response_body.status_code == 200:
        print("TC#1 - GET requesst is successful")
    else:
        print("TC#1 - GET requesst is not successful")

Get_info_users()