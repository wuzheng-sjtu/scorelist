#-*- coding:utf-8 -*-
#! /usr/bin/python

# crawler of the average scores of all classes available in automn 2016
__author__='Zheng Wu'

from splinter import Browser
import time
import re

browser=Browser('chrome')
url='http://electsys.sjtu.edu.cn/edu/login.aspx'
browser.visit(url)
time.sleep(15)
browser.visit('http://electsys.sjtu.edu.cn/edu/student/elect/warning.aspx?xklc=3&lb=1')
button=browser.find_by_id('CheckBox1')
if (browser.is_element_not_present_by_id('CheckBox1')):
	pass
else:
	button.click()
	browser.find_by_id('btnContinue').click()

# get the code of the classes
classlist = []
pattern=re.compile(r'[A-Z]{2}[0-9]{3}')
browser.find_by_id('SpeltyRequiredCourse1_btnXuanXk').click()
deparlist = ['02000','02500','03000','03300','03600','03700','04000','05000','07000','07100','07200','08000','08200','09000','11000','12000','13000','14000','14200','15000','16000','17000','18000','19000','20000','21000','22000','23000','24000','25100','26000','29100','30000','33000','35000','35100','36000','37000','38000','39000','40000','40001','40100','40110','40200','40300','40400','40500','40600','41000','41300','41500','41600','41700','41800','41900','42000','42100','42200','50100','50120','50200','50300','50400','50500','50501','50600','50700','50800','50900','60100','60200','60300','60400','60500','60520','60600','60700','60800','60900','61000','61100','61200','61300','61400','61410','61700','61800','62000','62100','62300','62400','62500','69100','70000','80000','80310','80510','90000','99000','999003','999007']
for depar in deparlist:
	browser.select('OutSpeltyEP1$dpYx',depar)
	for year in ['2014','2015','2016']:
		browser.select('OutSpeltyEP1$dpNj',year)
		browser.find_by_id('OutSpeltyEP1_btnQuery').click()
		#classlist=[]
		classes = browser.find_by_text('选修')
		#print classes
		if classes == []:
			break
		for ele in browser.find_by_tag('td'):
			if (re.match(pattern,ele.text)):
				if ele.text not in classlist:
					classlist.append(ele.text)
	#print classlist
classfile = open(u'classes.txt','w')
for classid in classlist:
	classfile.write(classid),classfile.write('\n')
#print classlist
#打开微信
wechaturl='http://wechat.shwilling.com/auth/qrcode/login?redirect=http%3A%2F%2Fwechat.shwilling.com%2Fsjtu%2Fcourse'
browser.visit(wechaturl)
print u'你现在有20s的时间扫描二维码确认登陆'
time.sleep(10)
print u'请稍等,本程序稍微有点慢...但是等待还是值得的.'
myfile=open(u'all_scorelist.txt','w')
for classid in classlist:
	time=['/2014-2015-1','/2014-2015-2','/2015-2016-1','/2015-2016-2']
	for i in range(4):
		class_str='http://wechat.shwilling.com/sjtu/course/detail/'+classid+time[i]
		browser.visit(class_str)
		if (browser.is_element_not_present_by_css('.d-name')):
			pass
		else:
			name=browser.find_by_css('.d-name').text
			timea=browser.find_by_css('.c-code').text
			meanscore=browser.find_by_css('.c-aver').text
			highscore=browser.find_by_css('.c-max').text
			print name,time[i],meanscore,highscore
			myfile.write(name.encode('utf-8')),myfile.write('\t'),myfile.write(time[i].encode('utf-8')),myfile.write('\t'),myfile.write(meanscore.encode('utf-8')),myfile.write('\t'), myfile.write(highscore.encode('utf-8')),myfile.write('\n')

classfile.close()
myfile.close()
browser.quit()