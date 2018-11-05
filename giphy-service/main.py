#!/usr/bin/env python3
import logging
import sys

import cherrypy as cp

from src.gify import generate_html

LOGGER = logging.getLogger(__name__)

#API_KEY = "7Erd2gbuRzazxRXR1yfMq6J2FEwYNXAX"
API_KEY = "zR6ucowViYKngIJDz25M3K13NmPaZkQ8"

class CatServer:


    def index(self):
        return generate_html(api_key=API_KEY)
    index.exposed = True


def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    cp.config.update(
        {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 5000
        }
    )
    cp.quickstart(CatServer())


if __name__ == "__main__":
    main()
