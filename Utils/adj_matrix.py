import pandas as pd
import pyarrow as pa
from pyarrow import parquet as pq
def adjMatrix(file,df):
    df1=df.copy()
    seq=pd.read_csv(f'../Relations/{file}.csv')
    df1.set_index(df1.columns[1:],inplace=True)
    df1.drop("Total_terms",inplace=True,axis=1)
    for i in range(len(seq)):
        df1[seq["go_id"][i]][seq["parent_id"][i]]=1
    df1.columns = df1.columns.str.replace('[^a-zA-Z0-9]', '_',regex=True)
    pq.write_table(pa.Table.from_pandas(df1), f'../Adj_Matrices/{file}.parquet')
