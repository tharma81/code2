from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Pattern Matching Function
def function1(txt, pat, m, n):
    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

@app.route('/', methods=['GET', 'POST'])
def index():

    result = None
    txt_length = 0
    pat_length = 0
    execution_time = 0

    if request.method == 'POST':

        # Get text and pattern from form
        txt = request.form['text']
        pat = request.form['pattern']

        stime = time.time()

        time.sleep(1)

        result = function1(txt, pat, len(txt), len(pat))

        etime = time.time()

        txt_length = len(txt)
        pat_length = len(pat)

        execution_time = etime - stime - 1

    return render_template(
        'index.html',
        result=result,
        txt_length=txt_length,
        pat_length=pat_length,
        execution_time=execution_time
    )

if __name__ == '__main__':
    app.run(debug=True)