import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

colum = st.columns(4)

with colum(0):
  manage_button = st.button("จัดการสินค้า")
with colum(1):
  stock_button = st.button("เช็คจำนวนสินค้า")
with colum(2):
  calculate_button = st.button("คำนวณยอดขายสินค้า")
with colum(3):
  customer_button = st.button("จัดการข้อมูลลูกค้า")




