import streamlit as st
import pandas as pd
import os

# Thiết lập cấu hình trang
st.set_page_config(page_title="Cửa Hàng Quần Áo Thời Trang", page_icon="👗", layout="wide")

# CSS tùy chỉnh
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
    }
    .product-card {
        background-color: white;
        padding: 15px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    .product-card img {
        max-width: 100%;
        height: auto;
        border-radius: 5px;
    }
    .product-title {
        font-size: 1.5em;
        color: #343a40;
        margin-bottom: 10px;
    }
    .price {
        color: #e44d26;
        font-weight: bold;
        font-size: 1.2em;
    }
    .cart-table {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #28a745;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #218838;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề ứng dụng
st.markdown("<h1 style='text-align: center; color: #343a40;'>Cửa Hàng Quần Áo Thời Trang</h1>", unsafe_allow_html=True)

# Dữ liệu mẫu cho sản phẩm
products = {
    "Tên sản phẩm": ["Áo thun nam", "Quần jeans nữ", "Váy maxi", "Áo sơ mi công sở"],
    "Giá (VND)": [150000, 350000, 450000, 250000],
    "Mô tả": [
        "Áo thun cotton thoáng mát, phong cách trẻ trung",
        "Quần jeans ống suông thời trang, chất liệu bền",
        "Váy maxi hoa nhẹ nhàng, phù hợp dạo phố",
        "Áo sơ mi trắng thanh lịch, thích hợp công sở"
    ],
    "Hình ảnh": [
        "images/tshirt.jpg",
        "images/jeans.jpg",
        "images/maxi.jpg",
        "images/shirt.jpg"
    ]
}
df_products = pd.DataFrame(products)

# Hiển thị danh sách sản phẩm
st.subheader("Danh sách sản phẩm")
cols = st.columns(4)  # Hiển thị 4 sản phẩm trên 1 hàng
for idx, row in df_products.iterrows():
    with cols[idx % 4]:
        st.markdown(f"""
            <div class='product-card'>
                <img src='{row['Hình ảnh']}' alt='{row['Tên sản phẩm']}' width='200'>
                <div class='product-title'>{row['Tên sản phẩm']}</div>
                <div>{row['Mô tả']}</div>
                <div class='price'>{row['Giá (VND)']:,} VND</div>
            </div>
        """, unsafe_allow_html=True)

# Khởi tạo giỏ hàng trong session state
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Form để thêm sản phẩm vào giỏ hàng
st.subheader("Thêm vào giỏ hàng")
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        selected_product = st.selectbox("Chọn sản phẩm", df_products["Tên sản phẩm"])
    with col2:
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
    st.markdown("<div class='cart-table'>", unsafe_allow_html=True)
    st.dataframe(cart_df, use_container_width=True)
    total = cart_df["Giá (VND)"].sum()
    st.markdown(f"<h3 style='text-align: right;'>Tổng tiền: {total:,} VND</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.write("Giỏ hàng trống.")
