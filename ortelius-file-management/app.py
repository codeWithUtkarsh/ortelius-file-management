import os
import base64

import psycopg2
from flask import Flask, request
from flask_restful import Api

# Initialize flask
app = Flask(__name__)
api = Api(app)

# Initialize database connection
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "postgres")
db_user = os.getenv("DB_USER", "postgres")
db_pass = os.getenv("DB_PASS", "postgres")
db_port = os.getenv("DB_PORT", "9876")

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass, port=db_port)

@app.route('/file', methods=['POST'])
def post():  # completed
    try: 
        input_data = request.form
        
        file = input_data.get('file')
        compid = input_data.get('compid')
        filetype = input_data.get('filetype')
        
        encoded_bytes = base64.encodebytes(bytes(file, 'utf-8'))
        line_no = 1
        data_list = []
        for line in encoded_bytes.splitlines():
            d = (compid, filetype, line_no, line.decode('utf-8')) # this will be changed
            line_no += 1
            data_list.append(d)

        print (data_list) 
        cursor = conn.cursor()
        #pre-processing
        pre_process = 'DELETE FROM dm.dm_textfile WHERE compid = %s AND filetype = %s;'
        cursor.execute(pre_process, [compid, filetype])
        
        records_list_template = ','.join(['%s'] * len(data_list))
        sql = 'INSERT INTO dm.dm_textfile(compid, filetype, lineno, base64str) VALUES {}'.format(records_list_template)
        cursor.execute(sql, data_list)
        rows_inserted = cursor.rowcount

        conn.commit()   # commit the changes
        cursor.close()
        
        if rows_inserted > 0:
            return ({"message": f'components updated Succesfully'})
        else:
            return ({"message": f'oops!, Something went wrong!'})

    except Exception as err:
        print(err)
        cursor = conn.cursor()
        cursor.execute("ROLLBACK")
        conn.commit()
        
        return ({"message": f'oops!, Something went wrong!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)