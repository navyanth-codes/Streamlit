import streamlit as st
import pandas as pd
import numpy as np
import time 

a=[1,2,3,4,5,6,7,8,]
n=np.array(a)
nd=n.reshape((2,4))
dict={"name":"hi","gan":"star"}
#data=pd.read_csv("data//employees.csv")

st.dataframe(n)
st.dataframe(nd)
st.dataframe(dict)
# st.dataframe(data,width=100,height=100)
# st.table(data) #donot get scroll bar

st.json(dict)
# st.write(data) 
st.write(dict)


#cache to make the app speed

@st.cache

def ret_time(a):
    time.sleep(5)
    return time.time()

# if st.checkbox("1"):
#     st.write(ret_time())

# if st.checkbox("2"):
#     st.write(ret_time())


# it runs fast for second because of cache memory

if st.checkbox("1"):
    st.write(ret_time("1"))

if st.checkbox("2"):
    st.write(ret_time("2"))

#slow becoz we dont use cache memory

