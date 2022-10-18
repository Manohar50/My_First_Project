import sqlite3
import requests
import streamlit as st

# To connect to sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()


# Routine for Animation to play
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#  All routines for TodoList - tasktable
def view_all_tdata():
    cur.execute('SELECT * FROM taskstable')
    data = cur.fetchall()
    return data


def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE)')


def add_data(task, task_status, task_due_date):
    cur.execute('INSERT INTO taskstable(task, task_status, task_due_date) VALUES (?, ?, ?)',
                (task, task_status, task_due_date))
    conn.commit()


def view_all_data():
    cur.execute('SELECT * FROM taskstable')
    data = cur.fetchall()
    return data


def view_all_task_names():
    cur.execute('SELECT DISTINCT task FROM taskstable')
    data = cur.fetchall()
    return data


def get_task(task):
    cur.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
    data = cur.fetchall()
    return data


def get_task_by_status(task_status):
    cur.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
    data = cur.fetchall()


def edit_task_data(new_task, new_task_status, new_task_date, task, task_status, task_due_date):
    cur.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? "
                "WHERE task=? and task_status=? and task_due_date=? ",
                (new_task, new_task_status, new_task_date, task, task_status, task_due_date))
    conn.commit()
    data = cur.fetchall()
    return data


def delete_tdata(task):
    cur.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
    conn.commit()


# All routines for VideoTutorial -v_table
def add_vdata(n, v, d):
    cur.execute(""" CREATE TABLE IF NOT EXISTS v_table(NAME TEXT,V_LINK TEXT,DATE TEXT);""")
    cur.execute("INSERT INTO v_table VALUES(?,?,?)", (n, v, d))
    conn.commit()
    # conn.close()
    st.success("Successfully Submitted")


def delete_vdata(name):
    cur.execute('DELETE FROM  v_table WHERE NAME="{}"'.format(name))
    conn.commit()


def view_all_names():
    cur.execute('SELECT * FROM v_table')
    data = cur.fetchall()
    return data


def play_data(vlink):
    cur.execute('SELECT DISTINCT V_LINK FROM  v_table WHERE V_LINK="{}"'.format(vlink))
    # data = '"{}"'.format(V_LINK)
    conn.commit()


def update_vdata(new_name, new_vlink, new_date, name):
    cur.execute("UPDATE v_table SET NAME=?,V_LINK=?, DATE=?  WHERE NAME=? ", (new_name, new_vlink, new_date, name))
    conn.commit()


def view_all_vdata():
    cur.execute('SELECT * FROM v_table')
    data = cur.fetchall()
    return data


def get_name(name):
    cur.execute('SELECT * FROM v_table WHERE NAME="{}"'.format(name))
    data = cur.fetchall()
    return data


# All routines for Docs Tutorial d_table
def view_all_dnames():
    cur.execute('SELECT DISTINCT NAME FROM d_table')
    data = cur.fetchall()
    return data


def update_ddata(new_name, new_d_link, new_date, name):
    cur.execute("UPDATE d_table SET NAME=?,D_LINK=?, DATE=?  WHERE NAME=? ", (new_name, new_d_link, new_date, name))
    conn.commit()


def view_all_ddata():
    cur.execute('SELECT * FROM d_table')
    data = cur.fetchall()
    return data


def addData(na, do, da):
    cur.execute(""" CREATE TABLE IF NOT EXISTS d_table(NAME TEXT,D_LINK TEXT,DATE TEXT);""")
    cur.execute("INSERT INTO d_table VALUES(?,?,?)", (na, do, da))
    conn.commit()
    st.success("Successfully Submitted")


def delete_data(name):
    cur.execute('DELETE FROM  d_table WHERE NAME="{}"'.format(name))
    conn.commit()


def get_dname(name):
    cur.execute('SELECT * FROM d_table WHERE NAME="{}"'.format(name))
    data = cur.fetchall()
    return data
