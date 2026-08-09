import pandas as pd
import numpy as np
import random

""" data= pd.read_csv("customers.csv")
headdata=data.head()
##print(headdata)
print(data.shape) """

random.seed(101)
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

print(df)
data=df.describe()
print(df['marks'])
print(df[['name','marks']])

print(df['marks']>295)

"""loc to provide label and index for iloc"""
print(df.loc[1])

print(df.iloc[:3])

print(df.iloc[:,:3]) ## fetc all rows and first 3 columns

df['doublemarks']=df['marks']*2 ## creates new column doublkemarks with 

df['marks']=df['marks'].apply(lambda x:x+5)


##Rename column names

df.drop(['doublemarks'],axis=1) ## axis=1 for column ,0 for rows


print(df) 

print(df['name'][0])

print(df[0:2])

df=df.set_index('name')


df.sort_values(by=['age','marks'])

df.reset_index(inplace=True)

print(df)

df.isnull()

df.dropna()

df.drop_duplicates()

## Merge 2 df

df2=pd.DataFrame({'name':['b','y'],'attendence':[10,34]})

df3=pd.merge(df,df2,on='name',how="outer")
print(df3)

df2=pd.DataFrame({'name':['g','p'],'attendence':[120,342]})

print(pd.concat([df2,df3]))

print(df.groupby('gender')['marks'].max())

print(df.pivot_table(values='marks',index='gender',columns='subject',aggfunc="max"))

df['newgender']=df['gender'].map({'male':0,'female':1})
print(df)

##pd.to_datetime(df['date'])

