# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

title = """
------------------------------------------------------------------------------------
                    ■  ■■■■■■   ■■■■■■■■■■ 
                    ■  ■    ■■      ■    ■ 
                    ■  ■     ■ ■■■■■■■■■■■■
                    ■  ■     ■     ■     ■ 
                    ■  ■    ■■  ■■■■■■■■■■ 
                    ■  ■■■■■■     ■■       
                    ■  ■          ■■■■■■■■ 
                    ■  ■         ■■      ■ 
                    ■  ■        ■ ■      ■ 
                    ■  ■       ■  ■      ■ 
                                  ■■■■■■■■ 
                                  ■      ■      Ver. Python
------------------------------------------------------------------------------------
"""

print(title)

print("IPアドレスを取得しています...")

# -----IPアドレスの取得-----

# IP取得用URLの設定
url = "http://53.u29.xyz/get-ip.php"
# URLにアクセスする
html = urllib.request.urlopen(url)
# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, 'html.parser')
# 取得したIPアドレスをString型にしておく
ip_address = str(soup)

# -----IPアドレスの取得終了-----

# htmlのソースを出力
print("あなたのIPアドレス: " + ip_address)