from locust import HttpUser, task, between

class LocustTest(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def showSummary(self):
        response = self.client.post("/showSummary", {"email":"john@simplylift.co"})
    
    @task
    def changeClub(self):
        response = self.client.get("/changeClub/Simply Lift")

    @task
    def book(self):
        response = self.client.get("/book/Spring Festival/Simply Lift")

    @task
    def purchasePlaces(self):
        response = self.client.post("/purchasePlaces", {
            "competition":"Spring Festival",
            "club":"Simply Lift",
            "places":"2"
        })

    @task
    def logout(self):
        response = self.client.get("/logout")
    

    