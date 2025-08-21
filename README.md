# 概要
Pygletでキーボード入力の制御を簡単にするモジュール\
Keyboadr_ModuleディレクトリにあるKeyboard_Module.pyがモジュール本体

# 前提環境
pyglet\
keyboard

# 使い方
先頭でインポート
```
from 【場所】 import Keyboard_Module
```
\
pyglet.window.Windowの直後に初期化
```
window = pyglet.window.Window(【縦】, 【横】)
keys = Keyboard_Module.Keyboard_Module(window, 【キーコードのリスト】)
```
\
キーコードのリストの例
```
["Q", "W", "E", "R", "T", "Y", "ENTER"]
```
\
pygletのupdate関数の先頭でUpdate関数を実行
```
def update(dt):
    keys.Update()
    ...
```
\
各状況で長押しされているフレーム数を以下で取得
```
keys.active(keys.GetIndex("【キーコード】"))     % アクティブ状態
keys.inactive(keys.GetIndex("【キーコード】"))   % 非アクティブ状態
keys.pressed(keys.GetIndex("【キーコード】"))    % アクティブ/非アクティブ 問わず
```
