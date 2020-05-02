@app.route('/index.html')
def index():
    with open("index.html") as f:
        html = f.read()
    return html

@app.route('/data.html')
def data():
    with open("data.html") as f:
        html = f.read()
    return html

@app.route('/acks.html')
def acks():
    with open("acks.html") as f:
        html = f.read()
    return html

@app.route('/results.html')
def acks():
    with open("results.html") as f:
        html = f.read()
    return html

@app.route('/before.html')
def acks():
    with open("before.html") as f:
        html = f.read()
    return html

@app.route('/after.html')
def acks():
    with open("after.html") as f:
        html = f.read()
    return html
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0") # don't change this line!