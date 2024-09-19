from flask import Flask,render_template
from recomand import Recomander

app = Flask(__name__)
recom = Recomander()
@app.route('/')
def hello():
    return render_template('index.html',movie=recom.get_title(),recomand=recom.get_top_recomand())
@app.route('/<title>')
def get_title(title):
    l = recom.get_recomandation(title)
    return render_template('title.html',split=l)

if __name__ == '__main__':
    app.run(debug=True,port=1234)