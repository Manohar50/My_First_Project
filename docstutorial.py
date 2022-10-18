# WebProjects\streamlit-multiapps\docstutorial.py
import pandas as pd
from streamlit_lottie import st_lottie
import streamlit.components.v1 as stc
from db_funcn import *

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:8px;border-radius:8px">
    <h1 style="color:white;text-align:center;">Tutorial Studies: Docs</h1>
    <p style="color:white;text-align:center;">Built with Python & Streamlit</p>
    </div>
    """

lottie_reading = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_wqypnpu5.json")


def app():
    menu = ["Create", "Read",  "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    with st.container():
        left_column, right_column = st.columns(2)
        with right_column:
            st_lottie(lottie_reading, height=150, key="Video-coding")
        with left_column:
            stc.html(HTML_BANNER)
            st.subheader("Organize Tutorial [CRUD]")

    if choice == "Read":
        st.text(" Select Doc's  ")
        # with st.expander("View All"):
        result = view_all_ddata()
        clean_df = pd.DataFrame(result, columns=["Name", "D_Link", "Date"])
        st.dataframe(clean_df)

        unique_list = [i[1] for i in view_all_ddata()]
        dlink = st.selectbox("Select to Read", unique_list)
        btn = st.button("Click To Read")
        if btn:
            st.markdown("Playing: '{}'".format(dlink))

    elif choice == "View":
        st.text("View All Doc's")
        with st.expander("View All"):
            result = view_all_ddata()
            clean_df = pd.DataFrame(result, columns=["Name", "d_Link", "Date"])
            st.dataframe(clean_df)

    elif choice == "Create":
        st.write("this s a form")
        with st.form(key="Information form"):
            name = st.text_input("Enter your Name:")
            d_link = st.text_input("Docs url Link:")
            date = st.date_input("Date:")
            submission = st.form_submit_button(label="submit")
            if submission:
                addData(name, d_link, date)

    elif choice == "Update":
        st.text("View All Data")
        # with st.expander("Current Data"):
        result = view_all_ddata()
        # st.write(result)
        clean_df = pd.DataFrame(result, columns=["Name", "Url-Links", "Date"])
        st.dataframe(clean_df)

        list_of_data = [i[0] for i in view_all_dnames()]
        selected_name = st.selectbox("Select To Update", list_of_data)
        raw_result = get_dname(selected_name)

        if raw_result:
            name = raw_result[0][0]
            d_link = raw_result[0][1]
            date = raw_result[0][2]

            new_name = st.text_input("Name:", name)
            new_d_link = st.text_input("Url_Link:", d_link)
            new_date = st.date_input(date)

        if st.button("Update Data"):
            update_ddata(new_name, new_d_link, new_date, name)
            # st.success("Updated ")
            st.success("Updated ::{} ::To {}".format( new_name,name,))

        with st.expander("Updated Data"):
            result = view_all_ddata()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Name", "Url Links", "Date"])
            st.dataframe(clean_df)

    elif choice == "Delete":
        st.text("Select View All Data For Delete")
        with st.expander("View All"):
            result = view_all_ddata()
            clean_df = pd.DataFrame(result, columns=["Name", "D-Url Link", "Date"])
            st.dataframe(clean_df)
            unique_list = [i[0] for i in view_all_ddata()]
            delete_by_Name = st.selectbox("Select Name", unique_list)

        if st.button("Delete"):
            delete_data(delete_by_Name)
            st.warning("Deleted: '{}'".format(delete_by_Name))

        with st.expander("Updated Data"):
            result = view_all_ddata()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Name", "Url Links", "Date"])
            st.dataframe(clean_df)


if __name__ == '__main__':
    app()
