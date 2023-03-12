from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'name' : 'О сайте', 'url' : 'about'},
    {'name' : 'Обратная связь', 'url' : 'contact'},
    {'name' : 'Информация', 'url' : 'info'}
    ]

@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form)
    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.route('/info')
def info():
    return render_template('info.html', title='Информация', menu=menu)

@app.route('/aaa')
def info():
    return '''hihiASDASASD'''


if __name__ == '__main__':
    app.run(debug=True)