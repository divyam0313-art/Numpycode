import csv
import pandas as pd
import random
import json


##### READER CSV
with open("customers.csv",mode="r") as file:
    # data=csv.reader(file)
    # for row in data:
    #     print(row)
    #     print("-------------------------------------------------------------------------")
    df=pd.DataFrame(csv.reader(file))
    print(df)

    ##pd.reader"_csv()

##### Writer CSV
names=['a','b','c','d']
gender=['male','female','male','female']
age=[random.randint(16,31) for _ in range(4)]
marks=[random.randint(216,331) for _ in range(4)]
subject= random.choices(['py','ja','AI'], k=4)

df=pd.DataFrame({
    "name":names,
    "gender" : gender,
    "age" :age,
    "marks":marks,
    "subject": subject
})
students=[names,gender,age,marks,subject]
df.to_csv("dfstudents.csv",index=False)
with open("students.csv" ,mode="w" ,newline="") as studentsfile:
    writer=csv.writer(studentsfile)
    writer.writerows(students)
studentsfile.close()

#### JASONREADeR
print("JSON READER")
with open("employee.json" , 'r') as employeefile:
    employeedata=json.load(employeefile)

print(employeedata["employees"]) 
employeefile.close()

####### JASON WRITE
employeedata["employees"].append({'id':104 ,'firstName' :"John" ,"lastName":"salar"})

with open ("employee.json" ,'w') as filee:
   json.dump(employeedata,filee,indent=5)

   filee.close()
