from os import system
import shutil
import os

from bottle import get, put, post, run, request


def rmdir(path):
    try:
        shutil.rmtree(path, ignore_errors=True)
        print(f"Attempted to remove {path}")
    except Exception as e:
        print(f"Unexpected error: {e}")


@get("/api/deploy_wh")
@put("/api/deploy_wh")
@post("/api/deploy_wh")
def deploy_wh():
    rmdir("/tmp/myapp")
    system("git clone git@github.com:MartinBaunWorld/vercel-light-play.git /tmp/myapp")
    system("/tmp/myapp/build")
    print("Deployed")

run()
