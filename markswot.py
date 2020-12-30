import requests

class MarksWot:
	"""
		Все нации:
		СССР(ussr)
		Германия(germany)
		США(usa)
		Китай(china)
		Франция(france)
		Великобритания(uk)
		Япония(japan)
		Чехия(czech)
		Швеция(sweden)
		Польша(poland)
		Италия(italy)

		Все классы:
		heavytank
		mediumtank
		lighttank
		at-spg
		spg
	"""

	def __init__(self, nation, level=None, typet=None):
		headers = {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'X-CSRF-TOKEN': 'wEJS1zx4OCPdN41nv6Zkz3sIFnmFHvEtUqoB6p6Y',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie': '__cfduid=da08c7406be5ff9557c9713a91398aaa01596838201; _ga=GA1.2.396453457.1596838202; _gid=GA1.2.1468575389.1599315260; XSRF-TOKEN=eyJpdiI6IlwvK2VlNEkxdSswbEs1NjUyZW12a293PT0iLCJ2YWx1ZSI6Ik1sdGl1YjVwRlN1cHBaaHkzdnZnYUlJaHNNUTZydXBQc1NWS3BrdXAzZ295a2dHNDRxQXR2cVU2NkpqR0ZDb0siLCJtYWMiOiI0Y2RlYzU2ZTFmYjA4YzA2MGE2YWJjN2QwNDdkNjJiYjViYWVmMzU3NzZhMjBlYjc3MTZmYjlkZmJkYjA0YTg2In0%3D; lebwatv_session=eyJpdiI6IlRnUElnODBlWVdZUUlVakYyMUg4Z1E9PSIsInZhbHVlIjoia3JWcWZVRkh2WTBINUI3V2ZjSk4wYnczY0pjVmxlUUhOTGk5VTlzbEsycCtGN21nUis1WFRWdWVRSWd2b0tIMyIsIm1hYyI6ImI5MjEyYThkYjk1MDVmMTI0YzE3YWNhNjljYWVhZTg1Y2M4NjJlMjA4NzRlYjliNDM3MjVhZTUzNTVhNTI2MTIifQ%3D%3D'}
		data = {'nation': nation}
		data_level = {'nation': nation, 'level': level}
		data_types = {'nation': nation, 'type': typet}
		data_types_level = {'nation': nation, 'level': level, 'type': typet}
		if level == None and typet == None:
			self.marks = requests.post('https://lebwa.tv/marks/filter', headers=headers, data=data).json()['data']
			self.mastery = requests.post('https://lebwa.tv/mastery/filter', headers=headers, data=data).json()['data']
		elif typet:
			if level == None:
				self.marks = requests.post('https://lebwa.tv/marks/filter', headers=headers, data=data_types).json()['data']
				self.mastery = requests.post('https://lebwa.tv/mastery/filter', headers=headers, data=data_types).json()['data']
			else:
				self.marks = requests.post('https://lebwa.tv/marks/filter', headers=headers, data=data_types_level).json()['data']
				self.mastery = requests.post('https://lebwa.tv/mastery/filter', headers=headers, data=data_types_level).json()['data']				
		elif level:
			self.marks = requests.post('https://lebwa.tv/marks/filter', headers=headers, data=data_level).json()['data']
			self.mastery = requests.post('https://lebwa.tv/mastery/filter', headers=headers, data=data_level).json()['data']


	def get_marks(self):
		wot_all = {}
		for i in self.marks:
			type_wot = i['type']
			name = i['name']
			values = i['values']
			if type_wot == 'at-spg':
				type_wot = 'ПТ-САУ'
			elif type_wot == 'heavytank':
				type_wot = 'Тяжелый танк'
			elif type_wot == 'lighttank':
				type_wot = 'Легкий танк'
			elif type_wot == 'mediumtank':
				type_wot = 'Средний танк'
			elif type_wot == 'spg':
				type_wot = 'САУ'
			wot_all[type_wot + ' - ' + name]=values
		return wot_all

	def get_mastery(self):
		wot_all = {}
		for i in self.mastery:
			type_wot = i['type']
			name = i['name']
			values = i['values']
			if type_wot == 'at-spg':
				type_wot = 'ПТ-САУ'
			elif type_wot == 'heavytank':
				type_wot = 'Тяжелый танк'
			elif type_wot == 'lighttank':
				type_wot = 'Легкий танк'
			elif type_wot == 'mediumtank':
				type_wot = 'Средний танк'
			elif type_wot == 'spg':
				type_wot = 'САУ'
			wot_all[type_wot + ' - ' + name]=values
		return wot_all

if __name__ == "__main__":
	print(MarksWot(nation='ussr', level='6').get_mastery())