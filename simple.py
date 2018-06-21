from locust import HttpLocust, TaskSet, task
from config_apps import get_random_app

class UserBehavior(TaskSet):

    def on_start(self):
        self.client.get('/')
        self.app = get_random_app()
        self.client.get(self.app.get_page_application())

    @task(1)
    def main(self):
        self.client.get('/')

    @task(1)
    def visit_application_details(self):
        self.client.get(self.app.get_page_application())

    @task(1)
    def serf_screens_application(self):
        screens = self.app.get_screens()
        for screen in screens:
            self.client.get(screen)

    @task(1)
    def change_application(self):
        self.app = get_random_app()

    @task(1)
    def download_application_installer(self):
        self.client.get(self.app.get_installer())

    def on_stop(self):
        pass

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 900




