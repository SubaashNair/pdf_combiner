import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def combine_pdfs_from_uploads(uploaded_files):
    writer = PdfWriter()
    
    # Sort files by name (optional)
    uploaded_files = sorted(uploaded_files, key=lambda x: x.name)
    
    for uploaded_file in uploaded_files:
        reader = PdfReader(uploaded_file)
        num_pages = len(reader.pages)
        
        # Add each page from the uploaded PDF
        for page in reader.pages:
            writer.add_page(page)
        
        # Add a blank page if the PDF has an odd number of pages
        if num_pages % 2 != 0:
            if num_pages > 0:
                last_page = reader.pages[-1]
                width = last_page.mediabox.width
                height = last_page.mediabox.height
            else:
                width, height = 595, 842  # Default A4 dimensions
            writer.add_blank_page(width=width, height=height)
    
    # Write the combined PDF to a BytesIO object
    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)
    return output_stream

st.title("PDF Combiner with Even-Page Enforcement")
st.write("Upload your PDF files (select multiple files at once) to combine them into one PDF. A blank page will be added for PDFs with an odd number of pages.")

# Use the file uploader to let users select multiple PDF files
uploaded_files = st.file_uploader("Select PDF files", type=["pdf"], accept_multiple_files=True)

if st.button("Combine PDFs"):
    if uploaded_files:
        try:
            combined_pdf = combine_pdfs_from_uploads(uploaded_files)
            st.success("PDFs combined successfully!")
            st.download_button("Download Combined PDF", data=combined_pdf, file_name="combined.pdf", mime="application/pdf")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload at least one PDF file.")