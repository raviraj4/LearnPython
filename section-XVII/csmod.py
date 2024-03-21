import csv
path = "D://Computer Science//Courses//Udemy//jose portila-python//python programs//section-XVII//hola.csv"
data = open(path,encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)
