from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import dailynews

app = Flask(__name__)

@app.route('/')
def index():
    title = "記事一覧"
    return render_template('index.html',title=title)

@app.route('/update', methods=['GET'])
def update():
    title = "新着記事一覧"
    itpro_articles = dailynews.ITpro.get_new_article()
    gigazine_articles = dailynews.GIGAZINE.get_content()
    cnet_articles = dailynews.CNETJapan.get_new_article()
    if request.method == 'GET':
        return render_template('index.html',
                                title = title,
                                itpro_articles=itpro_articles,
                                gigazine_articles=gigazine_articles,
                                cnet_articles=cnet_articles)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0',port = 5555)
