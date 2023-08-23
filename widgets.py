import streamlit as st

st.title('widgets')

#button

if st.button("subscribe"):
    st.write("namaste")              #if for adding functionality

name=st.text_input("Name :")
st.write(name)

#more text

address = st.text_area("Enter your address")
st.write(address)

st.date_input("enter a date")
st.time_input("enter a time")


#checkbox

if st.checkbox("you accept by clicking ",value=False):
    st.write("thanks")

#radio button

v1=st.radio("colours",["r","b","g"],index=0)   #index already option will be selected

v2=st.selectbox("colours",["r","b","g"],index=0)  #top down menu

st.write(v1,v2)

v3=st.multiselect("colours",["r","b","g"])
st.write(v3)


# slider

st.slider("Age",min_value=18,max_value=90,value=30,step=2)

st.number_input("numbers",min_value=18,max_value=90,value=30,step=2)

# numbers can be int and float

#adding files

st.file_uploader("upload a file")

