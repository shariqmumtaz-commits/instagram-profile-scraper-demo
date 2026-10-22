import scrapy
from scrapy_playwright.page import PageMethod
import os
import json
import tempfile


class NikeSpider(scrapy.Spider):
    name = "nike_profile"

    async def start(self):
        username = getattr(self, "username", "adidasoriginals")
        url = f"https://www.instagram.com/{username}/"

        state_json = os.getenv("INSTAGRAM_STATE")

        if state_json:
            state_data = json.loads(state_json)

            temp_state = tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".json",
                delete=False
            )

            json.dump(state_data, temp_state)
            temp_state.close()

            state_file = temp_state.name

        else:
            base_dir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            )

            state_file = os.path.join(
                base_dir,
                "state.json"
            )


        yield scrapy.Request(
            url,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_context_kwargs": {
                    "storage_state": state_file
                },
                "playwright_page_methods": [
                    PageMethod("wait_for_timeout", 5000)
                ]
            },
            callback=self.parse
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        await page.wait_for_timeout(5000)

        try:

            header_text = await page.locator("header").inner_text()

            lines = [
                line.strip()
                for line in header_text.split("\n")
                if line.strip()
            ]

       
            print(lines)

            username = getattr(
                self,
                "username",
                "adidasoriginals"
            )

            full_name = None
            bio = None
            posts = None
            followers = None
            following = None

            for line in lines:
                low = line.lower()

                if "post" in low:
                    posts = line

                elif "follower" in low:
                    followers = line

                elif "following" in low:
                    following = line


            clean_lines = [
                line
                for line in lines
                if not any(
                    word in line.lower()
                    for word in [
                        "post",
                        "follower",
                        "following",
                        "follow",
                        "message"
                    ]
                )
            ]

            if len(clean_lines) >= 2:
                full_name = clean_lines[1]

            if len(clean_lines) >= 3:
                bio = " ".join(clean_lines[2:])

        except Exception as e:
            yield {
                "error": str(e)
            }

            await page.close()
            return

        yield {
            "username": username,
            "full_name": full_name,
            "bio": bio,
            "posts": posts,
            "followers": followers,
            "following": following
        }

        await page.close()