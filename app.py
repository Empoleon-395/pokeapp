from crypt import methods
from flask import Flask, request,render_template
from pokem import plot_poke
import pandas as pd
df = pd.read_csv("./data/poke_info.csv")

app = Flask(__name__, static_folder='templates')
a = plot_poke(filename = "./templates/imgs/output.png")
languages = list(df["name_h"])
img_path = "./templates/imgs/output.png"
@app.route('/',methods = ['GET', 'POST'])
def search():
    if request.method == 'post':
        nn = df[df["name_h"]==str(request.form['name'])].reset_index(drop = True).loc[0]["name"]
        ff = df[df["name_h"]==str(request.form['name'])].reset_index(drop = True).loc[0]["form"]
        print([nn,ff])
        a.run(str(nn),str(ff))
        print(request.method)
        return render_template("index.html",languages=languages, image_path = img_path,title = "Home")
    else:
        try:
            nn = df[df["name_h"]==str(request.form['name'])].reset_index(drop = True).loc[0]["name"]
            ff = df[df["name_h"]==str(request.form['name'])].reset_index(drop = True).loc[0]["form"]
            print([nn,ff])
            a.run(str(nn),str(ff))
            print(str(request.method))
            return render_template("index.html" ,languages=languages,image_path = img_path,title = "Home")
        except:
            return render_template("index2.html" ,languages=languages,image_path = img_path,title = "Home")

if __name__ == "__main__":
    app.run(port = 8000, debug=True)