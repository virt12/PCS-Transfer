import psycopg2
import datetime
import json
import pprint
import re
import os.path
 


conn = psycopg2.connect("dbname=logs user=postgres password=admin")

cur=conn.cursor()
cur.execute("CREATE TABLE ex_logs21(Some_description VARCHAR, Execution_environment_description VARCHAR, Date_when_benchmark_has_been_performed date, Server_name_where_benchmark_has_been_performed  VARCHAR, Application_version varchar, Test_suite_version varchar, Method_API varchar, Method_name varchar, Parameters varchar,  Testcase_execution_time_in_seconds float  );")


file_path=input("Please enter the full file path")
if (len(file_path) ==0 or (not os.path.isfile(file_path))):
    print("Path can't be null, please insert a new path or you typed wrong file path")
else:
    with open(file_path, 'rt') as f:
        sending_pattern = r"Sending (.*) for reference time measurement"
        rpc_calls = []
        for line in f:
            a = re.search(sending_pattern, line)
            if a:
                json_text = a.group(1)
                rpc_calls.append(json.loads(json_text))
            else:
                a = re.search(r'Got response in (.*)s', line)
                if a:
                    time = a.group(1)
                    rpc_calls[-1]['time'] = float(time)
        for i in rpc_calls:
            description=input("Insert the description")
            environment=input("Insert environment")
            date_time=datetime.datetime.now()
            server=input("Insert server version" )
            app_version=input("Insert app version")
            version=input("Insert version")
            api_name=i["method"].split(".")
            api_names=api_name[0]
            a=api_name[1]
            b= json.dumps(i["params"])
            c=json.dumps(i["time"])
            cur.execute("INSERT INTO ex_logs21(Some_description, Execution_environment_description,Date_when_benchmark_has_been_performed, Server_name_where_benchmark_has_been_performed, Application_version, Test_suite_version,Method_API, Method_name, Parameters,Testcase_execution_time_in_seconds) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (description, environment, date_time, server, app_version, version, api_names, a, b,c ))
            conn.commit()

        cur.close()

        conn.close()



 











 














