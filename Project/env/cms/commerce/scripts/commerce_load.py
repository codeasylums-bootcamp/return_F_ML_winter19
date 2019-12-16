import csv

from commerce.models import Laptop

def run():
	fhand = open('commerce/load.csv')
	reader = csv.reader(fhand)


	for row in reader:
		name = row[0]
		storage = row[1]
		screen_size = row[2]
		OS = row[3]
		RAM = row[4]
		Processor = row[5]
		Warranty = row[6]
		Price = row[7]
		
		new_laptop=Laptop(name=name, storage=storage, screen_size=screen_size, OS=OS, RAM=RAM, Processor=Processor,Warranty=Warranty,Price=Price )
		new_laptop.save()