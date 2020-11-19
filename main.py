import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:0000@localhost:3306/justq", encoding='utf-8')


from sqlalchemy import Table, MetaData, Column, insert
from sqlalchemy.orm.session import Session,sessionmaker
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.mysql import BIGINT, DECIMAL, VARCHAR, DATE

metadata = MetaData()

sampledata = Table('sampledata', metadata,
                   Column('Sno', BIGINT, primary_key=True),
                   Column('OrderDate', DATE),
                   Column('Region', VARCHAR(45)),
                   Column('Rep', VARCHAR(45)),
                   Column('Item', VARCHAR(45)),
                   Column('Unit', BIGINT),
                   Column('UnitCost', DECIMAL(10, 2)),
                   Column('EastRegulation', VARCHAR(45)),
                   Column('Total', DECIMAL(10, 2))
                   )


class SampleData(object):
    def __init__(self, Sno, OrderDate, Region, Rep, Item, Unit, UnitCost, EastRegulation, Total):
        self.Sno = Sno
        self.OrderDate = OrderDate
        self.Region = Region
        self.Rep = Rep
        self.Item = Item
        self.Unit = Unit
        self.UnitCost = UnitCost
        self.EastRegulation = EastRegulation
        self.Total = Total


mapper(SampleData, sampledata)

metadata.create_all(engine)


df = pd.read_excel('./SampleData.xlsx', sheet_name='SalesOrders', header=1)
df.columns = ['OrderDate', 'Region', 'Rep', 'Item', 'Unit', 'UnitCost', 'EastRegulation', 'Total']
df['OrderDate'] = df['OrderDate'].dt.date
print(df)
df.to_sql(name='sampledata', con=engine, if_exists='append', index=False)

print('-------------------------------')

# Session = sessionmaker(bind=engine)
# s = Session()
# for i in df.index:
#     data = (SampleData(i+1, df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7]))
#     s.add(data)

# s.query(SampleData)
# s.commit()




# for i in df.index:
#     sampledata.insert(SampleData(i+1, df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2],
#                        df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7]))