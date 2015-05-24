# Requirements
Python3 + Django1.8 + Selenium 環境の構築
```
cd ${INSTALL_DIRECTORY}
pyenv virtualenv --python=python3 3.4.2 tdd-dev
pyenv local tddpy-dev
pip3 install -r requirements.txt
pip3 install -r test_requirements.txt
```

# Vagrant with Digital Ocean
1. デプロイで参照するリモートブランチを作成する
```
git remote add {HTTPS_URL}
```

2. インスタンスを起動する
```
vagrant up --provider=digital_ocean
```

3. ブラウザでサーバにアクセスする

# Run tests
* Run all tests
```
make test
```

* Run unit test
```
  make unit-test
```
* Run unit test for JavaScript
```
  make unit-test-js
```
* Run functional test
```
  make functional-test
```

# Run local server
ローカルでサーバを実行する
```
cd ${INSTALL_DIRECTORY}/source
python manage.py runserver
```

# References
http://chimera.labs.oreilly.com/books/1234000000754/index.html
