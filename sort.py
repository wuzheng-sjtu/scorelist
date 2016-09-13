#! usr/bin/python
#-*- coding:utf-8 -*-
# sort the scores from score_crawler.py
__author__='Zheng Wu'

file=open('./all_scorelist.txt').read()
file=file.split('\n')

mydict = {}

for i in range(len(file)):
	line=file[i]
	linelist=line.split('\t')
	try:
		score=float(linelist[2])
		mydict[i]=score
	except:
		pass
#print dic

myfile=open('sortscore.txt','w')
myfile.write('课程名称	均分	最高分	课程代码')
myfile.write('\n')
sortdict=sorted(mydict.iteritems(),key=lambda d:d[1],reverse=True)
for key,value in sortdict:
	myfile.write(file[key])
	myfile.write('\n')
myfile.close()
