import streamlit as st
import os
from modules.compress import compress_pdf, get_file_size
from modules.pdf_to_word import pdf_to_word
from modules.word_to_pdf import word_to_pdf
from modules.merge import merge_pdfs

# Configuration
st.set_page_config(page_title="RapidoPDF", layout="centered")

# Titre
st.title("🚀 RapidoPDF - Traitement de vos fichiers PDF")

# Menu principal
option = st.sidebar.selectbox(
    "Choisissez une action",
    (
        "Accueil",
        "Compresser un PDF",
        "Convertir PDF ➔ Word",
        "Convertir Word ➔ PDF",
        "Fusionner plusieurs PDF"
    )
)

# 📄 Dossier temporaire
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

if option == "Accueil":
    st.write("Bienvenue sur **RapidoPDF** ! Sélectionnez une action dans le menu à gauche.")

elif option == "Compresser un PDF":
    uploaded_file = st.file_uploader("📤 Uploadez votre fichier PDF", type=["pdf"])
    if uploaded_file:
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        output_path = os.path.join(OUTPUT_DIR, f"compressed_{uploaded_file.name}")
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        level_friendly = st.selectbox(
            "Choisissez la qualité de sortie souhaitée :",
            (
                "Compression maximale (qualité faible)",
                "Compression standard (ebook)",
                "Bonne qualité (impression)",
                "Très haute qualité (publication)",
                "Compression par défaut"
            )
        )
        if st.button("Compresser"):
            size_before = get_file_size(input_path)
            level_mapping = {
                "Compression maximale (qualité faible)": "/screen",
                "Compression standard (ebook)": "/ebook",
                "Bonne qualité (impression)": "/printer",
                "Très haute qualité (publication)": "/prepress",
                "Compression par défaut": "/default"
            }
            compression_level = level_mapping[level_friendly]
            compress_pdf(input_path, output_path, compression_level)
            size_after = get_file_size(output_path)
            st.success("Compression terminée ✅")
            st.write(f"📏 Taille avant : {size_before} Ko")
            st.write(f"📏 Taille après : {size_after} Ko")
            st.write(f"💡 Gain : {round(100 * (size_before - size_after) / size_before, 2)} %")
            with open(output_path, "rb") as f:
                st.download_button("📥 Télécharger le PDF compressé", f, file_name=os.path.basename(output_path))

elif option == "Convertir PDF ➔ Word":
    uploaded_file = st.file_uploader("📤 Uploadez votre fichier PDF", type=["pdf"])
    if uploaded_file:
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(uploaded_file.name)[0]}.docx")
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        if st.button("Convertir en Word"):
            pdf_to_word(input_path, output_path)
            st.success("Conversion terminée ✅")
            with open(output_path, "rb") as f:
                st.download_button("📥 Télécharger le fichier Word", f, file_name=os.path.basename(output_path))

elif option == "Convertir Word ➔ PDF":
    uploaded_file = st.file_uploader("📤 Uploadez votre fichier Word", type=["docx"])
    if uploaded_file:
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(uploaded_file.name)[0]}.pdf")
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        if st.button("Convertir en PDF"):
            word_to_pdf(input_path, output_path)
            st.success("Conversion terminée ✅")
            with open(output_path, "rb") as f:
                st.download_button("📥 Télécharger le PDF", f, file_name=os.path.basename(output_path))

elif option == "Fusionner plusieurs PDF":
    uploaded_files = st.file_uploader("📤 Uploadez plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)
    if uploaded_files:
        input_paths = []
        for uploaded_file in uploaded_files:
            path = os.path.join(UPLOAD_DIR, uploaded_file.name)
            with open(path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            input_paths.append(path)
        output_path = os.path.join(OUTPUT_DIR, "merged_output.pdf")
        if st.button("Fusionner"):
            merge_pdfs(input_paths, output_path)
            st.success("Fusion terminée ✅")
            with open(output_path, "rb") as f:
                st.download_button("📥 Télécharger le PDF fusionné", f, file_name="merged_output.pdf")
