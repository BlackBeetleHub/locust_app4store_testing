from locust import HttpLocust, TaskSet, task

credit_users = [
    {"username1", "password1"},
    {"username2", "password2"},
    {"username3", "password3"}
]

class UserBehavior(TaskSet):

    def on_start(self):
        print(credit_users.pop())
        self.client.get('/')

    def on_stop(self):
        self.client.get('/')

    @task(2)
    def index(self):
        self.client.get('/')

    @task(1)
    def profile(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000




