import os
rootdir = os.getcwd()

thelist = []
linesPrint = 0

def returnIP(line):
  import re

  theIP = '' 
  searchObj = re.search( r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', line, re.M|re.I)
  if searchObj:
    results = searchObj.group()
    return str(results)
  else:
    return None

theList= []
for root, _, files in os.walk(rootdir):
  for f in files: # Each file in the Directory 
    if '.py' in f:
      print 'Skipping %s'% f
    else:
      fname = os.path.join(root, f) # Set the name and path of the file 
      print 'Opening', fname # Displays name of the file
      theFile = open(fname,'r') # Opens the file
      for line in theFile:
        #### Do a check here
        theResults = returnIP(line) 
        if theResults:
          if theResults not in theList:
            theList.append(theResults)
      	linesPrint = linesPrint + 1 # Increases the lines print by one
      theFile.close() 


if not theList: # After the all files have been read
  print 'The search returned no results... Sorry - better luck next time'
else: #If the array isn't empty
  print 'Writing log file to disk' # Display
  theLog = rootdir + '\\'+ 'ExtractedIPs.txt'
  writeLog = open(theLog, 'w')
  for item in theList:
    item = "%s\n" % item
    writeLog.write(item)
  writeLog.close()
  thelist = []