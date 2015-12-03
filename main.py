"""Annual-Rainfall"""
import csv
def fetch_data_2012():
  """bring all data in files to dictionary and sum values of each dictionary"""
  rainfall2012_part1=open('RainfallHourlyData2012_Part1.csv',newline='')
  rainfall2012_part2=open('RainfallHourlyData2012_Part2.csv',newline='')
  data1 = csv.reader(rainfall2012_part1)
  data2 = csv.reader(rainfall2012_part2)
  table2012=[row for row in data1]+[row for row in data2]
  info2012 = {}
  for time in range(len(table2012)):
    rain = [float(i) for i in table2012[time][-23:]]
    if table2012[time][3] not in info2012:
      info2012[table2012[time][3]] = sum(rain)
    else:
      info2012[table2012[time][3]] += sum(rain)
  return info2012
  
  def fetch_data_2013():
  """bring all data in files to dictionary and sum values of each dictionary"""
  rainfall2013_part1=open('RainfallHourlyData2013_Part1.csv',newline='')
  rainfall2013_part2=open('RainfallHourlyData2013_Part2.csv',newline='')
  data1 = csv.reader(rainfall2013_part1)
  data2 = csv.reader(rainfall2013_part2)
  table2013=[row for row in data1]+[row for row in data2]
  info2013 = {}
  for time in range(len(table2013)):
    rain = [float(i) for i in table2013[time][-23:]]
    if table2013[time][3] not in info2013:
      info2013[table2013[time][3]] = sum(rain)
    else:
      info2013[table2013[time][3]] += sum(rain)
  return info2013

def fetch_data_2014():
  """bring all data in files to dictionary and sum values of each dictionary"""
  rainfall2014_part1=open('RainfallHourlyData2014_Part1.csv',newline='')
  rainfall2014_part2=open('RainfallHourlyData2014_Part2.csv',newline='')
  data1 = csv.reader(rainfall2014_part1)
  data2 = csv.reader(rainfall2014_part2)
  table2014=[row for row in data1]+[row for row in data2]
  info2014 = {}
  for time in range(len(table2014)):
    rain = [float(i) for i in table2014[time][-23:]]
    if table2014[time][3] not in info2014:
      info2014[table2014[time][3]] = sum(rain)
    else:
      info2014[table2014[time][3]] += sum(rain)
  return info2014
