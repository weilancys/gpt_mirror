# ChatGPT Mirror

### intro
- ChatGPT Mirror is a tiny mirror site built with flask and [the openai python library](https://github.com/openai/openai-python).

### install
1. clone this repo
2. `cd gpt_mirror`
3. `python setup.py install`

### run
1. replace your openai api key in config.py
2. put config.py in flask [instance folder](https://flask.palletsprojects.com/en/2.2.x/config/#instance-folders)
3. `waitress-serve --port 8080 --call gpt_mirror:create_app` you can choose your port.
4. optionally, you can use `flask run` too
5. navigate to `localhost:8080` and the app greets you happily there.


### deploy
- [deploy options](https://flask.palletsprojects.com/en/2.1.x/deploying/)