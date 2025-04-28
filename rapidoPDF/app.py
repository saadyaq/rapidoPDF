# app.py

from modules.compress import compress_pdf, get_file__size
import os

def main():
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

    size_before= get_file__size(input_pdf)
    print(f"📦 Taille avant compression : {size_before} Ko")

    compress_pdf(input_pdf, output_pdf)

    if os.path.exists(output_pdf):
        size_after= get_file__size(output_pdf)
        print(f"📦 Taille après compression : {size_after} Ko")
        gain=round(100*(size_before-size_after)/size_before,2)
        print(f"📉 Gain de taille : {gain} %")
    else :
        print("❌ La compression a échoué.")

if __name__ == "__main__":
    main()
