# DON'T USE ON YOUR PC USE USING GOOGLE COLAB (link on it in readme file)

import sys
import requests

# РџРѕР»СѓС‡Р°РµРј user_id РёР· Р°СЂРіСѓРјРµРЅС‚РѕРІ РєРѕРјР°РЅРґРЅРѕР№ СЃС‚СЂРѕРєРё
user_id = 'cracked by lovedilka'

# Р¤СѓРЅРєС†РёСЏ РїСЂРѕРІРµСЂРєРё РїРѕРґРїРёСЃРєРё
def check_subscription(user_id):
    return True

# РћСЃРЅРѕРІРЅРѕР№ РєРѕРґ
def main():
    global user_id

    print("|| CRACKED BY LOVEDILKA WITH LOVE💖 ||")
  
    if check_subscription(user_id):
        url = 'https://hdmn.cloud/ru/demo/'

        try:
            response = requests.get(url)
            if response.status_code == 200 and 'Р’Р°С€Р° СЌР»РµРєС‚СЂРѕРЅРЅР°СЏ РїРѕС‡С‚Р°' in response.text:
                email = input('\033[1;32mР’Р°С€ Email:\033[0m ')
                response = requests.post('https://hdmn.cloud/ru/demo/success/', data={"demo_mail": email})

                if 'Р’Р°С€ РєРѕРґ РІС‹СЃР»Р°РЅ РЅР° РїРѕС‡С‚Сѓ' in response.text:
                    print('\033[1;32mР’Р°С€ РєРѕРґ СѓР¶Рµ РІ РїСѓС‚Рё!\033[0m РџСЂРѕРІРµСЂСЊС‚Рµ СЃРІРѕР№ РїРѕС‡С‚РѕРІС‹Р№ СЏС‰РёРє.')
                else:
                    print('вќЊ \033[1;31mРЈРєР°Р·Р°РЅРЅР°СЏ РїРѕС‡С‚Р° РЅРµ РїРѕРґС…РѕРґРёС‚ РґР»СЏ РїРѕР»СѓС‡РµРЅРёСЏ С‚РµСЃС‚РѕРІРѕРіРѕ РїРµСЂРёРѕРґР°.\033[0m')
            else:
                print('вќЊ \033[1;31mРћС€РёР±РєР°: РќРµРѕР±С…РѕРґРёРјРѕ РѕС‚РєР»СЋС‡РёС‚СЊСЃСЏ РѕС‚ СЃСЂРµРґС‹ РІС‹РїРѕР»РЅРµРЅРёСЏ Рё СѓРґР°Р»РёС‚СЊ РµРµ.\033[0m')
        except requests.RequestException as e:
            print(f"вќЊ \033[1;31mРћС€РёР±РєР° РїСЂРё Р·Р°РїСЂРѕСЃРµ Рє СЃР°Р№С‚Сѓ:\033[0m {e}")
    else:
        print('\033[1;31mРџРѕР¶Р°Р»СѓР№СЃС‚Р°, РїРѕРґРїРёС€РёС‚РµСЃСЊ https://t.me/keyhide, С‡С‚РѕР±С‹ РїСЂРѕРґРѕР»Р¶РёС‚СЊ.\033[0m')

if __name__ == '__main__':
    main()
