import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:0000@localhost:3306/justq", encoding='utf-8')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT,DECIMAL,VARCHAR
from sqlalchemy import Column, Date

Base = declarative_base()

class Test(Base):
    __tablename__='sampledt'
    __table_args__={'extend_existing':True}
    OrderDate = Column(Date)
    Region = Column(VARCHAR)
    Rep = Column(VARCHAR)
    Item = Column(VARCHAR, primary_key=True)
    Unit = Column(BIGINT)
    UnitCost = Column(DECIMAL)
    EastRegulation = Column(VARCHAR)
    Total =Column(DECIMAL)

metadata = Base.metadata
metadata.create_all(engine)

df = pd.read_excel('./SampleData.xlsx', sheet_name='SalesOrders', header=1)
df.columns = ['OrderDate', 'Region', 'Rep', 'Item', 'Unit', 'UnitCost', 'EastRegulation', 'Total']
df['OrderDate'] = df['OrderDate'].dt.date
print(df)
df.to_sql(name='sampledt', con = engine, if_exists='append', index=False)

