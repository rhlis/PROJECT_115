'use strict'

function showPie(response){
  let js_pie=JSON.parse(response)
  let pieLabelList=[]
  let pieValuesList=[]
  for (let k of Object.keys(js_pie)){
    pieLabelList.push(k)
  }
  for (let v of Object.values(js_pie)){
    pieValuesList.push(v)
  }
  let pieDiv= document.getElementById("plotPie")
  let pie_data =  [{
  values: pieValuesList ,
  labels: pieLabelList ,
  type: 'pie'}]
  let layout = {
  title: 'First Year Savings By Year Completed'}
  Plotly.newPlot(pieDiv, pie_data,layout);
}

function showBar(res){
  let js_bar=JSON.parse(res)
  let xList=[]
  let yList=[]
  for (let keys of Object.keys(js_bar)){
    xList.push(keys)
  }
  for (let vals of Object.values(js_bar)){
    yList.push(vals)
  }
  let bar_data = [
  {
    x: xList,
    y: yList,
    type: 'bar'
  }
  ];
  let layout = {
  title: 'Sum of Total Project Costs By Date Completed', xaxis: {
  title: 'Date Completed'}, yaxis: {title: 'Total Costs (in $)'}};
  let barDiv= document.getElementById("plotBar")
  Plotly.newPlot(barDiv,bar_data,layout); 
}

function showLine(res){
  let js_line=JSON.parse(res)
  let xList=[]
  let yList=[]
  for (let keys of Object.keys(js_line)){
    xList.push(keys)
  }
  for (let vals of Object.values(js_line)){
    yList.push(vals)
  }
  let line_data = [
  {
    x: xList,
    y: yList,
    type: 'scatter'
  }
  ];
  let layout = {
  title: 'kWh Saved Per Dollar Spent By Date Completed', xaxis: {
  title: 'Date'}, yaxis: {title: 'kWh/$'}};
  let lineDiv= document.getElementById("plotLine")
  Plotly.newPlot(lineDiv,line_data,layout); 
}


function getData() {
  let bar = ajaxGetRequest("/barChart", showBar)
  let line = ajaxGetRequest("/lineChart", showLine)
  let pie = ajaxGetRequest("/pieChart", showPie)
}



