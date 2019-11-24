import flask
from flask import render_template
import pickle
import sklearn

def mypredict(model):
    with open(f'{model}.pkl', 'rb') as fh:
        loaded_model = pickle.load(fh)
    exp = float(flask.request.form['temperature'])
    return loaded_model.predict([ [exp] ])

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html' )

    if flask.request.method == 'POST':

        line_pack=round(mypredict('Line_pack')[0]/1000,2)
        pao_prod=round(mypredict('Production_PAO')[0]/1000,2)
        UGS_out=round(mypredict('UGS_out')[0]/1000,2)
        UGS_in=round(mypredict('UGS_in')[0]/1000,2)

        return render_template('main.html', line_pack = line_pack, pao_prod=pao_prod, UGS_out=UGS_out, UGS_in=UGS_in   )

if __name__ == '__main__':
    app.run()