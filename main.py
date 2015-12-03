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
