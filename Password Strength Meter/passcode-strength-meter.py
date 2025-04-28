import streamlit as st
import re
st.set_page_config(page_title="Password Strength Checker",page_icon="🔐🔐")
st.title("Password Strength Checker")
st.markdown(""" ## Welcome to Password Strength Checker!👋🏻
            Use this simple app to check the strength of your password and get advice on how 
         to it stronger.We provide you tips on how to create a *strong password*🔐.""")
password =st.text_input("Enter your password",type="password")
feedback =[]
score = 0
if password:
   if len(password) >= 8:
    score +=1
else:feedback.append("✖ Password should have at least 8 characters.")
if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
  score += 1
else:
  feedback.append("✖ Password should contain both upper and lower case.")
if re.search(r'\d',password):
    score += 1
else:
  feedback.append("✖ Password should contain at least 1 digit.") 
if re.search(r'!@#$%^&*()_+?><{}+\[];-/.,',password):
   score += 1
else: 
  feedback.append("✖ Password should contain one special character.[{(!@#$%^&*_+?><+\;-/.,)}]") 

if score == 4:
  feedback.append("✔✔✔Your password is strong.")
elif score == 3:
  feedback.append("🟡 Your password is medium It could be strong.")
else:
  feedback.append("🔴Your password is too weak make it more stronger. ")
if feedback :
  st.markdown("## How to Improve your password")
for tip in feedback:
  st.write(tip)
else:
  st.info("Please Enter your password to get started.")
