import psycopg2
import datetime
import json
import pprint
import re
import os.path
from pathlib import Path
 

conn = psycopg2.connect("dbname=logs user=postgres password=admin")
cur=conn.cursor()
cur.execute("CREATE TABLE benchmark5(Some_description VARCHAR, Execution_environment_description VARCHAR, Date_when_benchmark_has_been_performed date, Server_name_where_benchmark_has_been_performed  VARCHAR, Application_version varchar, Test_suite_version varchar);")
cur.execute("CREATE TABLE testcase5(Method_API varchar, Method_name varchar, Parameters varchar);")
cur.execute("CREATE TABLE testcase_execution5(Testcase_execution_time_in_seconds float);")
file_path=input("Please enter the full file path")
if (len(file_path) ==0 or (not os.path.isfile(file_path))):
    print("Path can't be null, please insert a new path or you typed wrong file path")
else:
    with open(file_path, 'rt') as f:
        sending_pattern = r"Request: (.*) processed in (.*)s"
        rpc_calls = []
        for line in f:
            a = re.search(sending_pattern, line)
            json_text = a.group(1)
            rpc_calls.append(json.loads(json_text))
            a = re.search(r'in (.*)s', line)
            time = a.group(1)
            rpc_calls[-1]['time'] = float(time)
        print(rpc_calls)
        for i in rpc_calls: 
            c=json.dumps(i["time"])
            b=json.dumps(i["result"])
            description=input("Insert the description")
            environment=input("Insert environment")
            date_time=datetime.datetime.now()
            server=input("Insert server version" )
            app_version=input("Insert app version")
            version=input("Insert version")
            api_names=input("inser name")
            a=input("Method name insert")
            cur.execute("INSERT INTO benchmark5(Some_description, Execution_environment_description,Date_when_benchmark_has_been_performed, Server_name_where_benchmark_has_been_performed, Application_version, Test_suite_version) VALUES (%s, %s, %s, %s, %s,%s)", (description, environment, date_time, server, app_version, version))
            cur.execute("INSERT INTO testcase5(Method_API, Method_name, Parameters) VALUES (%s, %s, %s)", (api_names, a, b))
            cur.execute("INSERT INTO testcase_execution5(Testcase_execution_time_in_seconds) VALUES (%s)", (c,))

            conn.commit()

        cur.close()
        conn.close()



 











 














