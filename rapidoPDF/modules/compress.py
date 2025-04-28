import subprocess
import os


def get_file_size(file_path):
    """
    Get the size of a file in Ko, round to 2 decimal places.
    """

    sizes=os.path.getsize(file_path)/1024
    return round(sizes,2)





def compress_pdf(input_path: str, output_path: str,compression_level: str = "/screen"):

    """
    Compress a PDF file using Ghostscript.
    :param input_path: Path to the input PDF file.
    :param output_path: Path to save the compressed PDF file.
    """



    try:
        subprocess.run([
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={compression_level}",  
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path
        ], check=True)
        print(f"✅ Compression succeeded : {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error Ghostscript : {e}")
