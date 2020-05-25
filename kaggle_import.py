import csv
import cx_Oracle

username = 'viktoriya'
password = 'viktoriya'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

csvfile = open('flavors_of_cacao.csv', errors='ignore', encoding='utf-8')
readCSV = csv.reader(csvfile, delimiter=',')
bar_id = 0

company_unique = []


tables = ['Chocolate', 'Company']
for table in tables:
    cursor.execute("DELETE FROM " + table)

try:
    for row in readCSV:
        bar_name = row[1].strip()
        company = row[0].strip()
        bean_type = row[-1].strip()
        cocoa_perc = row[4].strip()

        if company not in company_unique:
            company_unique.append(company)
            query = '''INSERT INTO Company(company) VALUES(:company)'''
            cursor.execute(query, company=company)


        query = '''
        INSERT INTO Chocolate(bar_id, bar_name, company, bean_type, cocoa_perc) VALUES(:bar_id, :bar_name, :company, :bean_type, :cocoa_perc)'''
        cursor.execute(query, bar_id = bar_id, bar_name = bar_name, company = company, bean_type = bean_type, cocoa_perc = cocoa_perc)

        bar_id += 1

except:
    print(f'Error of the row {bar_id}')
    raise

csvfile.close()
connection.commit()
cursor.close()
connection.close()
