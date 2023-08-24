import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

plt.style.use("ggplot")
data={
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

rad=st.sidebar.radio("Navigation",['Home','About US'])
if rad=='Home':
  df=pd.DataFrame(data=data)

# col=st.sidebar.selectbox("Select a column",df.columns)
  col=st.sidebar.multiselect("Select a column",df.columns)
  plt.plot(df['num'],df[col])

  st.pyplot()

if rad=='About US':

  progress = st.progress(0)
  for i in range(100):
    time.sleep(0.1)
    progress.progress(i+1)

  st.balloons()

  st.write("you are here in about us")  
  #status message

  st.error("Error")
  st.success("success")
  st.info("info")
  st.exception(RuntimeError("this is error"))


#progress bar










