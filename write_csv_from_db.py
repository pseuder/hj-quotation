# -*- coding: utf-8 -*- 
#將database資料寫入csv檔案中
import sys
import subprocess
import csv
import sqlite3
import codecs
import os

if len(sys.argv) == 1:
    print("insufficient parameters")
    sys.exit(1)

if sys.argv[1] == '-w' or sys.argv[1] == '-l':
    database = sqlite3.connect("db.sqlite3")
    cursor = database.cursor()
    tables = ['Users','Test','Product']  ##database內的表格名稱

    if not os.path.isdir("./csv"):
        os.mkdir("./csv")

    for table in tables:
        csv_file = codecs.open(('./csv/%s.csv') % table, 'w', encoding='utf-8')
        writer = csv.writer(csv_file)

        for row in cursor.execute("SELECT * FROM %s" % table):
            writer.writerow(row)

        csv_file.close()
else:
    print("invalid parameter")
    sys.exit(1)
