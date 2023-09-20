from flask import Flask, render_template, request, url_for, redirect
from pgm.db import get_meating, get_proposal, get_stats, get_rq, put_pop

app = Flask(__name__)
br = 'around.html'
mytop = 'mytop.html'
tbl = 'meetings.html'
nfo = 'proposals.html'
lst = 'stats.html'
sts = 'RQ.html'


@app.route('/around.html')
def around():
    return render_template('around.html')


@app.route('/mytop.html')
def home():
    return render_template('mytop.html')


@app.route('/meetings.html')
def meetings():
    return render_template('meetings.html', meeting=get_meating())


@app.route('/proposals.html')
def proposals():
    return render_template('proposals.html', proposal=get_proposal())


@app.route('/stats.html')
def stats():
    return render_template('stats.html', stats=get_stats())


@app.route('/RQ.html', methods=('GET', 'POST'))
def RQ():
    return render_template('RQ.html', rq=get_rq())


@app.route('/')
def frame():
    return render_template('frame.html', src_b=br, src=mytop, src_1=tbl, src_2=nfo, src_3=sts, src_4=lst)


@app.route('/meeting/add')
def addmeat():
    a = request.form['content']
    b = request.form['content']
    c = request.form['content']
    return render_template('addproposal.html', rq=put_pop(a,b,c))


if __name__ == '__main__':
    app.run()
