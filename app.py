from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')


@app.route('/registro')
def resgistro():
    return render_template('sitio/pages/resgistro.html')


@app.route('/list')
def list():
    return render_template('sitio/pages/lista.html')



@app.route('/update')
def updete():
    return render_template('sitio/pages/update.html')

@app.route('/deleter')
def deleter():
    render_template('sitio/pages/deleter.html')


if __name__ =='__main__':
    app.run(debug=True)
