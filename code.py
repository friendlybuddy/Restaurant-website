import streamlit as st

# 1. Page Configuration (The tab title and icon)
st.set_page_config(page_title="The Cyprus Grill", page_icon="🍴", layout="wide")

# 2. Hero Section (The first thing people see)
st.title("🔥 The Cyprus Grill")
st.subheader("Authentic Mediterranean Flavors in the Heart of the Island")
st.write("---")

# 3. Create Columns for a professional layout
col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800", caption="Our Cozy Atmosphere")

with col2:
    st.header("Our Story")
    st.write("""
    Founded in 2024, we bring the freshest local ingredients to your table. 
    From traditional Meze to modern twists on Cypriot classics, 
    every dish is prepared with passion.
    """)
    st.button("Book a Table Now")

# 4. Menu Section (Using a simple Data structure)
st.write("---")
st.header("🍴 Our Signature Menu")

menu_col1, menu_col2 = st.columns(2)

with menu_col1:
    st.markdown("### Starters")
    st.write("**Hellim Fries** - Crispy local halloumi with honey . . . 150 TL")
    st.write("**Classic Hummus** - Tahini, garlic, and lemon . . . 100 TL")

with menu_col2:
    st.markdown("### Main Courses")
    st.write("**Mix Kebab** - Lamb, chicken, and köfte . . . 450 TL")
    st.write("**Seafood Platter** - Catch of the day from Girne . . . 600 TL")

# 5. Contact & Location (Essential for North Cyprus businesses)
st.write("---")
st.header("📍 Find Us")
st.write("Address: 123 Blue Harbor Road, Girne, North Cyprus")
st.write("Phone: +90 533 000 00 00")

# Simple Contact Form
with st.expander("Send us a Message"):
    name = st.text_input("Name")
    msg = st.text_area("How can we help?")
    if st.button("Submit"):
        st.success(f"Thank you {name}, we'll get back to you soon!")
        