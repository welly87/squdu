#!/usr/bin/env python3

from impala.dbapi import connect
from impala.util import as_pandas

import sys
import os

conn = connect(host='178.128.112.105', port=21050) 
cursor = conn.cursor()

table_name = os.environ['SOURCE_TABLE']

create_statment = 'CREATE EXTERNAL TABLE IF NOT EXISTS ' + table_name + ' STORED AS KUDU TBLPROPERTIES("kudu.table_name" = "' + table_name + '");'
# print(create_statment)

cursor.execute(create_statment)
print("table created")

cursor.execute('SELECT count(*) FROM ' + table_name)

df = as_pandas(cursor)

print(df.head())
