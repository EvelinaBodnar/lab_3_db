import cx_Oracle
connection = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")

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
bar_url=py.plot(fig,filename='Company and quantity of chocolates-3', auto_open=False)


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
pie_url=py.plot(pie, filename='percentage of chocolate company-3',auto_open=False)


cur.execute(''' SELECT Bean.bean_type,
    COUNT(Chocolate.bar_id) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC
''')
rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)
scatter = go.Figure([go.Scatter(x=y, y=x)])
scatter_url=py.plot(scatter, filename = 'dependence on the type of beans on the percentage of chocolate-3', auto_open=False)

import re
import chart_studio.dashboard_objs as dashboard

board = dashboard.Dashboard()
scatter_beans= fileId(scatter_url)
pie_choc= fileId(pie_url)
bar_rating= fileId(bar_url)

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

board.insert(box_1)
board.insert(box_2, 'below', 1)
board.insert(box_3, 'left', 2)

py.dashboard.upload(mboard, 'Dashboard.3')

connection.commit()
cur.close()
connection.close()
