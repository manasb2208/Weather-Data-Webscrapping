from selenium import webdriver
import time


def nday(month,year):
	if month in ['january','march','may','july','august','october','december']:
		no_day= 31
	elif month in ['april','june','september','november']:
		no_day = 30
	elif month == 'february':
		if (year%4 == 0) and (not(year%100 == 0)) or (year%400 == 0):
			no_day = 29
		else:
			no_day = 28
	return no_day

cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe"
#mon = input("Enter the month: ").lower()
#mon = mon.lower()
mon = 'october'
#yr = int(input("Enter the year: "))
yr = 2020

n_day=nday(mon,yr)
#time.sleep(20)
url = 'https://www.accuweather.com/en/in/kolkata/206690/' + mon +'-weather/206690?year=' + str(yr) + '&view=list'
#print(url)
driver = webdriver.Chrome(cd)
time.sleep(5)
driver.get(url)


data1 = driver.find_elements_by_xpath("//div[@class = 'date']")
date = []
for i in data1:
	date.append(i.text)


data2 = driver.find_elements_by_xpath("//div[@class = 'high  ']")
h_temp = []
for i in data2:
	h_temp.append(i.text)


data3 = driver.find_elements_by_xpath("//div[@class = 'low' ]")
l_temp =[]
for i in data3:
	l_temp.append(i.text)
 
for i, j in enumerate(date):
	if j == '1':
		st_indx = i
		lt_indx = st_indx + n_day
		break

print(st_indx)
print(lt_indx)


date = date[st_indx:lt_indx]
h_temp = h_temp[st_indx:lt_indx]
l_temp = l_temp[st_indx:lt_indx]

print(date)
print(h_temp)
print(l_temp)


dicn = {'DATE' : date, 'High_Temp': h_temp, "Low_Temp": l_temp}
print(dicn)


import pandas as pd
df = pd.DataFrame(dicn)
print(df)
df.to_csv("C:\\Users\\Manas\\accuweather.csv", index = False)
print("Done")