import re
from playwright.sync_api import Page, expect

def test_get_started_streamlit(page: Page):
    page.goto("http://localhost:8501")
    #page.get_by_role("button", name="テス").click()
    page.get_by_role("button", name="送信").click()
