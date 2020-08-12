# proxy-gen-telegram-bot

>This will generate the proxy which less than <50ms out of list. It is based on Telegram bot API and module usage of python-telegram-bot

### Clone

- Clone this repo to your local machine using `https://github.com/chirusandeep/proxy-gen-telegram-bot.git`

### Setup

- Get token from telegram bot API from botfather.
- Use generated token in proxy-gen-telegram-bot file.

### Installation
>Linux
```shell
$ pip3 install -r requirements.txt
```

>Windows
```shell
$ pip install -r requirements.txt
```
- Modules will be installed are `python-telegram-bot`,`pytz`,`requests`.

###Usage
>Linux
```shell
$ python3 testing_proxy_gen.py
```

>Windows
```shell
$ python testing_proxy_gen.py
```

- Now bot will up and use the commands `http`,`socks4`,`socks5`.

### Deployment
>We use heroku here with files `Procfile` and `requirements` necessary.

- Steps to Deploy in Heroku.

```shell
$ heroku login
$ heroku git:clone -a `bot name here`
$ cd `bot name here`
```
- Deploy the files in Heroku.

```shell
$ git add .
$ git commit -am "First commit"
$ git push heroku master
```

Leave a star for noobs army. :)
