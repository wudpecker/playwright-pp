# playwrightpp/driver.py

from playwright.sync_api import sync_playwright
from playwrightpp.llm import LLM
from playwrightpp.dom_cleaner import clean_dom  # reuse your cleaner

class PlaywrightLLMDriver:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()
    
    def get(self, url):
        self.page.goto(url)

        
    def find_element(self, by, value):
        if by == "llm":
            raw_html = self.page.content()
            clean_html = clean_dom(raw_html)
            selector = LLM.prompt("selector", description=value, html=clean_html)
            el = self.page.locator(selector).first
            el.wait_for(state="visible", timeout=5000)
            return el
        else:
            raise NotImplementedError("Only By.LLM is currently supported")
    def ask(self, question: str, additional_context: str = "") -> str:
        raw_html = self.page.content()
        clean_html = clean_dom(raw_html)

        answer = LLM.prompt(
            "ask",
            html=clean_html,
            question=question,
            context=additional_context,
        )
        return answer


    def current_url(self):
        return self.page.url

    def quit(self):
        self.browser.close()
        self.playwright.stop()
