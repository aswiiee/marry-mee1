import streamlit as st

st.set_page_config(page_title="For You ❤️", layout="centered")

# Hide Streamlit menu/footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize state
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.image("photo.jpg", use_column_width=True)

    st.markdown(
        "<h2 style='text-align:center; color:#d81b60;'>Sanvi are you Thadichi 💖</h2>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes ❤️"):
            st.session_state.page = 2
            st.rerun()

    with col2:
        st.button("No 😢")  # can't move button in Streamlit

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.image("photo.jpg", use_column_width=True)

    st.markdown(
        "<h1 style='text-align:center; color:#e91e63;'>i love you shuttumani ❤️</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Ante kuttyne njn mind akkathe alla busy ayi povunne konda 💭</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center;'>Ante kutty anik nalla ishta ❤️</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center;'>LOVE YOU SANNNN!! 😍🔥</p>",
        unsafe_allow_html=True
    )