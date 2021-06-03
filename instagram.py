from selenium import webdriver
import time
from credentials import username,password,speak
driver = webdriver.Chrome(executable_path=r"A:\Files\PyPy\Selenium\chromedriver.exe")

#connecting to website
speak("opening instaa gram")
driver.get("https://www.instagram.com/")
time.sleep(2)

#typing username and password
speak("entering id password")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
time.sleep(3)

#submit
driver.find_element_by_css_selector('button[type=submit]').click()
speak("wait for few seconds...it will be continue ")
time.sleep(5)

#not now buttons
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
speak("wait for 5 seconds")
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(2)

a = 1
count = 1
#like first 5 Post
for i in range(1,7):
    try:
        time.sleep(5)
        sp = "Post number {} liked".format(count)
        heart = "/html/body/div[1]/section/main/section/div/div[2]/div/article[{}]/div[3]/section[1]/span[1]/button".format(a)

        like = driver.find_element_by_xpath(heart)
        time.sleep(1)
        like.click()
        time.sleep(1)
        print(sp)
        speak(sp)
        count += 1
        if(a<7):
            a += 1
        else:
            #time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[8]/div[3]/section[1]/span[1]/button").click()
    except:
        print("something went wrong !! at count{}".format(count))

        
speak("Task Complete")
