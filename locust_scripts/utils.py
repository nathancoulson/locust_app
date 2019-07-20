import random
import datetime

def url_generator(app_list):
	base_string = "/"
	url_list = []

	for app in app_list:
		instances = random.choice(range(1,6))
		url = base_string + str(random.choice(app_list)) + '/'
		for i in range(instances):
			if i < instances - 1:
				url = url + str(random.choice(app_list)) + '-'
			else:
				url = url + str(random.choice(app_list))
		url = url + "/" + str(random.randint(1,250))
		url_list.append(url)

	return url_list

def bias_app_list(bias):
	avail_apps = [2, 3, 4]

	app_list = avail_apps + (bias * random.randint(1,2))

	return app_list
	


print(bias_app_list([4]))

#print(url_generator([2,3,4,4,4,2,4,2,4]))