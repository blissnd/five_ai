import unittest
from src.gify import get_random_gify, generate_html
import requests_mock


class classname(unittest.TestCase):

    def test_get_working_url(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                f"https://api.giphy.com/v1/gifs/random?api_key=test&raiting=PG&tag=cat",
                json={"data": {"images": {"original": {"url": "https://media3.giphy.com/media/10SExFZRVjG7Xq/giphy.gif"}}}})
            resp_url = get_random_gify("test", "cat")
        self.assertEqual(
            resp_url, "https://media3.giphy.com/media/10SExFZRVjG7Xq/giphy.gif")

    def test_get_working_url_html(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                f"https://api.giphy.com/v1/gifs/random?api_key=test&raiting=PG&tag=cat",
                json={"data": {"images": {"original": {"url": "https://media3.giphy.com/media/10SExFZRVjG7Xq/giphy.gif"}}}})
            resp = generate_html("test", "cat")
        self.assertEqual(
            resp, '<img src="https://media3.giphy.com/media/10SExFZRVjG7Xq/giphy.gif">')

    def test_html_in_rate_limit(self):
        fail_json = {"message": "rate limit exceeded"}
        with requests_mock.Mocker() as mock:
            mock.get(
                f"https://api.giphy.com/v1/gifs/random?api_key=test&raiting=PG&tag=cat", json=fail_json
            )
            resp = generate_html("test", "cat")
        self.assertEqual(resp, 
                         f'''<h1> We've been rate limited {fail_json}</h1>'''
                         )
