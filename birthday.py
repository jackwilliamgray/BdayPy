import time
import ast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
try:
    file = open("settings.json", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    userEmail = dictionary["UserInfo"]["email"]
    userPass = dictionary["UserInfo"]["password"]
    delay = dictionary["Settings"]["delay"]
    file.close()
    
    
except:
    print("Error parsing settings.json")
    time.sleep(delay)
    exit()
else:
    time.sleep(delay)  # Let the user actually see something!
# Optional argument, if not specified will search path.

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options,
    executable_path=r'C:\Users\raow2\Documents\BirthdayPy\chromedriver_win32\chromedriver.exe')
    
driver.get('http://m.facebook.com/')
time.sleep(delay)  # Let the user actually see something!
email = driver.find_element_by_name('email')
email.send_keys(userEmail)
password = driver.find_element_by_name('pass')
password.send_keys(userPass)
# password.submit() alternate method for logging in, seems to bug out web tho
login = driver.find_element_by_name('login')
login.click()
time.sleep(delay)
driver.get("https://m.facebook.com/events/calendar/birthdays/")
time.sleep(delay)  # Let the user actually see something!

# todaysBirthdays = driver.find_element_by_xpath("(//ul)[1]")
# for element in  driver.find_elements_by_class_name('_52jh _5at0 _592p'):
for element in  driver.find_elements_by_xpath("(//ul)[1]//div//p"):
    print(element.text)
    time.sleep(delay)
print('logged in successfully')
time.sleep(1)
driver.quit()
exit()