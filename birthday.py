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
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromeDriverLocation)
driver.get('http://m.facebook.com/')
time.sleep(delay) 

#login
email = driver.find_element_by_name('email')
email.send_keys(userEmail)
password = driver.find_element_by_name('pass')
password.send_keys(userPass)
# password.submit() alternate method for logging in, seems to bug out web tho
login = driver.find_element_by_name('login')
login.click()
time.sleep(delay)

#navigate to bday list page
driver.get("https://m.facebook.com/events/calendar/birthdays/")
time.sleep(delay)  

#get list of names and urls for their profile pages
names = []
urls = []
for element in  driver.find_elements_by_xpath("(//ul)[1]"):
    name = element.find_element_by_xpath("//a//p[1]")
    names.append(name.text)
    url = element.find_element_by_xpath("//a")
    urls.append(url.get_attribute('href')) 
    bdayMessage = "bday message"
    with open("birthday.cfg") as f:
        lines = f.readlines()
        bdayMessage = random.choice(lines)
    textinput = element.find_element_by_xpath("//textarea")
    if "$name" in bdayMessage:
        textinput.send_keys(bdayMessage.replace("$name",name.text.split(' ', 1)[0]))
    elif "$name" not in bdayMessage:
        textinput.send_keys(bdayMessage)
    
    time.sleep(delay/2)

    textsend = element.find_element_by_xpath("//button") name.text.split(' ', 1)[0]
    textsend.click()
    time.sleep(delay)
  






#goto each persons page and write happy birthday message of sorts!
# for x in urls:
#     driver.get(x)
#     print(names[urls.index(x)])
#     time.sleep(delay)
#     composebutton = driver.find_element_by_xpath("//*[contains(text(), 'Write on')]")
#     composebutton.click()
#     time.sleep(delay)
#     composeinput = driver.find_element_by_xpath("//textarea[1]")
#     composeinput.send_keys("Happy birthday!")
#     time.sleep(delay)





print('ran successfully')
time.sleep(1)
driver.quit()
exit()