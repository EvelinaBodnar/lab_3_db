import cx_Oracle
connection = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")

import chart_studio
chart_studio.tools.set_credentials_file(username='EvelinaBodnar', api_key='B8KF4tdlXXi5cYNGTXUx')

curs = connection.cursor()

curs.execute('''
SELECT company, COUNT(bar_id) AS count
    FROM Tables
GROUP BY company
ORDER BY count DESC
''')
rows = curs.fetchall()
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


curs.execute('''
SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Tables,
    (SELECT COUNT(bar_name) AS count
FROM Tables)t   
GROUP BY  company,
     t.count
''')
rows = curs.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)
pie = go.Figure(data=[go.Pie(labels=y, values=x )])
pie_url=py.plot(pie, filename='percentage of chocolate company-3',auto_open=False)


curs.execute(''' SELECT bean_type,
    COUNT(Chocolate.bar_id) AS count
    FROM Tables
GROUP BY bean_type
ORDER BY count DESC
''')
rows = curs.fetchall()
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
scatter_beans= file(scatter_url)
pie_choc= file(pie_url)
bar_rating= file(bar_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'file':bar_rating,
    'title': 'Company and quantity of chocolatess'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'file':pie_choc,
    'title': 'percentage of chocolate company  '
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'file':scatter_beans ,
    'title': 'dependence on the type of beans on the percentage of chocolate'
}

board.insert(box_1)
board.insert(box_2, 'below', 1)
board.insert(box_3, 'left', 2)

py.dashboard.upload(board, 'Dashboard.3')

connection.commit()
cur.close()
connection.close()
