from PyPDF2 import PdfMerger    

def merge_pdfs(input_paths, output_path):

    """ 
    Merges multiple pdf files into one single pdf file.
    Args:
        input_paths (list): List of paths to the input pdf files.
        output_path (str): Path to the output merged pdf file.
    """

    try : 
        merger=PdfMerger()
        for pdf in input_paths:
            merger.append(pdf)
        merger.write(output_path)
        merger.close()
        print(f"PDFs merged successfully into {output_path}")
   
    except Exception as e:
        print(f"An error occurred while merging PDFs: {e}")
        return False
    