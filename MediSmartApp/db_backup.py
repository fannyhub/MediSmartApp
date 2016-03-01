#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import datetime as dt
import MySQLdb
import codecs
from MediSmartProject.settings import DATABASES as db

today = dt.datetime.now()
name = db['default']['NAME']
user = db['default']['USER']
passwd = db['default']['PASSWORD']

# cmd = 'mysqldump -u {0} -p{1} {2} > db_backup'.format(user, passwd, name)
#cmd = 'SELECT * FROM MediSmartApp_patient INTO OUTFILE "/tmp/BEKAP_new.txt";'
#cmd = 'create table writers(id int primary key auto_increment, name varchar(25));'
#cmd = 'SELECT last_name, first_name FROM MediSmartApp_patient;'
cmd = 'SELECT visit_date, description FROM MediSmartApp_visit;'


def run_backup():
    print 'ehllo'
    try:
        print user, passwd, name
        con = MySQLdb.connect('localhost', user, passwd, name, use_unicode=True)
        print 'connected'
        cur = con.cursor()
        cur.execute(cmd)
        print 'cmd executed'
        result_list = []
        for row in cur:
            print row
            #addition = '{0} {1}'.format(*row) + '\n'
            #row = ''.join(unicode(row)) + '\n'
            #result_list.append(row)
            #result_list.append(addition)
            result_list.append(row[1])
        #string = ''.join(result_list)
        print result_list
        with open('/tmp/backup/BACKUP_PACJENTOW_{0}.txt'.format(today), 'w') as f:
            print 'codecs open ok'
            for line in result_list:
                print type(line)
                try:
                    f.write(line.encode("utf-8", 'replace'))
                except Exception as e:
                    print 'unable to write line'
                    print e.args

        con.close()
        print 'CONNECTION CLOSED'

    except MySQLdb.Error as e:
        print e.args




run_backup()
