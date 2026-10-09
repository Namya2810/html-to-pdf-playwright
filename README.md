# HTML to PDF Converter

A Python utility that renders a local HTML document as a print-ready A4 PDF using headless Chromium and Playwright.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
python html_to_pdf.py
```

The generated file is saved as `output1.pdf` beside the source HTML.
