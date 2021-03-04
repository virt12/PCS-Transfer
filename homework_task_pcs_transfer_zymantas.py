import psycopg2
import re
import json
import datetime

conn = psycopg2.connect("dbname=logs user=postgres password=admin")

cur=conn.cursor()
cur.execute("CREATE TABLE ex_logs4(Some_description VARCHAR, Execution_environment_description VARCHAR, Date_when_benchmark_has_been_performed date, Server_name_where_benchmark_has_been_performed  VARCHAR, Application_version varchar, Test_suite_version varchar, Method_API varchar, Method_name varchar, Parameters varchar,  Testcase_execution_time_in_seconds float  );")

mylines = []                            
with open ('C:/Users/Žymantas/Desktop/homework/example_log.txt', 'rt') as myfile: 
    for myline in myfile:              
        mylines.append(myline)           

m8=mylines[8]
m8=re.sub('Sending for reference time measurement', '', m8)
m8=m8.lstrip("Sending")
m8=m8.replace("for reference time measurement","")
res8 = json.loads(m8)
m9=mylines[9]
m9=m9.replace("Got response in","")
m9=m9.replace("s","")
m9=float(m9)
firstdict={"time1":m9}
res8["time1"]=m9
print(res8)
m10=mylines[10]
m10=m10.lstrip("Sending")
m10=m10.replace("for reference time measurement","")
res10 = json.loads(m10)
print(res10)
m11=mylines[11]
m11=m11.replace("Got response in","")
m11=m11.replace("s","")
m11=float(m11)
secdict={"time2":m11}
res10["time2"]=m11
date1=datetime.datetime.now()
date2=datetime.datetime.now()
print("-------------")
print(res8)
print(5)
print(res10)
print("---------")
print(res8['method'])
print(res10['method'])
res8pslit=res8["method"].split(".")
print(res8pslit)
api1name=res8pslit[0] 
met1name=res8pslit[1]
print(api1name)
print(met1name)
res10pslit=res10["method"].split(".")
api2name=res10pslit[0]
met2name=res10pslit[1]
print(api2name)
print(met2name)
print(res8["params"])
params1=res8["params"]
params2=res10["params"]
params1=json.dumps(params1)
params2=json.dumps(params2) 
print(res10["params"])
time1=res8["time1"]
time2=res10["time2"]
descr1="Bench description1"
descr2="Bench description2"
env1="It is an execution environment1"
env2="It is an execution environment2"
server1="Sever 1"
server2="Server 2"
app1="Application1 version 2.25"
app2="Application1 version 2.28"
test1="Version 5"
test2="Version 6"
print(type(params1))

cur.execute("INSERT INTO ex_logs4 (Some_description, Execution_environment_description,Date_when_benchmark_has_been_performed, Server_name_where_benchmark_has_been_performed, Application_version, Test_suite_version,Method_API, Method_name, Parameters,Testcase_execution_time_in_seconds) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (descr1, env1, date1, server1, app1, test1, api1name, met1name, params1, time1))
cur.execute("INSERT INTO ex_logs4 (Some_description, Execution_environment_description,Date_when_benchmark_has_been_performed, Server_name_where_benchmark_has_been_performed, Application_version, Test_suite_version,Method_API, Method_name, Parameters,Testcase_execution_time_in_seconds) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (descr2, env2, date2, server2, app2, test2, api2name, met2name, params2, time2))

conn.commit()

cur.close()

conn.close()