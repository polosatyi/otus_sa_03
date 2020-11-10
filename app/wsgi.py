# -*- coding: utf-8 -*-
from application import create_app
from time import sleep


app = create_app()


if __name__ == "__main__":
    sleep(1)
    app.run(host="0.0.0.0", port="8000")
