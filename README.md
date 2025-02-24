# PDF Combiner with Even-Page Enforcement

This project is a simple Streamlit application that lets you combine multiple PDF files into a single PDF. It automatically adds a blank page if any PDF has an odd number of pages, ensuring that every document ends on an even page—ideal for duplex printing or presentations.

## Features

- **Multiple File Upload:** Select and upload multiple PDF files at once.
- **Even-Page Enforcement:** Automatically adds a blank page to PDFs with an odd number of pages.
- **Combined Output:** Generates a single PDF that merges all uploaded files.
- **Easy Download:** Download the resulting combined PDF directly from your browser.

## Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/subaashnair/pdf-combiner.git
   cd pdf-combiner