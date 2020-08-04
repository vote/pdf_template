# pdf_template

Small wrapper around pdftk for filling and signing PDFs

Example:

```py
from pdf_template import PDFTemplate, PDFTemplateSection, SignatureBoundingBox

input_data = {
    "is_18_or_over": True,
    "title_mr": False,
    "title_ms": True,
    "first_name": "Foo",
    "last_name": "Bar",
    "address1": "None",
    "zipcode": None,
    "mailto_line_1": "some address!",
}

template = PDFTemplate(
    [
        PDFTemplateSection(path="tests/test-input-page-1.pdf", is_form=True),
        PDFTemplateSection(
            path="tests/test-input-page-2-3.pdf",
            is_form=True,
            signature_locations={
                1: SignatureBoundingBox(x=300, y=490, width=200, height=37)
            },
        ),
        PDFTemplateSection(
            path="tests/test-input-page-4.pdf",
            signature_locations={
                1: SignatureBoundingBox(x=188, y=50, width=200, height=28)
            },
        ),
    ]
)

with template.fill(
    input_data, signature=Image.open("tests/sig.jpeg")
) as output_pdf:
    with open("output.pdf") as out_file:
        out_file.write(output_pdf.read())
```
