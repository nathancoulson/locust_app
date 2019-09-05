import random
import datetime
import yaml
import os



def url_generator(app_list):
	base_string = "/"
	url_list = []

	for _ in range(20):
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

def save_url_to_file(bias, lst_name, filename):
	yml_list = lst_name + ": \n"

	url_list = url_generator(bias_app_list(bias))

	text = yml_list + yaml.dump(url_list, default_flow_style=False)

	with open(filename + ".yml", "a+") as text_file:
		text_file.write(text)

save_url_to_file([4], "bias_4", "daily_set")
save_url_to_file([3], "bias_3", "daily_set")
save_url_to_file([2], "bias_2", "daily_set")
save_url_to_file([2,3], "bias_2_3", "daily_set")
save_url_to_file([2,4], "bias_2_4", "daily_set")
save_url_to_file([3,4], "bias_3_4", "daily_set")
save_url_to_file([2,3,4], "bias_2_3_4", "daily_set")