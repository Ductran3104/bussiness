import streamlit as st
import pandas as pd

# Tiêu đề ứng dụng
st.title("Cửa hàng quần áo trực tuyến")

# Dữ liệu mẫu cho sản phẩm
products = {
    "Tên sản phẩm": ["Áo thun nam", "Quần jeans nữ", "Váy maxi", "Áo sơ mi công sở"],
    "Giá (VND)": [150000, 350000, 450000, 250000],
    "Mô tả": [
        "Áo thun cotton thoáng mát",
        "Quần jeans ống suông thời trang",
        "Váy maxi hoa nhẹ nhàng",
        "Áo sơ mi trắng thanh lịch"
    ]
}
df_products = pd.DataFrame(products)

# Hiển thị danh sách sản phẩm
st.subheader("Danh sách sản phẩm")
st.dataframe(df_products)

# Khởi tạo giỏ hàng trong session state
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Form để thêm sản phẩm vào giỏ hàng
st.subheader("Thêm vào giỏ hàng")
selected_product = st.selectbox("Chọn sản phẩm", df_products["Tên sản phẩm"])
quantity = st.number_input("Số lượng", min_value=1, value=1)

if st.button("Thêm vào giỏ hàng"):
    price = df_products[df_products["Tên sản phẩm"] == selected_product]["Giá (VND)"].iloc[0]
    st.session_state.cart.append({
        "Tên sản phẩm": selected_product,
        "Số lượng": quantity,
        "Giá (VND)": price * quantity
    })
    st.success(f"Đã thêm {quantity} {selected_product} vào giỏ hàng!")

# Hiển thị giỏ hàng
st.subheader("Giỏ hàng của bạn")
if st.session_state.cart:
    cart_df = pd.DataFrame(st.session_state.cart)
    st.dataframe(cart_df)
    total = cart_df["Giá (VND)"].sum()
    st.write(f"Tổng tiền: {total:,} VND")
else:
    st.write("Giỏ hàng trống.")
