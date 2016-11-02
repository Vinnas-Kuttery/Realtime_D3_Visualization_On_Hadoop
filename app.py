from flask import Flask, render_template, jsonify
from loadHiveData import *#import get_data,tempdata,sentimentDataLoad,uniqueKeywords()
import os
from loadHBaseData import *

app = Flask(__name__)

@app.route('/getMovieHiveList/<jsdata>')
def getMovieHiveList(jsdata):
    d=str(jsdata)
    data=MoviesLikes_Hive(d)
    return  json.dumps(data)

@app.route('/ajaxGetHiveUniqueItems/<jsdata>')
def ajaxGetHiveUniqueItems(jsdata):
    column=str(jsdata)
    data=Hive_DistinctColumns(column)
    return  json.dumps(data)

@app.route('/HiveViz')
def HiveViz():
    return render_template('Hive_template.html')


@app.route('/getMovieHBaseList/<jsdata>')
def getMovieHBaseList1(jsdata):
    d=str(jsdata)
    data=MoviesLikes_HBase(d)
    return  json.dumps(data)

@app.route('/ajaxGetHBaseUniqueItems/<jsdata>')
def ajaxGetHBaseUniqueItems1(jsdata):
    column=str(jsdata)
    data=Hbase_DistinctColumns(column)
    return  json.dumps(data)

@app.route('/HBaseViz')
def HBaseViz():
    return render_template('HBase_template.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
