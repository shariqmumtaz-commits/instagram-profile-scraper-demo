from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # visible browser
    context = browser.new_context()

    page = context.new_page()

    # 👉 Open Instagram login
    page.goto("https://www.instagram.com/accounts/login/")

    print("👉 Please log in manually in the opened browser...")
    input("Press ENTER after login is complete...")

    # 💾 Save login session
    context.storage_state(path="state.json")

    print("✅ Login session saved as state.json")

    browser.close()