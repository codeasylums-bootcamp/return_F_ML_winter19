import requests
import subprocess as sp
import time
import json

while(1):
	print("\n\n****WELCOME TO FLIPKART LAPTOP DATABASE****\n")
	print("What would you like to do?")
	print("1. GET (Retrive)")
	print("2. POST (Insert)")
	print("3. PUT (Update)")
	print("4. DELETE")

	ch = int(input())

	if ch==1:
		print("1. Get all data")
		print("2. Search by id")
		ch2 = int(input())

		if ch2==1:
			url = "http://192.168.43.201:8000/laptops/laptops/"
			
		elif ch2==2:
			print("Enter id to search")
			name = int(input())
			url = "http://192.168.43.201:8000/laptops/laptops/"
			url = url + str(name)

		r = requests.get(url = url)
		data = r.json()	
		
		if r.status_code == requests.codes.ok:
			print("\nOperation was successful!\n")
			if ch2==2:
				for i,j in data.items():
					print(str(i) + ":" + str(j) )
				print("\n")
				#print(data)
			elif ch2==1:
				for k in data:					
					for i,j in k.items():
						print(str(i) + ":" + str(j))
					print("\n")
										
					
		else:
			print("No data was found!\n")
		#print(data)


	elif ch==2:
		print("Enter name")
		name = str(input())
		print("Enter storage")
		storage = str(input())
		print("Enter Screen size")
		ssize = str(input())
		print("Enter OS")
		os = str(input())
		print("Enter RAM")
		ram = str(input())
		print("Enter Processor")
		proc = str(input())
		print("Enter Warranty")
		war = str(input())
		p = 1
		while(p):
			print("Enter Price")
			price = (input())
			if price.isdigit():
				p = 0	
			else:
   				print("Enter a numeric value!\n")

		
		time.sleep(0.5)

		data2 = ""

		data2 = data2+ "{\n    \n  \"name\": \""
		data2 = data2 + name

		data2 += "\",\n   \"storage\": \""
		data2 += storage

		data2 += "\",\n   \"screen_size\": \""
		data2 += ssize
		
		data2 += "\",\n   \"OS\": \""
		data2 += os

		data2 += "\",\n   \"RAM\": \""
		data2 += ram

		data2 += "\",\n   \"Processor\": \""
		data2 += proc

		data2 += "\",\n   \"Warranty\": \""
		data2 += war

		data2 + "\",\n   \"Price\": \""
		data2 += str(price)

		data2 += "\"\n  }"


		url = "http://192.168.43.201:8000/laptops/laptops/"


		headers = {
		    'Content-Type': "application/json",
		    #'User-Agent': "PostmanRuntime/7.20.1",
		    'Accept': "*/*",
		    'Cache-Control': "no-cache",
		    #'Postman-Token': "1be90664-8adf-4e6e-9395-d650dfd98115,c3bba6de-ab04-44a6-a057-4ecd86936bfc",
		    'Host': "192.168.43.201:8000",
		    'Accept-Encoding': "gzip, deflate",
		    'Content-Length': "237",
		    'Connection': "keep-alive",
		    'cache-control': "no-cache"
		    }


		r = requests.request("POST", url, data=data2, headers=headers)

		#print(r)
		if r.status_code == requests.codes.ok:
			print("\nData was succesfully added!\n")
			print(data2)

	elif ch==3:
		print("Enter index to edit data : ")
		index = int(input())
		url = "http://192.168.43.201:8000/laptops/laptops/"
		url2 = url + str(index)

		r2 = requests.request("GET",url = url2)
		print(r2.status_code)
		if r2.status_code != 404:
			print("\nEntry Found!\n")
			
		else:
			print("No Entry Found!")
			continue;
		url += str(index)
		url += "/"
		
		headers = {
		    'Content-Type': "application/json",
		    'User-Agent': "PostmanRuntime/7.20.1",
		    'Accept': "*/*",
		    'Cache-Control': "no-cache",
		    'Postman-Token': "3f687248-e52b-4396-80f5-3ffd580a1a60,33f09195-ac97-4f16-ba67-af06b17b9a1e",
		    'Host': "192.168.43.201:8000",
		    'Accept-Encoding': "gzip, deflate",
		    'Content-Length': "254",
		    'Connection': "keep-alive",
		    'cache-control': "no-cache"
		    }
		

		print("Enter name")
		name = str(input())
		print("Enter storage")
		storage = str(input())
		print("Enter Screen size")
		ssize = str(input())
		print("Enter OS")
		os = str(input())
		print("Enter RAM")
		ram = str(input())
		print("Enter Processor")
		proc = str(input())
		print("Enter Warranty")
		war = str(input())
		print("Enter Price")
		price = int(input())

		data2 = ""

		data2 = data2+ "{\n    \n  \"name\": \""
		data2 = data2 + name

		data2 += "\",\n   \"storage\": \""
		data2 += storage

		data2 += "\",\n   \"screen_size\": \""
		data2 += ssize
		
		data2 += "\",\n   \"OS\": \""
		data2 += os

		data2 += "\",\n   \"RAM\": \""
		data2 += ram

		data2 += "\",\n   \"Processor\": \""
		data2 += proc

		data2 += "\",\n   \"Warranty\": \""
		data2 += war

		data2 + "\",\n   \"Price\": \""
		data2 += str(price)

		data2 += "\"\n  }"

		response = requests.request("PUT", url=url, data=data2, headers=headers)

		print(response.text)

		
	elif ch==4:
		print("Enter index to delete data : ")
		index = int(input())
		url = "http://192.168.43.201:8000/laptops/laptops/"

		url2 = url + str(index)

		r2 = requests.request("GET",url = url2)
		print(r2.status_code)
		if r2.status_code != 404:
			print("\nEntry Found!\n")
			
		else:
			print("No Entry Found!")
			continue;

		url += str(index)
		url += "/"

		headers = {
		    'User-Agent': "PostmanRuntime/7.20.1",
		    'Accept': "*/*",
		    'Cache-Control': "no-cache",
		    'Postman-Token': "e2f16d50-6bca-48a0-bbfa-cf1738af19db,172b8871-cb05-4cbc-a76f-a3b599fb8a5b",
		    'Host': "192.168.43.201:8000",
		    'Accept-Encoding': "gzip, deflate",
		    'Content-Length': "0",
		    'Connection': "keep-alive",
		    'cache-control': "no-cache"
		    }

		response = requests.request("DELETE", url, headers=headers)

		if response.status_code==200 or response.status_code==204:
			print("Data Deleted!\n")



	print("Continue? or exit?")
	ch3 = input()

	if ch3 == "exit":
		exit()
	
	

#url = "http://127.0.0.1:8000/laptops/laptops/"
#r = requests.get(url = url)
#data = r.json()
#print(data)
