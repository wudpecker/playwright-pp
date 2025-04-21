from bs4 import BeautifulSoup, NavigableString, Tag

ALLOWED_TAGS = {
    "a", "button", "input", "textarea", "select", "label",
    "form", "div", "span", "p", "ul", "ol", "li", "section",
    "nav", "header", "footer", "main", "article", "h1", "h2", "h3", "h4"
}

REMOVE_TAGS = {
    "script", "style", "svg", "noscript", "meta", "link", "iframe", "canvas"
}

MAX_TEXT_PER_TAG = 500  # characters
MAX_TOTAL_LENGTH = 100_000  # safety cutoff

def is_visible(tag: Tag) -> bool:
    """Rough check to ignore hidden layout elements"""
    style = tag.get("style", "")
    if "display: none" in style or "visibility: hidden" in style:
        return False
    if tag.has_attr("hidden"):
        return False
    return True

def clean_dom(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Remove script, style, and svg tags
    for tag in soup(["script", "style", "svg", "noscript"]):
        tag.decompose()

    # Remove hidden elements
    for tag in soup.find_all(style=True):
        style = tag["style"].lower()
        if "display:none" in style or "visibility:hidden" in style:
            tag.decompose()

    # Unwrap spans and divs with no attributes
    for tag in soup.find_all(["span", "div"]):
        if not tag.attrs and tag.parent:
            try:
                tag.unwrap()
            except ValueError:
                continue  # Already detached

    return str(soup)
