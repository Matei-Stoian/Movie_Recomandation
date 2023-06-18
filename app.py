from flask import Flask,render_template
from recomand import Recomander

app = Flask(__name__)
recom = Recomander()
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/<title>')
def get_title(title):
    l = recom.get_recomandation(title)
    l = l[:10]
    split = []
    for i in l:
        split.append(recom.title_from_index(i[0]))
    return render_template('title.html',split=split)

if __name__ == '__main__':
    app.run(debug=True,port=1234)