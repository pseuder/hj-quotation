import os 

fp = open("db.sqlite3",'w')
fp.close()
print(os.popen('python manage.py migrate').read())