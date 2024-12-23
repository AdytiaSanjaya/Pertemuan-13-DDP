import streamlit as st 

# st.title("hello Mas bro")
# st.write("piyeh? eneng 100?")
# st.image("1.jpeg", caption="iki opo?")

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")

nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu Utama" : [dashboard],
        "Transaksi" : [nabung]
    }
)
if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()