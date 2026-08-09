import pandas as pd
from sqlalchemy import create_engine

connectionurl="postgresql://postgres:99Manvik99@localhost:5432/Python"

engine= create_engine(connectionurl)


query="""SELECT * FROM public."Product" """

data=pd.read_sql_query(query,engine)
print(data)

engine.dispose()