from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random




def generate_credentials():
	string_set = "abcdefghijklmnopqrstuvwxyz"
	pass_len = 5
	rand_string =  "".join(random.sample(string_set, pass_len))
	return rand_string



def connect():
	print('Connecting with tcpvpn...')

	global browser
	browser = webdriver.Chrome('/media/akshat/Others/Programs/Selenium Webdrivers/chromedriver')
	browser.get('https://www.tcpvpn.com/vpn-server-india')
	time.sleep(10)
	server = browser.find_elements_by_xpath('//*[@id="tcp"]/div[2]/div/form/button')
	server[0].click()
	return



def create_account(rand_string):
	user = browser.find_elements_by_xpath('//*[@id="exampleInputEmail1"]')
	user[0].send_keys(rand_string)
	passwd = browser.find_elements_by_xpath('//*[@id="exampleInputPassword1"]')
	passwd[0].send_keys(rand_string)
	create = browser.find_elements_by_xpath('//*[@id="edit-profile"]/button')
	create[0].click()
	return



rand_string = generate_credentials()
connect()
create_account(rand_string)




print("Account successfully created")
print("username: "+rand_string)
print("password: "+rand_string)





browser.close()