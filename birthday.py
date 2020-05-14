import time
import ast
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
#attempt to import settings
    file = open("settings.json", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    userEmail = dictionary["UserInfo"]["email"]
    userPass = dictionary["UserInfo"]["password"]
    delay = dictionary["Settings"]["delay"]
    chromeDriverLocation = dictionary["Settings"]["chromeDriverLocation"]
    file.close()
    
    
except:
    #error in getting settings
    print("Error parsing settings.json")
    time.sleep(delay)
    exit()
else:
    
    #sleep cause why not
    time.sleep(delay) 
  
#define driver and load intial page
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromeDriverLocation)
driver.get('http://m.facebook.com/')
time.sleep(delay) 

#login
email = driver.find_element_by_name('email')
email.send_keys(userEmail)
password = driver.find_element_by_name('pass')
password.send_keys(userPass)
login = driver.find_element_by_name('login')
login.click()
time.sleep(delay)

#navigate to bday list page
driver.get("https://m.facebook.com/events/calendar/birthdays/")
time.sleep(delay)  

#get list of names and send random message
names = []
for element in  driver.find_elements_by_xpath("(//ul)[1]"):
    #get individuals name and store in case i wanna do anything with it later
    name = element.find_element_by_xpath("//a//p[1]")
    names.append(name.text)

    #generate random bday message
    bdayMessage = "Happy bday!"
    with open("birthday.cfg") as f:
        lines = f.readlines()
        bdayMessage = random.choice(lines)

    #fill randomly generated bday message into text box
    textinput = element.find_element_by_xpath("//textarea")
    if "$name" in bdayMessage:
        textinput.send_keys(bdayMessage.replace("$name",name.text.split(' ', 1)[0]))
    elif "$name" not in bdayMessage:
        textinput.send_keys(bdayMessage)

    time.sleep(delay/2)
    textsend = element.find_element_by_xpath("//button")
    textsend.click()
    time.sleep(delay)
    print("wished " + name.text + " a happy birthday")

print("ran successfully")
with open("history.logs", 'a') as f:
    for eye in names:
        f.write('Wished ' + eye + 'happy bday\n')
        
time.sleep(1)
driver.quit()
exit()