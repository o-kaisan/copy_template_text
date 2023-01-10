# copy template text
## 概要
templateディレクトリ配下にあるテキストファイルをテンプレートとして一覧表示し、選択したテンプレートの本文をクリップボードにコピーする

## テンプレート追加
※.txt以外は無視される
- templates配下にテキストファイルを追加する
- テキストファイルの本文にはテンプレートの本文を登録しておく

## テンプレートの呼び出し
- プログラムを実行
- 表示されるテンプレート一覧から「操作」したがってテンプレートを選択
- クリップボードにテンプレートの本文がコピーされる

## 操作
- テンプレートはキーボードの↑と↓で操作する
- テンプレートを選択する場合は「Enter」キーを押下
- アプリケーションを終了する場合は、「Ctrl + c」を押下

## 動作環境
- Windows
- python3.10

## パッケージインストール
```bash
pip install -r requirement.txt
```

## プログラム実行
```
python .\main.py
```