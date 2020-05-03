import cx_Oracle

try:
    connection = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")
except cx_Oracle.DatabaseError as exception:
    print('Failed to connect to %s\n', database)
    print(exception)
    exit(1)
import chart_studio
chart_studio.tools.set_credentials_file(username='EvelinaBodnar', api_key='B8KF4tdlXXi5cYNGTXUx')

cur = connection.cursor()

cur.execute('''
SELECT company, COUNT(bar_id) AS count
    FROM Chocolate
GROUP BY company
ORDER BY count DESC
''')
rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

import plotly.graph_objects as go
import chart_studio.plotly as py
bar = [go.Bar(x=y, y=x)]

fig = go.Figure(data=bar)


bar_money_url=py.plot(fig,filename='Company and quantity of chocolates-3', auto_open=False)

cur.execute('''
SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count
''')


rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)
pie = go.Figure(data=[go.Pie(labels=y, values=x )])
pie_gdp_url=py.plot(pie, filename='percentage of chocolate company-3',auto_open=False)

cur.execute(''' SELECT Bean.bean_type,
    COUNT(Chocolate.bar_id) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC;
''')

rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

scatter = go.Figure([go.Scatter(x=y, y=x)])

scatter_migration_url=py.plot(scatter, filename = 'dependence on the type of beans on the percentage of chocolate-3', auto_open=False)

import re
import chart_studio.dashboard_objs as dashboard
def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

my_dboard = dashboard.Dashboard()

scatter_migration= fileId_from_url(scatter_migration_url)
pie_gdp= fileId_from_url(pie_gdp_url)
bar_coastline= fileId_from_url(bar_money_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':bar_rating,
    'title': 'Company and quantity of chocolatess'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':pie_choc,
    'title': 'percentage of chocolate company  '
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':scatter_beans ,
    'title': 'dependence on the type of beans on the percentage of chocolate'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Dashboard.3')

connection.commit()
cur.close()
connection.close()
