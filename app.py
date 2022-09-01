import streamlit as st
import pandas as pd

st.write("# test입니다.")
view = [100, 150, 30]
view

st.bar_chart(view)

sview = pd.Series(view)
sview