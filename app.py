import sqlite3
import subprocess

from parse import check_for_keywords
from compile_run import compile_cpp, run_cpp
from flask import Flask, render_template, request, redirect

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

    nick = request.form.get("nick")
    message = request.form.get("message")

    if check_for_keywords(str(message)):
        print('System commands are not allowed')
        set_wall_data(nick, message, 'System commands are not allowed')
        return redirect("/", code=302)

    compilation_result = compile_cpp(str(message))
    if compilation_result != 0:
        print('Didnt compile, error: ', compilation_result)
        set_wall_data(nick, message, compilation_result)
        return redirect("/", code=302)

    output = run_cpp()

    set_wall_data(nick, message, output)
    print(f'Run result: {output}')
    return redirect("/", code=302)

@app.route('/')
def handle_time():
    return render_main_page()

if __name__ == '__main__':
    init_wall_data()
    app.run(host='0.0.0.0',port=5000)