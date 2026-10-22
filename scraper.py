import subprocess
import json
import os
import tempfile


def run_scraper(username):
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    )

    temp_path = temp_file.name
    temp_file.close()

    try:
        command = [
            "python",
            "-m",
            "scrapy",
            "crawl",
            "nike_profile",
            "-a",
            f"username={username}",
            "-O",
            temp_path,
        ]

        result = subprocess.run(
         command,
         text=True,
       )
        

        if result.returncode != 0:
         return {
        "status": "error",
        "returncode": result.returncode,
    }

        with open(
            temp_path,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        return {
            "status": "success",
            "username": username,
            "count": len(data),
            "data": data,
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)