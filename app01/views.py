# -*- coding:utf8 -*-
from app01 import app
from flask import render_template,request
import paramiko


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("Metro/base.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/user')
def user():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('bootstrap3/user.html', title='User', user=user)


@app.route('/cmd')
def ssh_command():
    ip = request.args.get('ip')
    user = request.args.get('user')
    passwd = request.args.get('passwd')
    command = request.args.get('command')
    port = int(request.args.get('port'))
    print ip,user,passwd,command,port
    pkey = 'app01/vps'
    key = paramiko.RSAKey.from_private_key_file(pkey,password='')
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=user, password=passwd,port=port, pkey=key)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    if result == '':
        result = stderr.read()
    return render_template('bootstrap3/index.html', results=result.split('\n'), title='User', user=user)



@app.route('/login')
def login():
    return render_template('Metro/login.html')


@app.route('/buttons')
def buttons():
    return render_template('bootstrap3/buttons.html')


@app.route('/form')
def form():
    return render_template('Metro/form.html')


@app.route('/calendar')
def calendar():
    return render_template('Metro/calendar.html')

@app.route('/editors')
def editors():
    return render_template('bootstrap3/editors.html')


@app.route('/tables')
def tables():
    return render_template('Metro/table.html')

@app.route('/interface')
def interface():
    return render_template('bootstrap3/interface.html')

@app.route('/stats')
def stats():
    return render_template('bootstrap3/stats.html')


@app.route('/chart')
def chart():
    return render_template('Metro/chart.html')

@app.route('/file_manager')
def file_manager():
    return render_template('Metro/file-manager.html')

@app.route('/gallery')
def gallery():
    return  render_template('Metro/gallery.html')

@app.route('/messages')
def messages():
    return  render_template('Metro/messages.html')

@app.route('/tasks')
def tasks():
    return  render_template('Metro/tasks.html')

@app.route('/icon')
def icon():
    return  render_template('Metro/icon.html')

@app.route('/submenu')
def submenu():
    return  render_template('Metro/submenu.html')

@app.route('/submenu2')
def submenu2():
    return  render_template('Metro/submenu2.html')

@app.route('/submenu3')
def submenu3():
    return  render_template('Metro/submenu3.html')

@app.route('/typography')
def typography():
    return  render_template('Metro/typography.html')

@app.route('/ui')
def ui():
    return  render_template('Metro/ui.html')

@app.route('/widgets')
def widgets():
    return  render_template('Metro/widgets.html')


import random
@app.route('/testapi')
def testapi():
    num =   random.randint(0, 100)
    print num
    return  str(num)

@app.route('/test')
def test():

    return  render_template('test.html')