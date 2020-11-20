import requests

def client():
    data = {
        "username": "test2",
        "email": "test@te232ste.com",
        "password1": "changeme123",
        "password2": "changeme123",
    }
        
    if 1:
        rs = requests.post("http://lab4.localshi.com:8000/api/rest-auth/registration/",
                           data=data)
    else:
        headers = {"Authorization": "Token a68e8f0ebb1eb93ec9fbc21084728871b53b9ff4"}
        rs = requests.get("http://lab4.localshi.com:8000/api/profiles/",
                          headers=headers)
    print(rs.status_code)

    rs_data = rs.json()
    print(rs_data)

client()
