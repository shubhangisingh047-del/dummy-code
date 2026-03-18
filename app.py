from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form_data = {}
    if request.method == 'POST':
        form_data = {
            'name': request.form.get('name'),
	    'journal_name': request.form.get('journal_name')
	}
    return render_template('index.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
