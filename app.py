import streamlit as st

st.title("🛒 ระบบจัดการร้านค้า")

menu = st.sidebar.selectbox(
    "เมนู",
    ["สินค้า", "ขายสินค้า", "ยอดขาย", "วิเคราะห์ข้อมูล"]
)

if menu == "สินค้า":
    st.header("📦 จัดการสินค้า")

elif menu == "ขายสินค้า":
    st.header("🛍️ ขายสินค้า")

elif menu == "ยอดขาย":
    st.header("💰 ยอดขาย")

elif menu == "วิเคราะห์ข้อมูล":
    st.header("📊 วิเคราะห์ยอดขาย")
