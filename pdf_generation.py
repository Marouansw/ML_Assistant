import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos  # For new positioning system


# Lire le fichier Excel
df = pd.read_excel('donnee_use_case.xlsx', sheet_name='Feuil1')

# Créer un objet PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12, style='B')

# Ajouter un titre
pdf.cell(200, 10, txt="Données d'utilisation des clients", ln=True, align='C')
pdf.ln(10)  # Ajouter un espace

# Parcourir les données et les ajouter au PDF
for index, row in df.iterrows():
    univers = row['Univers']
    variable = row['Variable']
    description = row['Description']
    segmentation = "Oui" if row['Segmentation'] == "X" else "Non"
    churn = "Oui" if row['Churn'] == "X" else "Non"
    nb = row['Nb']

    # Ajouter les informations structurées
    pdf.cell(200, 10, text=f"Univers : {univers}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, text=f"Variable : {variable}", ln=True)
    pdf.cell(200, 10, text=f"Description : {description}", ln=True)
    pdf.cell(200, 10, text=f"Utilisé pour effectuer la segmentation : {segmentation}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(200, 10, text=f"  Predire le Churn : {churn}", ln=True)
    pdf.cell(200, 10, text=f"Nb : {nb}", ln=True)
    pdf.ln(10)  # Ajouter un espace entre les entrées

# Sauvegarder le PDF
pdf.output("donnee_use_case_structuré.pdf")