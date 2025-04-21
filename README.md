# Playwright++

**Playwright++** is a lightweight Python framework that augments browser automation with LLM-powered helpers. It now uses [Playwright](https://playwright.dev/python/) for better reliability and modern capabilities.

---

## 🌍 What It Does

### Core Features

- `driver.find_element("llm", "natural language description")`

  - Use a prompt to describe an element, and LLM returns a **valid CSS selector**.

- `driver.ask("question about the page")`

  - Ask a natural-language question about the content of the page.

- Built-in DOM cleaner to avoid polluting the LLM prompt with scripts, hidden elements, or SVG noise.

- Debug with screenshots: take automatic or manual snapshots while testing prompts or navigation.

---

## 🚀 Quickstart

### Folder Structure

```
selenium-plus-plus/
├── main.py
├── .env
├── debug/                  # Screenshots saved here
├── playwrightpp/
│   ├── __init__.py
│   ├── driver.py           # Playwright-based driver with LLM helpers
│   ├── dom_cleaner.py      # Trims noisy elements from page HTML
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── openai_provider.py
│   │   └── prompts.py      # Prompt templates for selectors/questions
```

### Setup

```bash
# Install dependencies
pip install playwright openai beautifulsoup4 python-dotenv
playwright install chromium

# Set up your OpenAI API key
echo "OPENAI_API_KEY=sk-..." > .env
```

---

## 🔮 Example Usage

```python
from playwrightpp.driver import PlaywrightLLMDriver

driver = PlaywrightLLMDriver()
try:
    driver.get("https://userlens.io/")
    driver.page.screenshot(path="debug/screenshot_1.png")

    pricing_link = driver.find_element("llm", "A link to visit the pricing page")
    print("Text:", pricing_link.inner_text())
    print("URL:", pricing_link.get_attribute("href"))

    pricing_link.click()
    driver.page.wait_for_url("**/pricing")

    print("Current URL:", driver.current_url())
    print("Answer:", driver.ask("What plans are offered and what's their pricing?"))

finally:
    driver.quit()
```

---

## 💡 How it Works

- The DOM is first cleaned with BeautifulSoup to remove:
  - `<script>`, `<style>`, `<svg>`, `display:none`, etc.
- A prompt is generated using `prompts.py`.
- The prompt is sent to OpenAI via the provider layer.
- The returned CSS selector is used in `page.locator(...).first`.
- Screenshots are taken at any point for debugging.

---

## 📅 Roadmap / Nice-to-Haves

- Smart multi-step navigation
- Form filling with LLM suggestions
- Better error handling / fallbacks when selectors fail
- Support for other LLMs (Anthropic, Mistral, etc.) via the provider interface

---

## 🌍 License

This is an internal project, not intended for open-source distribution.

---

Made with ❤️ by Wudpecker
