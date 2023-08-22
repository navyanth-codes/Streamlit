import streamlit as st

#title for web

st.title("Hi Navyanth")   

# header and subheader

st.header("Header")

st.subheader("Sub header")


st.text("this is test")  # markdown and latex to update the text 

st.markdown(""" # h1 tag
## h2 tag
### h3 tag<br>            
:moon:  
**bold** <br>
__ italic __
:sunglasses: """,True)

#br for brick command and true for executing 


st.latex(r''' \int_a^b \iint \oint''')  # to write latex forms

# write command

st.write("nav","sya","ml")
st.write(" # Navyanth")  # --> heading
#st.write(st)
#st.write(sum)   # we caan pass the modules ,dictionaries, functions it will explain about them

#run in command prompt as streamlit run intro.py