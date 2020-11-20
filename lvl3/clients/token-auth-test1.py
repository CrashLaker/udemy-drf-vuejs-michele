import requests

def client():
    credentials = {
        "username": "admin",
        "password": "admin"
    }
        
    if 0:
        rs = requests.post("http://lab4.localshi.com:8000/api/rest-auth/login/",
                           data=credentials)
    else:
        headers = {"Authorization": "Token e8dbcec4818a662892c91560886235ad8b5a0106"}
        rs = requests.get("http://lab4.localshi.com:8000/api/profiles/",
                          headers=headers)
    print(rs.status_code)

    rs_data = rs.json()
    print(rs_data)

client()
