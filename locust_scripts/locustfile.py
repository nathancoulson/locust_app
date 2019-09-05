from locust import HttpLocust, TaskSet, task
import random
import yaml

url_sets = yaml.load(open("daily_set.yml"), Loader=yaml.FullLoader)

class UserBehavior(TaskSet):
    @task(1)
    def bias_2(self):
        self.client.get(url_sets["bias_2"][random.randint(1, (len(url_sets["bias_2"]) - 1))])

    @task(1)
    def bias_3(self):
        self.client.get(url_sets["bias_3"][random.randint(1, (len(url_sets["bias_3"]) - 1))])

    @task(1)
    def bias_4(self):
        self.client.get(url_sets["bias_4"][random.randint(1, (len(url_sets["bias_4"]) - 1))])

    @task(1)
    def bias_2_3(self):
        self.client.get(url_sets["bias_2_3"][random.randint(1, (len(url_sets["bias_2_3"]) - 1))])

    @task(1)
    def bias_2_4(self):
        self.client.get(url_sets["bias_2_4"][random.randint(1, (len(url_sets["bias_2_4"]) - 1))])

    @task(1)
    def bias_3_4(self):
        self.client.get(url_sets["bias_3_4"][random.randint(1, (len(url_sets["bias_3_4"]) - 1))])

    @task(1)
    def bias_2_3_4(self):
        self.client.get(url_sets["bias_2_3_4"][random.randint(1, (len(url_sets["bias_2_3_4"]) - 1))])

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_function = lambda self: random.expovariate(1)*4000


