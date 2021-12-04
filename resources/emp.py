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
                'x-api-key': "uH6EIvpPE33jltEGfjqcq3vv7zpzy0m14vJ5tvJO"
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
                r=[]
                close =d['close']
                leng_close = len(close)
                rebased = 100
                month = []
                rebase = []
                month_count = 0
                year_count = 0
                
                for i in range(leng_close):
                    month_count += 1
                    if month_count == 12:
                        month_count =0
                        year_count +=1


                    cumlative = 1
                    previous_month_adj = close[i]
                    try:
                        next_month_adj = close[i+1]
                    except IndexError:
                        next_year = 0
                
                    montly_return = (next_month_adj - previous_month_adj) / previous_month_adj # montly returns
                    month.append(montly_return)

                    rebased =  next_month_adj*100 / l2[0]# rebased to 100
                    rebase.append(rebased)

                    for j in month:       # cumlative returns
                        cumlative = cumlative *(1 + j)

                    r.append(rebased)
                d['close']=r
            return {"data":dic},201
        except Exception as e:
            print(str(e)+"Error")
            return {"message":"There was an error connecting to user table."},500

class Benchmark(Resource):
    def get(self):
        try:
            url = "https://yfapi.net/v8/finance/spark?interval=1mo&range=8y&symbols=AAPL%2CMSFT%2CAMZN%2CFB%2CTSLA%2CNDX"

            querystring = {"symbols":"NDX"}

            headers = {
                'x-api-key': "uH6EIvpPE33jltEGfjqcq3vv7zpzy0m14vJ5tvJO"
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
                'x-api-key': "uH6EIvpPE33jltEGfjqcq3vv7zpzy0m14vJ5tvJO"
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
