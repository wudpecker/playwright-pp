# main.py

from playwrightpp.driver import PlaywrightLLMDriver

driver = PlaywrightLLMDriver()
def take_screenshot():
    driver.page.screenshot(path="debug/screenshot.png")
try:
    driver.get("https://www.stripe.com/")
    driver.page.wait_for_timeout(2000)  # Wait for the page to load
    take_screenshot()
    pricing_link = driver.find_element("llm", "A link to visit the pricing page").click()
    driver.page.wait_for_timeout(2000)  # Wait for the page to load
    take_screenshot()
    print("Current URL:", driver.current_url())
    answer = driver.ask("Yes or No: Do they have a seat or per user based pricing model? Just the reason for yes or no anwer with one line.")
    print("Answer:", answer)
    answer = driver.ask("What plans are offered and what's their pricing?")
    print("Answer:", answer)

finally:
    driver.quit()
