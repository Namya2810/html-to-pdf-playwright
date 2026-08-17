from pathlib import Path
from playwright.sync_api import sync_playwright

project_dir = Path(__file__).resolve().parent
html_file = project_dir / "Sample1.html"
output_file = project_dir / "output1.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(html_file.as_uri(), wait_until="networkidle")
    page.pdf(
        path=str(output_file),
        format="A4",
        print_background=True
    )
    browser.close()

print("PDF generated successfully!")
