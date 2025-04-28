from pdf2docx import Converter 

def pdf_to_word(input_pdf, output_docx):
    """
    Convert a pdf file to a Word document.
    :param input_pdf: Path to the input PDF file.
    :param output_docx: Path to the output Word document.
    """

    try:

        cv=Converter(input_pdf)
        cv.convert(output_docx)
        cv.close()
        print(f"Successfully converted '{input_pdf}' to '{output_docx}'")
    except Exception as e:  
        print(f"An error occurred: {e}")