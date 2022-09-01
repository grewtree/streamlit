import streamlit as st
import pandas as pd

import psycopg2
import os
from dotenv import load_dotenv

st.write("# test입니다.")
view = [100, 150, 30]
view

st.bar_chart(view)

sview = pd.Series(view)
sview


st.write('# test2입니다.')

## 환경설정
load_dotenv()
host = os.environ.get('host')
database = os.environ.get('database')
user = os.environ.get('user')
password = os.environ.get('password')

conn = psycopg2.connect(
    host = host,
    database = database,
    user = user,
    password = password )

cur = conn.cursor()

## DB 데이터 불러오기
def load_sql(cur) :
    ## 가장 최근 저장된 기사 타이틀 100개 불러오기
    cur.execute("""select title from dandok
    order by id desc
    limit 1;""")
    result = cur.fetchall()    
    ls = []
    print("스크래핑을 시작합니다. \n")
    print("우선 DB에 최근 저장된 기사를 불러옵니다.\n")
    for i in range(len(result)) :
        ls.append(result[i][0])
        print(f"#{i+1}", result[i][0])
    print("\nDB 불러오기 종료! \n")
    return ls

ls = load_sql(cur)

st.write(ls)