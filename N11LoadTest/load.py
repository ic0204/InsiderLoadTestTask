from locust import HttpUser, task, constant, TaskSet

import random

search_url = "/arama?q={query}"


class MyResReq(TaskSet):

    @task
    def get_users(self):
        with self.client.get("/", name='Home Page ', catch_response=True) as response:
            if response.status_code == 200:
                print(response.status_code)
                print("user homepage")

    @task
    def get_search(self):
        data = ["xiaomi",
                "galatasaray",
                "mendil",
                "anahtarlık"
                ]

        randomdata = data[random.randint(0, (len(data) - 1))]

        url = "/arama?q=" + randomdata
        name = "Get Search Key " + randomdata + " For Search Bar"
        print(name)
        with self.client.get(url, name=name, catch_response=True) as response:
            print(response.status_code)
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Product check failed")


class anonymousBehavior(HttpUser):
    tasks = [MyResReq]
    wait_time = constant(1)
    host = 'https://www.n11.com'
