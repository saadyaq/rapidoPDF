# app.py

from modules.compress import compress_pdf, get_file_size
from modules.pdf_to_word import pdf_to_word
from modules.word_to_pdf import word_to_pdf
import os

def compress_pdf_flow():
    input_pdf= input("Entrez le chemin du fichier PDF à compresser : ").strip()
    
    if not os.path.exists(input_pdf):
        print("❌ Le fichier n'existe pas.")
        return
    
    print("Choisissez le niveau de compression:")

    levels={
        "1":"/screen (Qualité écran -très léger)",
        "2":"/ebook (Qualité ebook - léger)",
        "3": "/printer (Qualité imprimante - bonne)",
        "4": "/prepress (Qualité prépresse - très bonne)",
        "5": "/default (Qualité par défaut)"
    }

    for key,desc in levels.items():
        print(f"{key}: {desc}")
    
    choice = input("Entrez votre choix (1-5): ").strip()
    if choice not in levels:
        print("❌ Choix invalide.")
        return
    
    compression_level= {
        "1": "/screen",
        "2": "/ebook",
        "3": "/printer",
        "4": "/prepress",
        "5": "/default"
    }

    base_name= os.path.basename(input_pdf)
    output_pdf=os.path.join("outputs",f"compressed_{base_name}")

    size_before= get_file_size(input_pdf)
    print(f"📦 Taille avant compression : {size_before} Ko")

    compress_pdf(input_pdf, output_pdf,compression_level[choice])

    if os.path.exists(output_pdf):
        size_after= get_file_size(output_pdf)
        print(f"📦 Taille après compression : {size_after} Ko")
        gain=round(100*(size_before-size_after)/size_before,2)
        print(f"📉 Gain de taille : {gain} %")
    else :
        print("❌ La compression a échoué.")

def pdf_to_word_flow():

    input_pdf=input("Entrez le chemin du fichier PDF à convertir : ").strip()
    if not os.path.exists(input_pdf):
        print("❌ Le fichier n'existe pas.")
        return
    base_name= os.path.basename(input_pdf)
    output_docx=os.path.join("outputs",f"converted_{base_name}.docx")
    pdf_to_word(input_pdf, output_docx)

def word_to_pdf_flow():

    input_docx=input("📄 Entrez le chemin du fichier Word à convertir en PDF : ").strip()
    if not os.path.exists(input_docx):
        print("❌ Le fichier n'existe pas.")
        return
    base_name= os.path.splitext(os.path.basename(input_docx))[0]
    output_pdf=os.path.join("outputs",f"converted_{base_name}.pdf")
    word_to_pdf(input_docx, output_pdf)



def main():
    print("Bienvenue dans RapidoPDF!")
    print("1. Compresser un fichier PDF")
    print("2. Convertir un fichier PDF en Word")
    print("3. Convertir un fichier Word en PDF")
    choice = input("Choisissez une option (1-3): ").strip()

    if choice == "1":
        main()
    elif choice == "2":
        pdf_to_word_flow()
    elif choice == "3":
        word_to_pdf_flow()
    else:
        print("❌ Choix invalide.")


if __name__ == "__main__":
    main()
