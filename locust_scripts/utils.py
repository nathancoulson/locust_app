import random
import datetime
import yaml



def url_generator(app_list):
	base_string = "/"
	url_list = []

	for _ in range(10):
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

def save_url_to_file(bias, filename):
	yml_list = filename + ": \n"

	url_list = url_generator(bias_app_list(bias))

	text = yml_list + yaml.dump(url_list, default_flow_style=False)

	with open(filename + ".yml", "w") as text_file:
		text_file.write(text)

save_url_to_file([2, 3], "test")


'''
print(bias_app_list([]))
print(bias_app_list([2]))
print(bias_app_list([2]))
print(bias_app_list([2]))
print(bias_app_list([2]))
print(bias_app_list([4]))
print(bias_app_list([2, 4]))
print(bias_app_list([3, 4]))
print(bias_app_list([2, 3]))

print(url_generator(bias_app_list([2, 3])))
print(url_generator(bias_app_list([4])))
'''