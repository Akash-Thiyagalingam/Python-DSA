import mysql.connector
from datetime import datetime

str_d1 = str('2023-05-10')


d1 = datetime.strptime(str_d1, "%Y-%m-%d")

conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
cur = conn.cursor()
'''SELECT startDate, endDate
FROM YourTable
WHERE '2012-10-25' between startDate and endDate'''
cur.execute("SELECT *  FROM  booktb where VehicleNo='TN45AL5535' and  '" + str_d1 + "' between   SDate  and  Edate  ")
data2 = cur.fetchone()
if data2:
    print('yes')
else:
    print('No')

