
def get_values(d_list,k):
  acc=[]
  for dictionaryy in d_list:
    for x in dictionaryy.keys():
      if x == k and dictionaryy[x] not in acc:
        acc.append(dictionaryy[x])
  return acc

def break_out(LOD, K):
  result = {}
  lst = []
  for dictionary in LOD:
    V=dictionary[K]
    result[V]=[]
  for V in result.keys():
    for dictionary in LOD:
      if dictionary[K] == V:
        result[V].append(dictionary)
  return result

def sum_values(dd,kk):
  summ=[]
  for dictionaryy in dd:
    for x in dictionaryy.keys():
       if x == kk:
          summ.append(dictionaryy[x])
  return sum(summ)

def sum_values_by_year(listDictionaries, parameter):
  result ={}
  for dictionary in listDictionaries:
      theDate = dictionary['project_completion_date']
      theYear = theDate[0] + theDate[1] + theDate[2] + theDate[3]
      theValue = dictionary[parameter]
      if theYear in result: 
          result[theYear] = result[theYear] + theValue
      else:
          result[theYear] = theValue
  return result

