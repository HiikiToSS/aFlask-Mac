from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lmaoWhatAPassword'

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
        if len(request.form['username'])>2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
        print(request.form)
    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.route('/info')
def info():
    return render_template('info.html', title='Информация', menu=menu)


@app.errorhandler(404)
def NotFound(error):
    return render_template('page404.html', title='Такой страницы нет', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)