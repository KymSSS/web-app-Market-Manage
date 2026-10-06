import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

#ข้อมูลลูกค้า

Customer_data = {}

colum = st.columns(4)


with colum[0]:
  manage_button = st.button("จัดการสินค้า",width="stretch")
  if manage_button:
    st.session_state["menu"] ="จัดการสินค้า"


with colum[1]:
  stock_button = st.button("เช็คจำนวนสินค้า",width="stretch")
  if stock_button:
    st.session_state["menu"] = "เช็คจำนวนสินค้า"


with colum[2]:
  calculate_button = st.button("คำนวณยอดขายสินค้า",width="stretch")
  if calculate_button:
    st.session_state["menu"] = "คำนวณยอดขายสินค้า"


with colum[3]:
  customer_button = st.button("จัดการข้อมูลลูกค้า",width="stretch")
  if customer_button:
    st.session_state["menu"] = "ลูกค้า"


if st.session_state.get("menu") == "จัดการสินค้า":
  st.header("ควาย")
  name = st.text_input("ชื่อ-นามสกุล")
elif st.session_state.get("menu") == "เช็คจำนวนสินค้า":
  st.header("ควาย")
  name = st.text_input("ชื่อ-นามสกุล")
elif st.session_state.get("menu") == "คำนวณยอดขายสินค้า":
  st.header("ควาย")
  name = st.text_input("ชื่อ-นามสกุล")
elif st.session_state.get("menu") == "ลูกค้า":
  st.header("จัดการข้อมูลลูกค้า")
  name = st.text_input("ชื่อ-นามสกุล")




