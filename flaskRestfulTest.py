#coding=utf-8
from flask import Flask
#from flask.ext import restful  貌似废弃了这个
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)


#官网更多例子https://www.cnblogs.com/wbin91/p/5927506.html

