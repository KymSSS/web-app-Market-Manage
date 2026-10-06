import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

with colum(1)
manage_button = st.button("จัดการสินค้า",width="stretch")
with colum(2)
stock_button = st.button("เช็คจำนวนสินค้า",width="stretch")
with colum(3 )
calculate_button = st.button("คำนวณยอดขายสินค้า",width="stretch")
with colum(4)   
customer_button = st.button("จัดการข้อมูลลูกค้า",width="stretch")



