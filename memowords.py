#-*-coding:utf-8-*-
import urllib
import urllib.request
import sys
import urllib.parse
import base64
import xlrd
import time
import datetime
from time import strftime, localtime

def memo_print(print_data):
    s=bytes(print_data,encoding='gb2312')
    s1=s.decode('gb2312')
    s2=s1.encode('gb2312')
    s3=base64.b64encode(s2)
    s4='T:'+str(s3)[2:len(s3)+2]  #s4即为最终可post的数据
    print(s4)
    print(type(s4))
    test_data = {'ak':'******','timestamp':'2019-12-18 14:22:39','memobirdID':'*********','printcontent':s4,'userID':'********'}
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    requrl = "http://open.memobird.cn/home/printpaper"
    req=urllib.request.Request(url = requrl,data =test_data_urlencode)
    #print(req)
    #print(test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    print(res)

def get_time():
    now_time = datetime.datetime.now().strftime('%H'+'%M')
    return str(now_time)
def get_date():
    now_date = strftime('%Y-%m-%d %H:%M:%S',localtime())
    return str(now_date)

def daily_print():

    day_num = 20   #设置每天词汇量
    try:
        db = open('database.txt','r')
    except:
        print('未检测到数据库文件，请将数据库移动至脚本所在目录')
    else:
        pass

    try:
        with open('work_conf.txt', 'r') as work_conf:
            work_lines = work_conf.readlines()
            work_last_line = int(work_lines[-1]) #取最后一行
    except:
        work_conf = open('work_conf.txt','w')
        work_last_line = 0
        work_conf.close()

    else:
        with open('database.txt', 'r') as db:
            db_lines = db.readlines()
            words_list = []
            for word_num in range(0,day_num): 
                words_list.append(db_lines[work_last_line+word_num])
                    
            db.close()
        with open('work_conf.txt' , 'w') as work_conf:
            work_conf.write(str(work_last_line+word_num))
            work_conf.close()
    print(words_list)

    pdata = get_date()+'\n'

    for pnum in range(0,day_num):
        pdata=pdata+words_list[pnum]+'\n'
    return pdata

print('now time:'+get_time())
memo_print(str(daily_print()))
print('succeed in '+get_date())
'''#定时执行
while True:
    if get_time() == '2210':
        try:
            print('now time:'+get_time())
            #print(str(daily_print()))
            memo_print(str(daily_print))
        except:
            print('打印失败，请检查！')
        else:
            print('succeed in '+get_date())'''
