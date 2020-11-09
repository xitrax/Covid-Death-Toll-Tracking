uniqlines = set(open('/Users/mshapour/PythonScripts/Covid-19-Iran.txt').readlines())
f = open("CovidFinal.txt", "wb").writelines(set(uniqlines))
#f.close()

