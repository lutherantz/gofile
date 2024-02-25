import random
from .app import app
from requests import Session
from flask import render_template, send_file, Response, request

class Routes:
    def __init__(self) -> None:
        self.config = {
            "host": "127.0.0.1",
            "port": "1337",
            "debug": True
        }

        self.routes = {
            "/": {
                "function": self._index,
                "methods": ["GET", "POST"]
            },
            "/upload": {
                "function": self._upload,
                "methods": ["POST"]           
            },
            "/assets/<folder>/<file>": {
                "function": self._assets,
                "methods": ["GET"]           
            }
        }

    def _index(self):
        return 
    
    def _index(self) -> Response:
        return render_template("index.html")
    
    def _upload(self) -> Response:
        try:
            uploaded_files = request.files.getlist('files')

            if not uploaded_files:
                return "No files were uploaded", 400

            sess = Session()

            sess.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            }

            res = sess.get(
                url="https://api.gofile.io/getServers"
            )

            while True:
                randomServer = random.choice(res.json()["data"]["servers"])

                res = sess.head(
                    url=f"https://{randomServer}.gofile.io/"
                )

                if res.status_code == 200:
                    severUrl = f"https://{randomServer}.gofile.io/uploadFile"
                    break

            for file in uploaded_files:
                res = sess.post(
                    url=severUrl,
                    files={
                        "file": (file.filename, file.read())
                    }
                )

            return res.json()["data"]["downloadPage"]

        except Exception as e:
            print(f"Error: {e}")
            return "Internal Server Error", 500
        
    def _assets(self, folder: str, file: str) -> Response:
        try:
            return send_file(f"../assets/{folder}/{file}", as_attachment=False)
        except:
            return "File not found", 404

    @staticmethod
    def page_not_found(e) -> Response:
        return render_template("404.html"), 404