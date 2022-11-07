from flask import request, Flask

app = Flask(__name__)

@app.route('/reserva', methods = ['POST'])
def foo():
    data = request.form
    return data

if __name__ == '__main__':
    app.run(debug = True)
