import requests

def client():
    token_h = 'Token aa3c02dcc25f7129f581a0af59783c8b4dcdb36f'
    # The above is how you define a proper authorization header in Django
    # Rest Framework using a token. The key needs 'Token ' in front of it.

    headers = {'Authorization': token_h}

    #credentials = {'username': 'admin', 'password': 'password123'}
    # data = {
    #     "username": "resttestuser",
    #     "email": "test@test.com",
    #     "password1": "changeme123",
    #     "password2": "changeme123"
    #     }
    # The reason for password2 is because it's the confirmation password.

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
    #                          data=data)

    response = requests.get('http://127.0.0.1:8000/api/profiles/',
                             headers=headers)



    print ('Status Code:', response.status_code)
    response_data = response.json()
    print (response_data)


if __name__ == '__main__':
    client()