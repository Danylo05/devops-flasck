from flask import Flask

app = Flask (__name__)

@app.route('/')
def say_hello():
     return  '''
     <p>Heelo, World, I am a Flask  app!<p>  
     <p><a href="/about">About this application</a><p>
      '''




@app.route('/about')
def about():
    return '''
    <p>This applicarion is running on the Flask web f.<p>
    <p><a href="https://flask.palletsprojects.com/">Flask website </a><p>
    <p><a href="/">Back to home </a><p>
     '''





