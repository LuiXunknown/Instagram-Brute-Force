
from time import sleep
import requests
import re
uid1 = "d3b88cdf-5fc4-4ea7-b465-d3febd7d3673"
cr1 = requests.session()
counter = 0
listq = open('acc.txt',"r").read().splitlines()
def clo():
  input('Press Enter To Close ...')
  exit(0)
qwe = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi;1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com'
}

def l12(user,Pass):
  cr1_l = "https://i.instagram.com/api/v1/accounts/login/"
  cr ={
        'uuid': uid1,
        'password': Pass,
        'username': user,
        'device_id': uid1,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
  }
  login = cr1.post(cr1_l,data=cr, headers=qwe).text
  if ('"logged_in_user"') in login:
    print('Logged in As @{}'.format(user))
    return True   
  elif("Incorrect Username") in login:
    print("The username you entered doesn't appear to belong to an account. Please check your username and try again.")
    print('---------------------------------------------')
    print('Nama pengguna yang anda masukkan tidak tepat. Sila semak nama pengguna anda dan cuba lagi. Terima kasih')
    print('---------------------------------------------')
  elif('Incorrect password') in login:
    print("The password you entered is incorrect. Please try again.")
    print('Kata kunci anda tidak tepat, sila cuba lagi. Terima kasih')
    print('---------------------------------------------')
  elif ('"inactive user"') in login:
    print('Your account has been disabled for violating our terms. Learn how you may be able to restore your account.')
  elif ('checkpoint_challenge_required') in login:
    print('Secure !')
  else: 
    print(login)

def lo2t():
    logout_url = 'https://i.instagram.com/api/v1/accounts/logout/'
    logout = cr1.post(logout_url , headers=qwe).text
    if('{"status": "ok"}') in logout:
        pass
    else:
        print(f'Logged Out Faild')


def crona_vuris(com):
  global pstid , counter
  u = f'https://i.instagram.com/api/v1/media/{pstid}/comment/'
  awdi = {
        '_uuid': uid1,
        '_uid': uid1,
        '_csrftoken': 'missing',
        'comment_text': com
    }
  while True:
    r = cr1.post(u , data=awdi , headers=qwe).text
    if ('"status": "ok"') in r:
      counter +=1
      print('Done : {}'.format(counter))
    else:
      print('switching account')
      lo2t()
      break
    sleep(slp)




print('Brute Force Start')
print('   ,    ,    /\   /\ ')
print('  /( /\ )\  _\ \_/ /_')
print('  |\_||_/| < \_   _/ >')
print('  \______/  \|0   0|/')
print('   _\/_   _(_  ^  _)_')
print('   ( () ) /`\|V"""V|/`\ ')
print('     {}   \  \_____/  /')
print('     ()   /\   )=(   /\ ')
print('heheh  {}  /  \_/\=/\_/  \ ')
while True:
  for x in listq:
    user = x.split(':')[0]
    pr = x.split(':')[1]
    print(user)
    print(pr)
    if l12(user,pr):
      crona_vuris(com1)
    else:
        sleep(4)
        pass


