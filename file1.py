from selenium import webdriver 
from time import sleep
import subprocess as sp
#from cryptography.fernet import Fernet
#import json

#file = open('key.key','rb')
#key = file.read()
#file.close()

#f = Fernet(key)

x = sp.getoutput("whoami")
user = "bananaboi"
stat = 0

if(x==user):
        print("Welcome {}".format(x))
        stat = 1

#if(stat == 0):
    #print("Hello {}!".format(x))
    #print("Welcome to EasyLog. I can help you set up one command login")
    #print("Set login info\n")
    #sp.getoutput("echo { | cat > userinfo")
    #print("1. Facebook \n")
    #ch = int(input())
    #print("Enter username")
    #fb_u = str(input())
    #fb_u_bytes = fb_u.encode()
    #print("Enter password")
    #fb_p = str(input())
    #fb_p_bytes = fb_p.encode()
    #encofb_u = f.encrypt(fb_u_bytes)
    #encofb_p = f.encrypt(fb_p_bytes)
    #sp.getoutput("printf '\"fbu\": \"{}\",' | cat >> userinfo".format(encofb_u))
    #sp.getoutput("printf '\"fbp\": \"{}\",' | cat >> userinfo".format(encofb_p))
#    print("2. Gmail \n")
#    print("Enter username")
#    #gm_u = str(input())
    #gm_u_bytes = gm_u.encode()
#    print("Enter password")
    #gm_p = str(input())
    #gm_p_bytes = gm_p.encode()
    #encogm_u = f.encrypt(gm_u_bytes)
    #encogm_p = f.encrypt(gm_p_bytes)
    
    #sp.getoutput("printf '\"gmu\": \"{}\",' | cat >> userinfo".format(encogm_u))

    #sp.getoutput("printf '\"gmp\": \"{}\"'| cat >> userinfo".format(encogm_p))
    #x = user
    #sp.getoutput("printf '}' | cat >> userinfo")
    #sp.getoutput("chmod 700 userinfo.json") 


#with open('userinfo') as json_file:
    #data = json.load(json_file)
    

print("Enter platform name to login into it ")
c=str(input())

if('facebook' == c):
        #v1 = data["fbu"]
        #v11 = v1.encode()
        #usr= f.decrypt(v11)
        #v2 = data["fbp"]
        #v22 = v2.encode()
        #pwd= f.decrypt(v22)
        usr='amritya.lordstark@gmail.com'
        pwd='xoxoxo69'

        driver = webdriver.Chrome() 
        driver.get('https://www.facebook.com/') 
        print ("Opened facebook") 
        sleep(1) 

        username_box = driver.find_element_by_id('email') 
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(1) 

        password_box = driver.find_element_by_id('pass') 
        password_box.send_keys(pwd) 
        print ("Password entered") 
        login_box = driver.find_element_by_id('loginbutton') 
        login_box.click() 


elif(c=='gmail'):
        #v3 = data["gmu"]
        #v33 = v3.encode()
        #v4 = data["gmp"]
        #v44 = v4.encode()
        #v333 = f.extract_timestamp(v33)
        #v333 = f.decrypt(v33)
        #v444 = f.decrypt(v44)

        #print(v333,v44)
        usr='amritya.stark'
        pwd='Yuphoria6999'
        driver= webdriver.Chrome()
        driver.get(('https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession'))
        sleep(2)

        username = driver.find_element_by_id('identifierId')
        username.send_keys(usr)
        nextButton = driver.find_element_by_id('identifierNext')
        nextButton.click()

        sleep(3)

        password_box = driver.find_element_by_name('password') 
        password_box.send_keys(pwd) 
	 
        signInButton = driver.find_element_by_id('passwordNext')
        signInButton.click()

else:
        print("Oh Snap! We don't currently support this platform")

print ("Done") 
input('Press anything to quit') 
#driver.quit() 
print("Finished") 
