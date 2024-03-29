# django_api  
WebAPIを試すだけのDjango用プロジェクト  
![top](https://user-images.githubusercontent.com/58038726/69896664-507a6c80-1385-11ea-848f-d8146b14c619.png)  
  
Windows10向け  
※その他OSは動作未確認(たぶん動く)  
  
## 目次  
- 導入手順  
- 起動方法  
- 確認方法  
- 処理の概要  
  
## 導入手順  
__python3.xのインストール__  
python(バージョンは3以上)をインストールしてください。  
参考：https://www.python.jp/install/windows/install_py3.html  
  
__pythonとpipコマンドの環境変数設定__  
コマンドプロンプトで「python」や「pip」を実行できるよう設定してください。  
参考：https://www.javadrive.jp/python/install/index3.html  
  
__Djangoライブラリのインストール__  
djangoライブラリをインストールしてください。
```cmd  
pip install django  
```  
  
__本ソースコードのダウンロード__  
ローカル環境の好きな場所にダウンロードしてください。  
```cmd  
git clone https://github.com/mikenomist/django_api.git  
```  
  
## 起動方法  
__ディレクトリ移動__  
ダウンロードしたソースコードのディレクトリまで移動してください。
```cmd  
cd ディレクトリパス\django_api  
```  
  
__デバッグモード起動__  
Djangoのデバッグモードを使って自PCを仮想サーバとして起動します。
```cmd  
python manage.py runserver  
```  
![runserver](https://user-images.githubusercontent.com/58038726/69896612-e6fa5e00-1384-11ea-994d-34d9a598b375.png)  
  
## 確認方法  
__ブラウザへのアクセス__  
好きなブラウザ(Chrome推奨)を開いて http://127.0.0.1:8000/ にアクセスします。  
「送信」ボタンを押下して数字が変わったら成功。  
__APIの実行__  
コマンドプロンプトでcurlコマンドやpythonでリクエストを投げて正常に返ってくれば成功。  
```cmd  
curl http://127.0.0.1:8000/api/count/  
```  
![curl](https://user-images.githubusercontent.com/58038726/69896978-c8966180-1388-11ea-98ef-bfa35d662a3c.png)  

## 処理の概要  
画面上処理：「送信」ボタンを押すことを検知すると、jQueryのAjaxを使って http://127.0.0.1:8000/api/count/ へアクセスする  
↓  
サーバ側処理：リクエストがあればその都度、数字をランダムに生成してレスポンスする  
↓  
画面上処理：レスポンスを受け取ると、数字の記載場所に受け取った数字になるまで数値を0から1ずつ足していく  
![django_api_flow](https://user-images.githubusercontent.com/58038726/69896646-21fc9180-1385-11ea-9eb8-c52622658635.png)  
