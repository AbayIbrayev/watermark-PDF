# Watermark PDF Python Script

This script allows you to add a watermark to each page of a PDF file using another PDF file as the watermark.

## Requirements

- Python 3.x
- PyPDF2 library

You can install the required library using pip:

```sh
pip install PyPDF2
```

## Usage

To run the script, use the following command:

```sh
python script.py <input_pdf> <watermark_pdf> <output_pdf>
```

- `<input_pdf>`: Path to the input PDF file that you want to watermark.
- `<watermark_pdf>`: Path to the PDF file that contains the watermark.
- `<output_pdf>`: Path where the output watermarked PDF file will be saved.

## Example

To watermark `input.pdf` with `watermark.pdf` and save the result as `output.pdf`, run:

```sh
python script.py dummy.pdf wtr.pdf marked.pdf
```

This will create a new PDF file `output.pdf` with the watermark applied to each page of `input.pdf`.
