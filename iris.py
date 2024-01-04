import streamlit as st

with st.form("form_key"):
    st.write("What would you like to order?")
    appetizer=st.selectbox("Appetizer",options=["choice1", "choice2","choice3"])
    main=st.selectbox("Main course",options=["choice1", "choice2","choice3"])
    dessert=st.selectbox("Dessert",options=["choice1", "choice2","choice3"])
    wine=st.checkbox("Are you coming with wine?")
    visit_date=st.date_input("When are you coming?")
    visit_time=st.time_input("What time are you coming?")
    allergies=st.text_area("Any allergies?",placeholder="Leave us a note on any alllergies")
    submit_btn=st.form_submit_button("submit")
st.write(f"""your order summary:
         
Appetizer:{appetizer}

Main course: {main}

Dessert:{dessert}

Are you coming with wine:{"yes" if wine else "no"}

When are you coming:{visit_date}

What time are you coming:{visit_time}

Any allergies:{allergies}""")

