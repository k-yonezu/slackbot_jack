# coding: utf-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

# SlackのAPIを利用するためのトークン
# Botの設定ページから「OAuth & Permissions」のページに遷移し、
# 「Bot User OAuth Access Token」をコピーして貼り付ける
API_TOKEN = os.getenv("API_TOKEN")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "ウキ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
