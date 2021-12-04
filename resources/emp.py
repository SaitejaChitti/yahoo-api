from flask_restful import Resource,reqparse
from db import query
from werkzeug.security import safe_str_cmp
from flask_cors import CORS 
import requests
import json
import time
import datetime as dt
class Yahoo(Resource):
    def get(self):
        try:
            url = "https://yfapi.net/v8/finance/spark?interval=1mo&range=8y&symbols=AAPL%2CMSFT%2CAMZN%2CFB%2CTSLA%2CNDX"

            querystring = {"symbols":"AAPL,MSFT,AMZN,FB,TSLA,NDX"}

            headers = {
                'x-api-key': "bu1LFtkDIT3Dy3HsaBwnv95yRFyATHIf6sWFzDs6"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)


            data=json.loads(response.text)
            stocks=['AAPL','MSFT','AMZN','FB','TSLA','NDX']
            dic={}
            for i in stocks:
                for j in range(len(data[i]['timestamp'])):
                    data[i]['timestamp'][j]=dt.datetime.utcfromtimestamp(data[i]['timestamp'][j]).strftime("%m/%Y")
                l1=[]
                l2=[]
                d={}
                d1=dt.date(2015,12,1)
                d2=dt.date(2021,1,1)
                for k,v in zip(data[i]['timestamp'],data[i]['close']):
                    l=k.split("/")
                    p=dt.date(int(l[1]),int(l[0]),1) # Converting String date to Date Object  
                    #print(d1,d2)
                    if p>= d1 and p <= d2:
                        l1.append(k)
                        l2.append(v)
                        print(k,v)
                d['datetime']=l1
                d['close']=l2
                dic[i]=d
            return {"data":dic},201
        except:
            return {"message":"There was an error connecting to user table."},500

class Benchmark(Resource):
    def get(self):
        try:
            url = "https://yfapi.net/v8/finance/spark?interval=1mo&range=8y&symbols=AAPL%2CMSFT%2CAMZN%2CFB%2CTSLA%2CNDX"

            querystring = {"symbols":"NDX"}

            headers = {
                'x-api-key': "bu1LFtkDIT3Dy3HsaBwnv95yRFyATHIf6sWFzDs6"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)


            data=json.loads(response.text)
            stocks=['NDX']
            dic={}
            for i in stocks:
                for j in range(len(data[i]['timestamp'])):
                    data[i]['timestamp'][j]=dt.datetime.utcfromtimestamp(data[i]['timestamp'][j]).strftime("%m/%Y")
                l1=[]
                l2=[]
                d={}
                d1=dt.date(2015,12,1)
                d2=dt.date(2021,1,1)
                for k,v in zip(data[i]['timestamp'],data[i]['close']):
                    l=k.split("/")
                    p=dt.date(int(l[1]),int(l[0]),1) # Converting String date to Date Object  
                    #print(d1,d2)
                    if p>= d1 and p <= d2:
                        l1.append(k)
                        l2.append(v)
                        print(k,v)
                d['datetime']=l1
                d['close']=l2
                dic[i]=d
            return {"data":l2},201
        except:
            return {"message":"There was an error connecting to user table."},500


class Trade(Resource):
    def get(self):
        try:
            url = "https://yfapi.net/v8/finance/spark?interval=1mo&range=8y&symbols=AAPL%2CMSFT%2CAMZN%2CFB%2CTSLA%2CNDX"

            querystring = {"symbols":"AAPL,MSFT,AMZN,FB,TSLA,NDX"}

            headers = {
                'x-api-key': "bu1LFtkDIT3Dy3HsaBwnv95yRFyATHIf6sWFzDs6"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)


            data=json.loads(response.text)
            stocks=['AAPL','MSFT','AMZN','FB','TSLA','NDX']
            dic={}
            for i in stocks:
                for j in range(len(data[i]['timestamp'])):
                    data[i]['timestamp'][j]=dt.datetime.utcfromtimestamp(data[i]['timestamp'][j]).strftime("%m/%Y")
                l1=[]
                l2=[]
                d={}
                d1=dt.date(2015,12,1)
                d2=dt.date(2021,1,1)
                for k,v in zip(data[i]['timestamp'],data[i]['close']):
                    l=k.split("/")
                    p=dt.date(int(l[1]),int(l[0]),1) # Converting String date to Date Object  
                    #print(d1,d2)
                    if p>= d1 and p <= d2:
                        l1.append(k)
                        l2.append(v)
                        print(k,v)
                #d['datetime']=l1
                d['close']=l2
                dic[i]=d
            return {"data":dic},201
        except Exception as e:
            print(e)
            return {"message":"There was an error connecting to user table."},500