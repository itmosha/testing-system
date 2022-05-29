from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3
import os
import subprocess

app = Flask('my_first_server')
DB_NAME = 'messages.db'

def init_wall_data():
    conn = sqlite3.connect(DB_NAME)
    conn.execute('''create table if not exists wall (
            id INTEGER PRIMARY KEY,
            nick TEXT,
            message TEXT,
            run_result TEXT)''')
    conn.commit()

def set_wall_data(nick, message, run_result):

    # add new message to the table

    conn = sqlite3.connect(DB_NAME)
    conn.execute('insert into wall(nick, message, run_result) values(?, ?, ?)', (nick, message, run_result))
    conn.commit()

def get_wall_data():

    # get all data from the table

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute('select nick, message, run_result from wall')
    rows = cursor.fetchall()
    return rows

def render_main_page():

    # filling the template

    wall_data = get_wall_data()
    return render_template("index.html",
            len=len(wall_data), wall_data=wall_data)


@app.route('/wall', methods=['POST'])
def response():

    # take data from user, fill the table with it and return the new page

    nick = request.form.get("nick")
    message = request.form.get("message")

    code_text = str(message)
    print(code_text)

    check1, check2 = code_text.find('system'), code_text.find('import os')

    if (check1 != -1 or check2 != -1):
        print("!!!!!")
        set_wall_data(nick, message, 'System commands are not allowed')
        return redirect("/", code=302)

    file = open("code.cpp", 'w')
    file.write(message)
    file.close()

    process = subprocess.Popen(['g++', 'code.cpp'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if (stderr != b''):
        print(f'Error: {stderr}')
        set_wall_data(nick, message, stderr)
        return redirect("/", code=302)

    process = subprocess.Popen(['./a.out'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    result = str(stdout)[2:-1]

    result = 'no output' if result == '' else result

    set_wall_data(nick, message, result)
    print(f'Run result: {result}')
    return redirect("/", code=302)

@app.route('/')
def handle_time():
    return render_main_page()

if __name__ == '__main__':
    init_wall_data()
    app.run(host='0.0.0.0',port=5000)