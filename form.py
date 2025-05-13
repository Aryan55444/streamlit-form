import streamlit as st

st.title("This is a student registration form")
st.subheader("Student Registration Form")


name = st.text_input("Enter your name")
password = st.text_input("Enter your password", type="password")
email = st.text_input("Enter your email")
phone = st.text_input("Enter your phone number")
address = st.text_input("Enter your address")
dob = st.date_input("Enter your date of birth")
if phone and not phone.isdigit():
    st.warning("Phone number should contain only digits")

if not email:
        st.warning("Email is required")
elif "@" in email and "." in email:
        st.success("Valid Email")
else:
        st.error("Invalid Email")

# Submit button
if st.button("Submit"):
    if not all([name, password, email, phone, address]):
        st.warning("Please fill out all fields")
    else:
        st.success("Form submitted successfully!")
      


if st.button("Reset"):
    st.session_state.clear()


    

