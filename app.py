import streamlit as st
from PyPDF2 import PdfMerger
from PIL import Image
import io

st.set_page_config(page_title="PDF Merger & Image Resizer", layout="centered")

st.title("🛠️ PDF Merger & Image Resizer App")

tab1, tab2 = st.tabs(["📄 PDF Merger", "🖼️ Image Resizer"])

# PDF Merger Tab
with tab1:
    st.header("📄 Merge your PDF files")
    pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

    if st.button("Merge PDFs"):
        if pdf_files:
            merger = PdfMerger()
            for pdf in pdf_files:
                merger.append(pdf)

            merged_pdf = io.BytesIO()
            merger.write(merged_pdf)
            merger.close()

            st.success("✅ PDF files merged successfully!")
            st.download_button("Download Merged PDF", data=merged_pdf.getvalue(), file_name="merged.pdf", mime="application/pdf")
        else:
            st.warning("Please upload at least 2 PDF files.")

# Image Resizer Tab
with tab2:
    st.header("🖼️ Resize your image")
    image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if image_file:
        img = Image.open(image_file)
        st.image(img, caption="Original Image", use_column_width=True)

        width = st.number_input("Enter width", value=img.width)
        height = st.number_input("Enter height", value=img.height)

        if st.button("Resize Image"):
            resized_img = img.resize((int(width), int(height)))
            st.image(resized_img, caption="Resized Image", use_column_width=True)

            img_byte_arr = io.BytesIO()
            resized_img.save(img_byte_arr, format='PNG')
            st.download_button("Download Resized Image", data=img_byte_arr.getvalue(), file_name="resized_image.png", mime="image/png")
