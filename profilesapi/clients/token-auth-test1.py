import requests

def client():
    token_h = 'Token cc1767ae86225538097389a9210cbdbb1ff7ea4e'
    # The above is how you define a proper authorization header in Django
    # Rest Framework using a token. The key needs 'Token ' in front of it.

    headers = {'Authorization': token_h}

    #credentials = {'username': 'admin', 'password': 'password123'}
    # credentials = {"username": "jacky", "password": "odessa"}


    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #                          data=credentials)

    response = requests.get('http://127.0.0.1:8000/api/profiles/',
                            headers=headers)

    print ('Status Code:', response.status_code)
    response_data = response.json()
    print (response_data)


if __name__ == '__main__':
    client()