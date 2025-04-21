def build_prompt(type_: str, **kwargs) -> str:
    if type_ == "selector":
        return f"""
You are a world-class front-end expert and assistant. Your job is to extract a **valid CSS selector** for a specific interactive element in the following HTML DOM.

---

### 🔍 Task
Your task is to identify the **best CSS selector** for a **visible, clickable** `<a>` link that a user would click to go to:

**\"{kwargs["description"]}\"**

---

### 📜 HTML DOM
```html
{kwargs["html"]}
```

---

### ✅ Valid Answer Requirements

You must follow ALL these instructions:

1. **Return only a single CSS selector string. No explanations.**
2. The selector must target an `<a>` tag with **visible text content**.
3. The selector must be a **standard CSS selector** that is compatible with:
   - `document.querySelectorAll(...)`
   - Playwright
   - Chromium-based browsers

4. ❌ Do **NOT** use:
   - `:contains(...)` – Not supported in real CSS
   - jQuery-style selectors
   - XPath
   - Selenium-only syntax
   - Explanations or commentary

5. ✅ Do use:
   - Standard CSS attribute selectors, tag selectors, class selectors, id selectors, etc.
   - Relative specificity. Be as specific as possible while still being robust.

6. ✨ Bonus (but optional) rules for great selectors:
   - Prefer links in **navbars**, **footers**, or primary CTAs.
   - Avoid dropdown menu duplicates, hidden elements, or skeleton components.
   - Use attributes like `href`, `role`, or `aria-*` when helpful.

---

### ✉️ Output Example (correct):
```css
a[href="/pricing"]
```

### ❌ Bad Outputs (do NOT do these):
```css
a:contains("Pricing")
```
```xpath
//a[text()="Pricing"]
```
```text
Here is your selector: a[href='/pricing']
```

Just return this:
```css
a[href="/pricing"]
```

Only output the CSS selector and nothing else.
"""

    elif type_ == "ask":
        return f"""
You are a helpful assistant who answers questions about a webpage.

Here is the page DOM:
{kwargs["html"]}

Here is the question:
{kwargs["question"]}

{f"Extra context: {kwargs['context']}" if kwargs.get('context') else ""}
"""
    else:
        raise ValueError(f"Unknown prompt type: {type_}")