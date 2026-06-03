import streamlit as st

def main():
    st.title("测试应用")
    st.write("Streamlit 测试成功！")
    
    if st.button("点击我"):
        st.success("按钮点击成功！")

if __name__ == "__main__":
    main()
