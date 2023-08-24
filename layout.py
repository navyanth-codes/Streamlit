import streamlit as st

st.title("registration form")

first,last = st.beta_colums(2)

first.text_input("First Name")
last.text_input("Last Name")

email,mob=st.beta_columns([3,1])   #email is 3x bigger than the mob field

email.text_input("Email id")
mob.text_input("mob number")

user,pwd,pwd2=st.beta_colums(3)
user.text_input("USer name")
pwd.text_input("password",type="password")
pwd2.text_input("Re-type your password",type="password")

ch,bl,sub=st.beta_columns(3)
ch.checkbox("I agree")
sub.button("Submit")