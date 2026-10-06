import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

def product_search(): #ค้นหา product
    query = st.text_input("Search products", type="search", live=True)
    matches = [
        p for p in products if query.lower() in p["Product"].lower()
    ]
    st.dataframe(matches, hide_index=True)

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

  



