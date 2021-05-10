import bottle
import json
import cache
import processing

import os.path
def load_data( ):
   csv_file = 'cached_data.csv'
   if not os.path.isfile(csv_file):
       url = 'https://data.ny.gov/resource/4a2x-yp8g.json'
       data = cache.load_from_url(url)
       cache.cache_store(data, csv_file)

load_data()

@bottle.route('/')
def index():
  return bottle.static_file("index.html", root="client/")

@bottle.route('/script.js')
def static():
  js_file = bottle.static_file("script.js", root="client/")
  return js_file

@bottle.route('/ajax.js')
def javascript():
  ajax_file = bottle.static_file("ajax.js", root="client/")
  return ajax_file

@bottle.route('/barChart')
def barChart():
  barDataFromCSV=cache.cache_load("cached_data.csv")
  converted_data=cache.convert_data(barDataFromCSV,["total_project_cost"])
  groupedDic=processing.break_out(converted_data,"project_completion_date")
  lv=[]
  lk=[]
  for keys in groupedDic.keys():
    s=(processing.sum_values(groupedDic[keys],"total_project_cost"))
    lv.append(s)
    lk.append(keys)
  finalDataToSend=cache.make_dictionary(lk,lv)
  json_bar = json.dumps(finalDataToSend)
  return json_bar

@bottle.route('/pieChart')
def pieChart():
  pieDataFromCSV=cache.cache_load("cached_data.csv")
  converted_data=cache.convert_data(pieDataFromCSV,["first_year_modeled_project_energy_savings_estimate"])
  dataPie=processing.sum_values_by_year(converted_data,"first_year_modeled_project_energy_savings_estimate")
  json_pie = json.dumps(dataPie)
  return json_pie

@bottle.route('/lineChart')
def lineChart():
  barDataFromCSV=cache.cache_load("cached_data.csv")
  converted_data=cache.convert_data(barDataFromCSV,["total_project_cost", "estimated_annual_kwh_savings"])
  groupedDic=processing.break_out(converted_data,"project_completion_date")
  lstSavings=[]
  lstCosts=[]
  lstKeys=[]
  for keys in groupedDic.keys():
    c=(processing.sum_values(groupedDic[keys],"total_project_cost"))
    lstCosts.append(c)
    s=(processing.sum_values(groupedDic[keys],"estimated_annual_kwh_savings"))
    lstSavings.append(s)
    lstKeys.append(keys)
  lstKeys.sort()
  finalValsLst=[]
  for i in range(len(lstSavings)):
    finalValsLst.append(lstSavings[i]/lstCosts[i])
  finalDataToSend=cache.make_dictionary(lstKeys,finalValsLst)
  json_line = json.dumps(finalDataToSend)
  return json_line


bottle.run(host="0.0.0.0",port=8080)