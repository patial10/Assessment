import time
import os
import shutil 
import mysql.connector
conn = mysql.connector.connect(host='localhost',database='db1',user='root',password='')


def call_f2(i):         #for  folder 2, after every 5 sec all txt files move from folder 1 to folder 2
    src = 'f1/'
    dest = 'f2/'
    allf = os.listdir(src)
    for j in allf:
        shutil.move(src + j, dest + j)
    time.sleep(5)    
    if i%10==0:
        call_f3(i)
        
def call_f3(i):               #for  folder 3, after every 10 sec all txt files move from folder 2 and store them to database table. 
    print("in f3",i)
    src = 'f2/'
    dest = 'f3/'
    allf = os.listdir(src)
    for j in allf:
        shutil.move(src + j, dest + j)
        query = "UPDATE tb1 SET status = %s WHERE text1 = %s"
        val=(1,j)
        cur = conn.cursor()
        cur.execute(query,val)
        conn.commit()
        cur.close()
    time.sleep(10)     
    
    
    
#creating from here    
save_path="f1/"
ext = ".txt"
i=0
while True:
    file_name =  os.path.join(save_path, str(i)+ext)
    file = open(file_name, 'w')
    query = """INSERT INTO tb1 (text1, status) 
                       VALUES 
                       (%s, %s) """
    val=(str(i)+ext,0)
    cur = conn.cursor()
    cur.execute(query,val)
    conn.commit()
    cur.close()
    i=i+1
    file.close()
    time.sleep(1)
    if i%5==0:
        call_f2(i)    