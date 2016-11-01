import json
import random
import pandas as pd
from pyhive import hive

HiveHost_Name='103.233.79.140'

def replaceNANumber(val):
    if isinstance(val, (int, float)):
        return str(val)
    else:
        return "0"

def defineFilter(colName,filterValue):
    if filterValue=="(All)":
	Filter=''
    else: 
        Filter=" and "+colName+"='"+filterValue+"'"
    return Filter

def MoviesLikes_Hive(jsdata):
    filterlist = json.loads(jsdata)
    languageFilter=defineFilter('language',filterlist['language'])
    countryFilter=defineFilter('country',filterlist['country'])
    colorFilter=defineFilter('color',filterlist['color'])
    title_yearFilter=defineFilter('title_year',filterlist['title_year'])
    addFilter=languageFilter+countryFilter+colorFilter+title_yearFilter
   
    print 'inside MoviesLikes_Hive Function'
    try:
        conn = hive.Connection(host=HiveHost_Name, port=10000, username="root")
        cursor = conn.cursor()
    except Exception,e:
        print 'Error in Hive connection : ',e

    query="SELECT movie_title,sum(movie_facebook_likes) as likes FROM vagan.imdb_data where movie_title not in ('',' ') "+addFilter+" group by movie_title order by likes desc limit 30"
    print 'Query : ',query

    cursor.execute(query)
    output = []
    for result in cursor.fetchall():
        output.append({'movie':result[0],'likes':result[1]})
    return output

def Hive_DistinctColumns(column):
    try:
        conn = hive.Connection(host=HiveHost_Name, port=10000, username="root")
        cursor = conn.cursor()
    except Exception,e:
        print 'Error in Hive connection : ',e

    query="select distinct "+column+" from vagan.imdb_data where "+column+" not in ('',' ')"
    print "\n\n\n Distinct Column  Query : ", query
    cursor.execute(query)

    output = []
    output.append({'column':'(All)'})
    for result in cursor.fetchall():
        output.append({'column':result[0]})
    return output

#filterlist='{"language": "English","country": "USA","color": "(All)","title_year": "(All)"}'
#print MoviesLikes_Hive(filterlist)
#print Hive_DistinctColumns('language')




