import json
import csv
import urllib.request

def make_dictionary(x, y):
  new = {}
  for i in (range(len(x))):
    theKey = x[i]
    theValue = y[i]
    new[theKey] = theValue
  return new

def read_csv(reader):
  lod = []
  keys = []
  values = []
  headers = next(reader)
  for row in reader:
    for x in headers:
      keys.append(x)
    for i in row:
      values.append(i)
    d = make_dictionary(keys,values)
    lod.append(d)
  return lod


def make_row(x, y):
    new = []
    for entry in x:
        if entry in y.keys():
            val = y[entry]
            new.append(val)
        else:
            val = ""
            new.append(val)
    return new


import csv

def write_csv(writer, lok, lod):
    w = writer.writerow(lok)
    for dictionary in lod:
      new = make_row(lok, dictionary)
      writer.writerow(new)


def load_from_url(url):
  jb = urllib.request.urlopen(url)
  jsonStr = jb.read().decode()
  data = json.loads(jsonStr)
  return data

def convert_data(lod, lok):
  lodd = []
  d = {}
  if len(lok)==0:
    return lod
  else:
    for d in lod:
      for key in lok:
        for val in d.values():
          d[key] = int(d[key])
        lodd.append(d)
  return lodd

def cache_store(lod, filename):
  with open(filename, "w") as f:
      writer = csv.writer(f)
      lst = []
      for d in lod:
          for key in d.keys():
              if key not in lst:
                  lst.append(key)
      write_csv(writer, lst, lod)
     

def cache_load(fn):
  with open(fn, "r") as f:
    reader = csv.reader(f)
    lod = []
    keys = []
    values = []
    headers = next(reader)
    for row in reader:
      for x in headers:
        keys.append(x)
      for i in row:
        values.append(i)
      d = make_dictionary(keys,values)
      lod.append(d)
    return lod
