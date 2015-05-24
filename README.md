# Requirements
Python3 + Django + Selenium + etc... 環境の構築

```
cd ${INSTALL_DIRECTORY}
pyenv virtualenv --python=python3 3.4.2 tddpy-dev
pyenv local tddpy-dev
pip3 install -r requirements.txt
pip3 install -r test_requirements.txt
```


# Vagrant with Digital Ocean
デプロイで参照するリモートブランチを作成し、インスタンスを起動する。

```
git remote add {HTTPS_URL}
vagrant up --provider=digital_ocean --provision
```

起動後はブラウザでサーバにアクセスするか、
sshコマンドでログインする。

```
vagrant ssh
```


# Run tests
テストを実行する

```
make test                  # Run all tests
```

個々のテストを実行する
```
make unit-test             # Run unit tests
make unit-test-js          # Run unit tests corresponding to JavaScript
make functional-test       # Run functional tests
```


# Run local server
ローカルでサーバを実行する
```
cd ${INSTALL_DIRECTORY}/source
python manage.py runserver
```


# References
http://chimera.labs.oreilly.com/books/1234000000754/index.html
