"""Annual-Rainfall"""
import csv
import folium
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

def call_data_2012():
  """Call data annual rainfall in 2012-2014"""
  data2012 = fetch_data_2012()
  data2013 = fetch_data_2013()
  data2014 = fetch_data_2014()
  return data2012, data2013, data2014

def create_pie_graph_province():
  """Input province that you want and show graph annual rainfall in 2012-2014 on browser."""
  point=open('point of province.txt',newline='')
  gps = csv.reader(point)
  table = [row for row in gps]
  data2012, data2013, data2014 = call_data_2012(), call_data_2013(), call_data_2014()
  list_summary = [data2012, data2013, data2014]
  north = ['เชียงราย', 'เชียงใหม่', 'น่าน', 'พะเยา', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'อุตรดิตถ์']
  eastnorth = ['กาฬสินธ์ุ', 'ขอนแก่น', 'ชัยภูมิ', 'นครพนม', 'นครราชสีมา', 'บึงกาฬ', 'บุรีรัมย์', 'มหาสารคาม', 'มุกดาหาร',\
              'ยโสธร', 'ร้อยเอ็ด', 'เลย', 'สกลนคร', 'สุรินทร์', 'ศรีสะเกษ', 'หนองคาย', 'หนองบัวลำภู', 'อุดรธานี',\
              'อุบลราชธานี', 'อำนาจเจริญ']
  center = ['กำแพงเพชร', 'ชัยนาท', 'นครนายก', 'นครปฐม', 'นครสวรรค์', 'นนทบุรี', 'ปทุมธานี', 'อยุธยา', 'พิจิตร', 'พิษณุโลก',\
            'เพชรบูรณ์', 'ลพบุรี', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สระบุรี',\
            'อ่างทอง', 'อุทัยธานี', 'กรุงเทพมหานคร']
  east = ['จันทบุรี', 'ฉะเชิงเทรา', 'ชลบุรี', 'ตราด', 'ปราจีนบุรี', 'ระยอง', 'สระแก้ว']
  west = ['กาญจนบุรี', 'ตาก', 'ประจวบคีรีขันธ์', 'เพชรบุรี', 'ราชบุรี']
  south = ['กระบี่', 'ชุมพร', 'ตรัง', 'นครศรีธรรมราช', 'พังงา', 'พัทลุง', 'ภูเก็ต', 'ระนอง', 'สตูล', 'สงขลา', 'สุราษฎร์ธานี']
  count = 2012
  for j in list_summary:
    pie_chart = pygal.Pie()
    pie_chart.title = 'Annual Rainfall in '+(str(count)) +'(in mm)'
    rainfall_n = 0
    rainfall_en = 0
    rainfall_c = 0
    rainfall_e = 0
    rainfall_w = 0
    rainfall_s = 0
  for i in range(len(table)):
    if table[i][0] in north:
      rainfall_n += j[table[i][0]]
    if table[i][0] in eastnorth :
      rainfall_en += j[table[i][0]]
    if table[i][0] in center:
      rainfall_c += j[table[i][0]]
    if table[i][0] in east:
      rainfall_e += j[table[i][0]]
    if table[i][0] in west:
      rainfall_w += j[table[i][0]]
    if table[i][0] in south:
      rainfall_s += j[table[i][0]]
  count += 1
  pie_chart.add('ภาคเหนือ', [rainfall_n])
  pie_chart.add('ภาคตะวันออกเฉียงเหนือ', [rainfall_en])
  pie_chart.add('ภาคกลาง', [rainfall_c])
  pie_chart.add('ภาคตะวันออก', [rainfall_e])
  pie_chart.add('ภาคตะวันตก', [rainfall_w])
  pie_chart.add('ภาคใต้', [rainfall_s])
  pie_chart.render_in_browser()
creat_pie_graph_province()

def mark_gps_map():
    """Add coordinates file as marker point, mark it in OpenStreetMap and create pop-up for describe that point."""
    point=open('point of province.txt',newline='')
    gps = csv.reader(point)
    table = [row for row in gps]
    map_osm = folium.Map(location=[13.7278956, 100.52412349999997], zoom_start=6, tiles='OpenStreetMap')
    data2012 = fetch_data_2012()
    data2013 = fetch_data_2013()
    data2014 = fetch_data_2014()
    for i in range(len(table)):
        map_osm.circle_marker(location=[table[i][1], table[i][2]], radius=10000,line_color='black',
                              fill_color='red', fill_opacity=0.2
                             ,popup='จังหวัด : '+table[i][0]+'<br>Annual Rainfall 2012 : '+\
                              str('%.2f' %data2012[table[i][0]])+' mm'+'<br>Annual Rainfall 2013 : '+\
                              str('%.2f' %data2013[table[i][0]])+' mm'+\
               '<br>Annual Rainfall 2014 : '+str('%.2f' %data2014[table[i][0]])+' mm')
    map_osm.create_map(path='Annual Rainfall Map.html')
    print('create map success')
mark_gps_map()
