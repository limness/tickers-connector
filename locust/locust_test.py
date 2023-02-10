from locust import HttpUser, task, between
import random


allowed_tickers = {
    "BTC-USDT",
    "SOL-USDT",
    "ETH-USDT",
}


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_get_courses(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        res = self.client.get(
            "/api/courses",
            headers=headers
        )
        print("res", res.json())

    @task(1)
    def test_get_course(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        ticker = random.choice(list(allowed_tickers))
        res = self.client.get(
            f"/api/courses/{ticker}",
            headers=headers
        )
        print(ticker, "res", res.json())
