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
url = "http://53.u29.xyz/get-ip.php"
html = urllib.request.urlopen(url)  # URLにアクセスする
soup = BeautifulSoup(html, 'html.parser')       # htmlをBeautifulSoupで扱う
ip_address = str(soup)
# -----IPアドレスの取得終了-----

print("あなたのIPアドレス: " + ip_address)       # htmlのソースを出力