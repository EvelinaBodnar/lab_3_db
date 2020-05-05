import csv
import cx_Oracle
try:
	conn = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")
except cx_Oracle.DatabaseError as exception:
    print('Not working database %s\n', database)
    print(exception)
    exit(1)

cur = conn.cursor()

tabl = ['Chocolate', 'Company', 'Beans']
for table in tabl:
    cur.execute("delete " +table)
file = open('flavors_of_cacao.csv', encoding='utf-8')
rows = csv.reader(file, delimiter=',')

company_un = []
beens_un = []
bar_id = 1
next(rows)
for row in rows:
    bar_name = row[1].strip()
    company = row[0].strip()
    bean_type = row[-1].strip()
    cocoa_perc = row[4].strip()
   if company not in company_un:
        company_un.append(company)
        cur.execute("INSERT INTO Company(company) VALUES(:company)", company=company)

    if bean_type not in beens_un:
        beens_un.append(bean_type)
        cur.execute("INSERT INTO Bean(bean_type) VALUES(:bean_type)", bean_type=bean_type)

    cur.execute("INSERT INTO Chocolate(bar_id, bar_name, company, year) VALUES(:bar_id, :bar_name, :company, :bean_type, :cocoa_perc)",
		bar_id = bar_id, bar_name = bar_name, company = company, bean_type = bean_type, cocoa_perc = cocoa_perc)
    bar_id += 1

conn.commit()
cur.close()
conn.close()
file.close()
