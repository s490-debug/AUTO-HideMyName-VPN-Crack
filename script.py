# DON'T USE ON YOUR PC USE USING GOOGLE COLAB (link on it in readme file)

import sys
import requests

user_id = 'cracked by lovedilka'

def check_subscription(user_id):
    return True

def main():
    global user_id

    print("|| CRACKED BY LOVEDILKA WITH LOVE💖 ||")
  
    if check_subscription(user_id):
        url = 'https://hdmn.cloud/ru/demo/'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                email = input('\033[1;32mР’Р°С€ Email:\033[0m ')
                response = requests.post('https://hdmn.cloud/ru/demo/success/', data={"demo_mail": email})

                print('response: '+response.text)
            else:
                print('error! '+response.status_code+" response: "+response.text)
        except requests.RequestException as e:
            print(f"Request Exception! : {e}")
    else:
        print('bruh crack not work')

if __name__ == '__main__':
    main()
