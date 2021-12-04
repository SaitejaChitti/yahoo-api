from flask import Flask
from flask_restful import Api
from resources.emp import Yahoo,Benchmark
from flask_cors import CORS

app=Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS']=True
api=Api(app)
CORS(app)
api.add_resource(Yahoo,'/yahoo')
api.add_resource(Benchmark,'/benchmark')

if __name__=='__main__':
    app.run()
