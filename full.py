from locust import HttpLocust, TaskSet, task
from simple import UserBehavior as UserBehaviorSimple

class UserBehavior(UserBehaviorSimple):
    @task(1)
    def aboutus(self):
        self.client.get('/aboutus')

    @task(1)
    def privacypolicy(self):
        self.client.get('/privacypolicy')

    @task(1)
    def help(self):
        self.client.get('/help')

    @task(1)
    def licenseterms(self):
        self.client.get('/licenseterms')

    def on_stop(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 900
