<<<<<<< HEAD
import psycopg2
import datetime
import json
import pprint
import re
import os.path
 

=======
#import psycopg2
#import re
#import json
#import datetime




import json
import pprint
import re


with open('C:/Users/Žymantas/Desktop/homework/example_log.txt', 'rt') as f:
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

    pprint.pprint(rpc_calls)
    pprint.pprint(type(rpc_calls))
    for a in rpc_calls:
        #cur.execute("INSERT INTO ex_logs4 (Some_description, Execution_environment_description,Date_when_benchmark_has_been_performed, Server_name_where_benchmark_has_been_performed, Application_version, Test_suite_version,Method_API, Method_name, Parameters,Testcase_execution_time_in_seconds) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (descr1, env1, date1, server1, app1, test1, api1name, met1name, params1, time1))












#conn = psycopg2.connect("dbname=logs user=postgres password=admin")
>>>>>>> c7fccc5429ecac723d6a86053ff8c16bcb66f22f

#cur=conn.cursor()
#cur.execute("CREATE TABLE ex_logs4(Some_description VARCHAR, Execution_environment_description VARCHAR, Date_when_benchmark_has_been_performed date, Server_name_where_benchmark_has_been_performed  VARCHAR, Application_version varchar, Test_suite_version varchar, Method_API varchar, Method_name varchar, Parameters varchar,  Testcase_execution_time_in_seconds float  );")

<<<<<<< HEAD
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
=======
#with open('C:/Users/Žymantas/Desktop/homework/example_log.txt', 'rt') as f:
    #text = f.read()
    #pattern = "Sending (.*) for reference time measurement\s+Got response in (.*)s"
   # a=re.findall(pattern, text)
   # print(a)
   # print(type(a))
   # print(a[0])
    #print(a[1])
    #for i in a:
    #    a[i]=json.loads(a[i])
    #b=[json.loads(thing) for thing in a]
    #print(a[1][0])
    #print(b)
    #b=json.dumps(a)

    #print(b)
    #b=json.loads(b)
    #print(b)
    #print(type(b))
    #for i in a:
    #    print(i[0])
    #print(type(a))
>>>>>>> c7fccc5429ecac723d6a86053ff8c16bcb66f22f



 











<<<<<<< HEAD
 














=======


'''
mylines = []                            
with open ('C:/Users/Žymantas/Desktop/homework/example_log.txt', 'rt') as myfile: 
    for myline in myfile:              
        mylines.append(myline)  


with open(blah blah blah) as f:
    text = f.read()


'''
'''         

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
'''
>>>>>>> c7fccc5429ecac723d6a86053ff8c16bcb66f22f
