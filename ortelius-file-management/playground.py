
#persist into database
# def test_persist():
#     sample_file = open('sample.md','rb');
#     result = run.persist_file(sample_file, 11, "readme")
#     print(result)

#test_persist()

#reconstruct from database
import base64
import psycopg2
import os

# Init db connection
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "postgres")
db_user = os.getenv("DB_USER", "postgres")
db_pass = os.getenv("DB_PASS", "postgres")
db_port = os.getenv("DB_PORT", "9876")

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass, port=db_port)

def reconstruct(compid, filetype):
        cursor = conn.cursor()
        sql = 'SELECT * FROM dm.dm_textfile WHERE compid = %s AND filetype = %s Order by lineno'
        cursor.execute(sql, [compid, filetype])
        records = cursor.fetchall()
        
        with open("sample_de.md", "wb") as fout:
            for rec in records:
                encoded_string = base64.b64decode(rec[3])
                fout.write(encoded_string)
                
        fout.close()
        conn.commit()

# reconstruct(100, 'readme')

import requests

API_ENDPOINT = "http://192.168.225.51:5000/file"

#request endpoint
def test_rest():
    data = {'compid': 100, 'filetype': 'readme', 'file': open('sample.md', 'rb').read()}
    r = requests.post(url = API_ENDPOINT, data = data)
    print("Status is:%s, Response is:%s  "%(r.status_code,r.text))

test_rest()