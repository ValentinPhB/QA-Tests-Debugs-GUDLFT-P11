from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def on_start(self):
        self.client.get("/")

    @task
    def table(self):
        self.client.get("/table")

    @task
    def showsummary(self):
        self.client.post(
            '/showSummary', data={'email': 'john@simplylift.co'})
        
    @task
    def book(self):
        self.client.get('/book/Fall Classic/Simply Lift')

    @task
    def purchasePlaces(self):
        self.client.post(
            '/purchasePlaces', data={'club': 'Simply Lift', 'competition': "Fall Classic", 'places': 3})
    @task
    def on_stop(self):
        self.client.get("/logout")
