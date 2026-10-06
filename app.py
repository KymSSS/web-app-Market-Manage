import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

manage_button = st.button("จัดการสินค้า")
stock_button = st.button("เช็คจำนวนสินค้า")
calculate_button = st.button("คำนวณยอดขายสินค้า")
customer_button = st.button("จัดการข้อมูลลูกค้า")



