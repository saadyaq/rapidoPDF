import subprocess
import os

def word_to_pdf(input_docx,output_pdf):
    """
    Convvert Word document to PDF document.
    :param input_docx: Path to the input Word document.
    :param output_pdf: Path to the output PDF file.
    """

    try:

        output_dir= os.path.dirname(output_pdf) if output_pdf else os.path.dirname(input_docx)
        subprocess.run([
            'libreoffice',
            '--headless',
            '--convert-to',
            'pdf',
            '--outdir',
            output_dir,
            input_docx
        ], check=True)

        if output_pdf is None:
            # Rename the output file if a specific output path is provided
            output_pdf= os.path.splitext(input_docx)[0] + '.pdf'


    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False