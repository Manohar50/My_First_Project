# todolist.py
from db_funcn import *
import pandas as pd
from streamlit_lottie import st_lottie
import streamlit.components.v1 as stc

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:8px;border-radius:8px">
    <h1 style="color:white;text-align:center;">Tutorial Studies:Video </h1>
    <p style="color:white;text-align:center;">Built with Python & Streamlit</p>
    </div>
    """

lottie_video = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tno6cg2w.json")


def app():
    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)
    # createV_table()
    with st.container():
        left_column, right_column = st.columns(2)

    with right_column:
        st_lottie(lottie_video, height=150, key="Video-coding")
    with left_column:
        stc.html(HTML_BANNER)
        st.subheader("Organize Tutorial [CRUD]")

    if choice == "Read":
        st.text("View All Data")
        # with st.expander("View All"):
        result = view_all_vdata()
        clean_df = pd.DataFrame(result, columns=["Name", "Url-Link", "Date"])
        st.dataframe(clean_df)
        unique_list = [i[1] for i in view_all_vdata()]
        vlink = st.selectbox("Select to Play", unique_list)
        btn = st.button("Play")
        if btn:
            st.warning("Playing: '{}'".format(vlink))

    if choice == "Create":
        st.write("this s a form")
        with st.form(key="Information form"):
            name = st.text_input("Enter your Name:")
            v_link = st.text_input("Video url Link:")
            date = st.date_input("Date:")
            submission = st.form_submit_button(label="submit")
            if submission:
                add_vdata(name, v_link, date)
        st.write("Check to see it Added")
        with st.expander("Updated Data"):
            result = view_all_vdata()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Name", "Url Links", "Date"])
            st.dataframe(clean_df)

    elif choice == "Delete":
        st.text("View All Data")
        result = view_all_vdata()
        clean_df = pd.DataFrame(result, columns=["Name", "Url-Link", "Date"])
        st.dataframe(clean_df)
        unique_list = [i[0] for i in view_all_vdata()]
        delete_by_Name = st.selectbox("Select to Delete", unique_list)
        if st.button("Delete"):
            delete_vdata(delete_by_Name)
            st.warning("Deleted: '{}'".format(delete_by_Name))

        with st.expander("Updated Data"):
            result = view_all_vdata()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Name", "Url Links", "Date"])
            st.dataframe(clean_df)


    elif choice == "Update":
        st.text("View All Data")
        result = view_all_vdata()
        clean_df = pd.DataFrame(result, columns=["Name", "Url-Links", "Date"])
        st.dataframe(clean_df)

        list_of_data = [i[0] for i in view_all_names()]
        selected_name = st.selectbox("Select To Update", list_of_data)
        raw_result = get_name(selected_name)

        if raw_result:
            name = raw_result[0][0]
            v_link = raw_result[0][1]
            date = raw_result[0][2]

            new_name = st.text_input("Name:", name)
            new_vlink = st.text_input("Url_Link:", v_link)
            new_date = st.date_input(date)

        if st.button("Update Task"):
            update_vdata(new_name, new_vlink, new_date, name)
            # st.success("Updated ")
            st.success("Updated ::{} ::To {}".format(new_name, name, ))

        with st.expander("Updated Data"):
            result = view_all_vdata()
            clean_df = pd.DataFrame(result, columns=["Name", "Url Links", "Date"])
            st.dataframe(clean_df)


if __name__ == '__main__':
    app()
