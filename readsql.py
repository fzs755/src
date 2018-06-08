import pymysql.cursors

connection = pymysql.connect(host='localhost',
  port=3306,
  user='root',
  password= '123456',
  db= 'test1',
  charset= 'utf8mb4')
try:
  with connection.cursor() as cursor:
    sql= "select `urlname`,`urlhref` from `wiki` where `id` is not null"        
    count= cursor.execute(sql)
    print(count)
    result= cursor.fetchall()
    print(result)
finally:
  connection.close()