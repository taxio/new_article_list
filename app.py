# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import dailynews

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    title = "記事一覧"
    # index.html をレンダリングする
    return render_template('index.html',title=title)

@app.route('/update', methods=['GET'])
def update():
    title = "新着記事一覧"
    itpros = dailynews.ITpro.get_new_article()
    gigazines = dailynews.GIGAZINE.get_content()
    cnets = dailynews.CNETJapan.get_new_article()
    if request.method == 'GET':
        return render_template('index.html',title = title,itpros=itpros,gigazines=gigazines,cnets=cnets)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = False # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
