import MySQLdb as mdb
con = None
con = mdb.connect(host='realm.umd.edu', user='geoodk_user', passwd='geoodk_pass', 'odk')
cur = con.cursor()
cur.execute("USE odk;")
cur.execute("Show tables;")
for i in cur:
    print i
cur.execute("SHOW COLUMNS from BRAZIL_CROP_FORM_CORE;")
cur.execute("SELECT CROP_TYPE from BRAZIL_CROP_FORM_CORE;")
print '     '
for i in cur:
    print i
con.commit()
con.close()

