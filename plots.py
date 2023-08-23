import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image


data=pd.DataFrame(np.random.randn(100,3),columns=['a','b','c'])

chart=alt.Chart(data).mark_circle().encode(
    x='a',y='b',tooltip=['a','b']
)

st.altair_chart(chart,use_container_width=True)

# creating flow charts

st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch                                   

}

""")

#graphs

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

#matplotlib
plt.scatter(data['a'],data['b'])
plt.title("scatter")
st.pyplot()


#  to get map in streamlit

cont_data=pd.DataFrame({
    'awsome cities' : ['chicago','minneapolies','lovisville','Topeka'],
    'lat':[41.868171,44.979840,38.257972,39.030575],
    'lon':[-87.667458,-93.272474,-85.765187,-95.702548]
})

#  st.map()
st.map(cont_data)

# media on stream lit

image=Image.open('2170400.jpg')
st.image(image,caption='hi')

# st.audio('data//demo.wav')

# st.video("data//video.mp4")

# youtube links
# st.video("https://youtu.be/3xJYP_C4KNE")