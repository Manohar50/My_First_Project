# todolist.py
import pandas as pd
from db_funcn import *
import streamlit.components.v1 as stc
from streamlit_lottie import st_lottie
import plotly.express as px


lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_3rwasyjy.json")

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:8px;border-radius:8px">
    <h1 style="color:white;text-align:center;">Todo List for Tutorial</h1>
    <p style="color:white;text-align:center;">Built with Python & Streamlit</p>
    </div>
    """


def app():
    with st.container():
        left_column, right_column = st.columns(2)
    with right_column:
        st_lottie(lottie_coding, height=150, key="coding-boy")
    with left_column:
        stc.html(HTML_BANNER)
        st.subheader("Organize ToDo List [CRUD]")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    # createV_table()

    if choice == "Create":
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Add Task With The Selected Status & Date")

        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"])
            task_due_date = st.date_input("Date")

        if st.button("Add Task"):
            add_data(task, task_status, task_due_date)
            st.success("Added ::{} ::To Task".format(task))

    elif choice == "Read":
        st.text("View All Data")
        # with st.expander("View All"):
        result = view_all_tdata()
        # st.write(result)
        clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
        st.dataframe(clean_df)

        with st.expander("Task Status"):
            task_df = clean_df['Status'].value_counts().to_frame()
            # st.dataframe(task_df)
            task_df = task_df.reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df, names='index', values='Status')
            st.plotly_chart(p1, use_container_width=True)

    elif choice == "Update":
        st.text("Update Data")

        with st.expander("Current Data"):
            result = view_all_tdata()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(clean_df)

            list_of_tasks = [i[0] for i in view_all_task_names()]
            selected_task = st.selectbox("Select Update Task", list_of_tasks)
            task_result = get_task(selected_task)
            # st.write(task_result)

        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_due_date = task_result[0][2]

            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do", task)

            with col2:
                new_task_status = st.selectbox(task_status, ["ToDo", "Doing", "Done"])
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
                edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
                st.success("Updated ::{} ::To {}".format(task, new_task))

            with st.expander("View Updated Task"):
                result = view_all_tdata()
                # st.write(result)
                clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
                st.dataframe(clean_df)

    elif choice == "Delete":
        st.write("Delete Task")
        # with st.expander("View Data"):
        result = view_all_tdata()
        # st.write(result)
        clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
        st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Select Delete Task", unique_list)
        if st.button("Delete"):
            delete_tdata(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

        with st.expander("Updated Task"):
            result = view_all_tdata()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(clean_df)

    else:
        st.subheader("About")
        st.write("Organizing Study Planing")
        st.text("Built with Python - Streamlit")
        st.text("By Mano har ")


if __name__ == '__main__':
    app()
