import time
import os
import shutil 
import mysql.connector
conn = mysql.connector.connect(host='localhost',database='db1',user='root',password='')


def queue():         
	src = 'Processing/'
	dest = 'queue/'
	allf = os.listdir(src)
	for j in allf:
		shutil.move(src + j, dest + j)
		
	file_list = os.listdir('queue/')
	for i in file_list:                       #insert file to database with status 1.
		query = """INSERT INTO tb1 (text1, status) 
						VALUES (%s, %s) """
		val=(i,1)
		cur = conn.cursor()
		cur.execute(query,val)
		conn.commit()
		cur.close()
		
	src_queue = 'queue/'                     #move all files to processed folder from queue
	dest_Processed = 'processed/'
	all_files = os.listdir(src_queue)
	for j in all_files:
		shutil.move(src_queue + j, dest_Processed + j)
		

    
    
    
    
#creating files from here inside Processing folder   
save_path="Processing/"
ext = ".txt"
i=0
starting_time = time.ctime().split()[-2].split(':')[-1]
while True:
    file_name =  os.path.join(save_path, str(i)+ext)
    file = open(file_name, 'w')
    i=i+1
    file.close()
    time.sleep(1)
    if i%5==0:#move all files from processing to queue folder
	    if not os.listdir('queue/'):#only if folder queue is empty 
		    queue()    