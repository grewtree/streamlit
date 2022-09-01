from select import select
import streamlit as st
import pandas as pd
import psycopg2
from streamlit_option_menu import option_menu


## 사이드 바
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        # menu_title=None,
        options = ["Home", "Project", "Contact"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home" :
    st.title(f"You have selected {selected}")
if selected == "Project" :
    st.title(f"You have selected {selected}")
if selected == "Contact" :
    st.title(f"You have selected {selected}")

## nav 바
# selected = option_menu(
#         # menu_title="Main Menu",
#         menu_title=None,
#         options = ["Home", "Project", "Contact"],
#         menu_icon="cast",
#         default_index=0,
#         orientation = 'horizontal',
#     )


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("""select title from dandok
    order by id desc
    limit 5""")

# Print results.
for i in rows :
    st.write(f"{i[0]}")
