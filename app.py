import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

#ข้อมูลลูกค้า

Customer_data = {
    '101' : {
        'Customer Name' : 'John Doe',
        'age' : 32 ,
        'Gender' : 'Male' ,
        'Total Spend' : 2500
    },
    '102' : {
        'Customer Name' : 'Jane Smith',
        'age' : 27 ,
        'Gender' : 'Female' ,
        'Total Spend' : 1500
    },
    '103' : {
        'Customer Name' : 'Robert Brown',
        'age' : 45 ,
        'Gender' : 'Male' ,
        'Total Spend' : 3200
    },
    '104' : {
        'Customer Name' : 'Emily Davis',
        'age' : 38 ,
        'Gender' : 'Female' ,
        'Total Spend' : 1800
    },
    '105' : {
        'Customer Name' : 'Michael Johnson',
        'age' : 29 ,
        'Gender' : 'Male' ,
        'Total Spend' : 2100
    }
}

colum = st.columns(4)

with colum[0]:
  manage_button = st.button("จัดการสินค้า",width="stretch")
  if manage_button:
    st.markdown("สวัสดี")

with colum[1]:
  stock_button = st.button("เช็คจำนวนสินค้า",width="stretch")
with colum[2]:
  calculate_button = st.button("คำนวณยอดขายสินค้า",width="stretch")
with colum[3]:
  customer_button = st.button("จัดการข้อมูลลูกค้า",width="stretch")
    if customer_button:
        import streamlit as st

import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

#ข้อมูลลูกค้า

Customer_data = {}

colum = st.columns(4)

with colum[0]:
  manage_button = st.button("จัดการสินค้า",width="stretch")
  if manage_button:
    st.markdown("สวัสดี")

with colum[1]:
  stock_button = st.button("เช็คจำนวนสินค้า",width="stretch")
with colum[2]:
  calculate_button = st.button("คำนวณยอดขายสินค้า",width="stretch")
with colum[3]:
  customer_button = st.button("จัดการข้อมูลลูกค้า",width="stretch")
  if customer_button:
    name = st.text_input("ชื่อ-นามสกุล")
    
    age = st.number_input(
    "อายุ",
    min_value=1,
    max_value=100,
    value=18
    )
    gender = st.selectbox(
    "เพศ",
    ["Male", "Female"]
    )


        





