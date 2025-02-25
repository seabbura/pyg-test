# 必要なライブラリをインポート
import streamlit as st
import pandas as pd
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer
from streamlit.components.v1 import html

# ページ設定を使用して幅を最大化
st.set_page_config(
    page_title="くそ雑得点可視化ツール",
    layout="wide"
)

# ページタイトルの設定
st.title('くそ雑得点可視化ツール')
st.write('2025年選手名鑑より')

# CSVファイルの読み込み
try:
    df = pd.read_csv('data/meikan_runs.csv')
except Exception as e:
    st.error(f'CSVファイルの読み込みに失敗しました: {e}')
    st.stop()  # エラーがあれば処理を停止

# pygwalkerをStreamlitで使用する
st.write('勝手にいじれます')

# ここで pyg_html を定義
pyg_html = pyg.to_html(df)

# pyg_html をカスタムの div でラップして html() に渡す
container_html = f"""
<div class="my-custom-container">
  {pyg_html}
</div>
"""

html(container_html, height=900, width=1100)
