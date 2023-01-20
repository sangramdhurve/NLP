import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)


    @task
    def read_root(self):
        self.client.get("/")

    @task
    def prediction(self):
        self.client.post(url="/predict", json={"text" : "This is for testing the data file, through the upcoming entries form web"})