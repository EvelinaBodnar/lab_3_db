import csv
import cx_Oracle

connection = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")
cur = connection.cursor()

tables = ['Chocolate', 'Company', 'Beans']
for table in tables:
    cur.execute("delete " +table)

csv_file = open('flavors_of_cacao.csv', encoding='utf-8', errors='ignore')
data = csv.reader(csv_file, delimiter=',')

company_un = []
beens_un = []
i = 1
next(data)
for row in data:
    bar_name = row[1].strip()
    company = row[2].strip()
    bean_type = row[3].strip()
    cocoa_perc = row[4].strip()


    if company not in company_un:
        company_un.append(company)
        cur.execute("INSERT INTO Company(company) VALUES(:company)", company=company)

    if been not in beens_un:
        beens_un.append(been)
        cur.execute("INSERT INTO Bean(been) VALUES(:bean_type)", bean_type=been)

    cur.execute("INSERT INTO Chocolate(bar_id, bar_name, company, year) VALUES(:id, :bar_name, :company, :bean_type, :cocoa_perc)",
		id = i, bar_name = bar_name, company = company, bean_type = bean_type, cocoa_perc = cocoa_perc)


    i += 1

connection.commit()
cur.close()
connection.close()
csv_file.close()
