# MySQL 연결
import pymysql

conn = pymysql.connect(host='localhost', user='zerock', password='zerock',
                        db='book_ex', charset='utf8')

curs = conn.cursor()

sql = "select * from tbl_board where bno=2"
curs.execute(sql)

rows = curs.fetchall()
print(rows)
# ((2, 'aaa', 'aaa', 'aaa', datetime.datetime(2021, 10, 22, 14, 53, 24), 0, 0),)

conn.close()

