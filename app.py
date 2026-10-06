import streamlit as st

st.title("ระบบจัดการหลังร้านค้า", width="stretch", text_alignment="center", wrap=True)

colum = st.columns(4)

#ข้อมูลลูกค้า

def customer_search(): #ฟังค์ชันการหาชื่อลูก

    name_customer = st.text_input(
        "ค้นหาชื่อลูกค้า",
        type="search"
    )

    matches = [] #สร้าง list เปล่าเพื่อที่เราจะได้เอาข้อมูลที่ค้นหามา show

    for customer_id, customer in customer_data.items(): #หาข้อมูลจากใน list ทั้งหมด

        if name_customer.lower() in customer["Customer Name"].lower():

            matches.append({ 
                "Customer ID": customer_id,
                "Customer Name": customer["Customer Name"],
                "Age": customer["age"],
                "Gender": customer["Gender"],
                "Total Spend": customer["Total Spend"]
            }) #อันนี้แหละที่เอาไปใส่ใน list เปล่า

    if matches:
        st.dataframe(
            matches,
            hide_index=True
        ) #อันนี้ จะสร้าง ตารางไม่มีไร
    elif name_customer:
        st.warning("ไม่พบข้อมูลลูกค้า")


def customer_add():

    st.subheader("เพิ่มข้อมูลลูกค้า")

    name = st.text_input("ชื่อ-นามสกุล")
    age = st.number_input("อายุ")
    gender = st.text_input("เพศ")

    if st.button("เพิ่มลูกค้า"):

        # สร้าง ID ใหม่
        new_id = str(max(map(int, customer_data.keys())) + 1)

        # เพิ่มข้อมูลลง Dictionary
        customer_data[new_id] = {
            "Customer Name": name,
            "age": age,
            "Gender": gender,
            "Total Spend": 0
        }

        st.success(f"เพิ่มลูกค้า {name} สำเร็จ")


customer_data = {
    '101' : {
        'Customer Name' : 'John Doe',
        'age' : 32 ,
        'Gender' : 'Male' ,
        'Total Spend' : 2500
    },
}



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
  st.header("จัดการสินค้า")
  name = st.text_input("ชื่อ-นามสกุล")
elif st.session_state.get("menu") == "เช็คจำนวนสินค้า":
  st.header("เช็คจำนวนสินค้า")
  name = st.text_input("ชื่อ-นามสกุล")
elif st.session_state.get("menu") == "คำนวณยอดขายสินค้า":
  st.header("Calculate")
  name = st.text_input("ชื่อ-นามสกุล")
elif st.session_state.get("menu") == "ลูกค้า":
  st.header("จัดการข้อมูลลูกค้า")
  customer_add()

  
