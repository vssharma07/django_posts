import pandas as pd
import statistics

csv_file = pd.read_csv("data.csv")
ages = []
domains = []
for index, row in csv_file.iterrows():
	email = row['email']
	age = row['age']
	ages.append(age)
	domain = email.split('@')[1]
	domains.append(domain)

print(f"Average Age: {round(statistics.mean(ages), 1)}\nMost Common Domain: {max(domains, key=domains.count)}")