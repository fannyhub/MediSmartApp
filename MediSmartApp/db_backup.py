#!/usr/bin/env python
import os, sys
import MySQLdb
from MediSmartProject.settings import DATABASES as db

name = db['default']['NAME']
user = db['default']['USER']
passwd = db['default']['PASSWORD']

# cmd = 'mysqldump -u {0} -p{1} {2} > db_backup'.format(user, passwd, name)
cmd = 'SELECT * FROM MediSmartApp_patient INTO OUTFILE "/tmp/BEKAP_new.txt";'
#cmd = 'create table writers(id int primary key auto_increment, name varchar(25));'

def run_backup():
    try:
        con = MySQLdb.connect('localhost', user, passwd, name)
        cur = con.cursor()
        cur.execute(cmd)
    except MySQLdb.Error as e:
        print e.args

run_backup()
