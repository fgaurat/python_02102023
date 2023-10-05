import streamlit as st
from UserDao import UserDao
def main():
    st.set_page_config(layout="wide")
    dao =UserDao("users_db.db")
    users = dao.findAll()


    st.write("# Ceci est un titre")
    st.write("truc **important**")
    st.write("""
    ```bash
            ./streamlit run main.py
            ls -lrt
    ```
""")

    st.button("Reset", type="primary")
    if st.button('Say hello',key="sh_1"):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    first_name = st.text_input('Prénom')
    if st.button('Say hello',key="sh_2") and first_name:
        st.write('Bonjour', first_name)


    st.table(users)
if __name__=='__main__':
    main()
