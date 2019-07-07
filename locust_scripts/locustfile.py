from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(3)
    def index(self):
        self.client.get("/")

    @task(1)
    def return_num(self):
        self.client.get("/10")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000