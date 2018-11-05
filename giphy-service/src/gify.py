import logging

import requests

LOGGER = logging.getLogger(__name__)


def get_random_gify(api_key=None, tag='cat'):
    LOGGER.debug(f"Searching for random gify with tag {tag}")
    try:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/random?api_key={api_key}&raiting=PG&tag={tag}")
        request_json = r.json()
        image_url = request_json.get('data', {}).get(
            'images', {}).get('original', {}).get("url", None)
        if not image_url:
            return request_json
        LOGGER.debug(f"Found random {tag.upper()} gif with url: {image_url}")
        return image_url
    except Exception as e:
        LOGGER.debug("Failed to get a url from gify", exc_info=True)
        raise e


def generate_html(api_key=None, tag="cat"):
    gify_reponse = get_random_gify(api_key=api_key, tag=tag)

    if isinstance(gify_reponse, dict):
        LOGGER.debug("We've been rate limited, displaying an error page")
        return f'''<h1> We've been rate limited {gify_reponse}</h1>'''

    LOGGER.debug(f"Displaying gif at url {gify_reponse}")
    return f'<img src="{gify_reponse}">'
