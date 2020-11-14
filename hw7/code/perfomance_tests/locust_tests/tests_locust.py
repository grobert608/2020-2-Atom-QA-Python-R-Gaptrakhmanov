from locust import HttpUser, TaskSet, task, between


class PostsBehavior(TaskSet):

    @task
    def posts(self):
        self.client.get("/posts")

    @task
    def comments(self):
        self.client.get("/comments")


class PhotosBehavior(TaskSet):

    @task
    def albums(self):
        self.client.get("/albums")

    @task
    def photos(self):
        self.client.get("/photos")


class UsersBehavior(TaskSet):

    @task
    def users(self):
        self.client.get("/users")


class WebsiteUser(HttpUser):
    tasks = [PostsBehavior, PhotosBehavior, UsersBehavior]
    wait_time = between(1, 2)
