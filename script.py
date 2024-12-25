import sys

import PyPDF2
from PyPDF2.errors import PdfReadError


def watermark(input_pdf_path, watermark_pdf_path, output_pdf_path):
    try:
        with open(input_pdf_path, "rb") as input_file, open(watermark_pdf_path, "rb") as watermark_file:
            input_pdf = PyPDF2.PdfReader(input_file)
            watermark_pdf = PyPDF2.PdfReader(watermark_file)
            output_pdf = PyPDF2.PdfWriter()

            watermark_page = watermark_pdf.pages[0]

            for page in input_pdf.pages:
                page.merge_page(watermark_page)
                output_pdf.add_page(page)

            with open(output_pdf_path, "wb") as output_file:
                output_pdf.write(output_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PdfReadError as e:
        print(f"Error reading PDF file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_pdf> <watermark_pdf> <output_pdf>")
    else:
        watermark(sys.argv[1], sys.argv[2], sys.argv[3])
