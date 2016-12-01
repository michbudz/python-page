#!/usr/bin/python
import os

virtenv = os.environ['APPDIR'] + '/env/'    # THIS LINE EDITED
#os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages') #This LINE added
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass


from flask import Flask, jsonify, render_template


app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title': u'Buy this book',
        'description': u'Mike, Pizza, Fruit, Textylia',
        'done': False
    },
     {
        'id':2,
        'title': u'Learn Python ',
        'description': u'Mike, Pizza, Fruit, Textylia',
        'done': False
     }
    
]


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify({'data':tasks})

@app.route("/html", methods=['GET'])
def get_html():
    return render_template('test.html')

@app.route("/my", methods=['GET'])
def get_my():
    return render_template('my.html')

if __name__ == "__main__":
    app.run(debug=True)