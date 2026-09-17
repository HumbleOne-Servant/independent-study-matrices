import os
import hashlib
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

# Create output directories if they don't exist
os.makedirs("data", exist_ok=True)

def generate_file_signature(file_path):
    """
    Generates a secure SHA-256 cryptographic signature of the file
    and writes it to a verification tracking log.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    signature = sha256_hash.hexdigest()
    
    # Append the signature to a centralized log file
    log_path = "data/signatures.txt"
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"File: {os.path.basename(file_path)}\n")
        log_file.write(f"SHA-256 Signature: {signature}\n")
        log_file.write("-" * 50 + "\n")
        
    return signature

def save_styled_excel(df, file_path, sheet_title='Data Matrix'):
    """
    Saves a pandas DataFrame to an Excel file with professional layouts,
    frozen headers, customized borders, and automated column width fitting.
    """
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_title)
        worksheet = writer.sheets[sheet_title]
        
        # Ensure default grid lines remain visible under background fills
        if worksheet.sheet_view.showGridLines is not None:
            worksheet.sheet_view.showGridLines = True
        
        # Define our Design Styling Palettes
        header_font = Font(name='Segoe UI', size=11, bold=True, color='FFFFFF')
        header_fill = PatternFill(start_color='2C4D75', end_color='2C4D75', fill_type='solid') # Professional Slate Blue
        data_font = Font(name='Segoe UI', size=10)
        
        thin_border = Border(
            left=Side(style='thin', color='D9D9D9'),
            right=Side(style='thin', color='D9D9D9'),
            top=Side(style='thin', color='D9D9D9'),
            bottom=Side(style='thin', color='D9D9D9')
        )
        
        # Freeze the top header row so it stays pinned while scrolling
        worksheet.freeze_panes = 'A2'
        
        # Apply Header Styling
        for col_num in range(1, df.shape[1] + 1):
            cell = worksheet.cell(row=1, column=col_num)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        
        # Apply Data Cell Styling & Text Alignment
        for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=worksheet.max_column):
            for cell in row:
                cell.font = data_font
                cell.border = thin_border
                
                # Smart Alignment: Center shorter codes, Hebrew letters, and genomic markers
                val_str = str(cell.value or '')
                if val_str.startswith('chr') or val_str.startswith('rs') or len(val_str) <= 10:
                    cell.alignment = Alignment(horizontal='center', vertical='center')
                else:
                    cell.alignment = Alignment(horizontal='left', vertical='center')

        # Dynamically Auto-Fit Column Widths to prevent clipped text
        for col_num in range(1, df.shape[1] + 1):
            col_letter = get_column_letter(col_num)
            max_len = len(str(df.columns[col_num - 1])) # Header length
            for val in df.iloc[:, col_num - 1]:
                max_len = max(max_len, len(str(val or '')))
            worksheet.column_dimensions[col_letter].width = max(max_len + 4, 13)

def apply_conditional_formatting(file_path, sheet_title='Data Matrix'):
    """
    Reopens the saved Excel sheet to apply conditional color formatting alerts.
    """
    wb = load_workbook(file_path)
    ws = wb[sheet_title]
    
    # Color palette rule configurations
    red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
    red_font = Font(color='9C0006', bold=True)
    green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
    green_font = Font(color='006100', bold=True)
    yellow_fill = PatternFill(start_color='FFEB9C', end_color='FFEB9C', fill_type='solid')
    yellow_font = Font(color='9C6500', bold=True)
    blue_fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
    blue_font = Font(color='1F4E79', bold=True)
    
    # Custom cell text scanning for dynamic highlights based on context
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            val_str = str(cell.value or '')
            if "Pristine" in val_str or "Beacon" in val_str or "Phenomenon" in val_str:
                cell.fill = green_fill
                cell.font = green_font
            elif "Lethal" in val_str or "Weaponized" in val_str or "Risk" in val_str:
                cell.fill = red_fill
                cell.font = red_font
            elif "Intrusive" in val_str or "Admixture" in val_str or "Sod" in val_str:
                cell.fill = yellow_fill
                cell.font = yellow_font
            elif "Index" in val_str or "Keyword" in val_str:
                cell.fill = blue_fill
                cell.font = blue_font

    wb.save(file_path)

# ==========================================
# FILE 1: ALDOB CHROMOSOME 9 VARIANT MATRIX
# ==========================================
aldob_data = {
    "Gene": ["ALDOB", "ALDOB", "ALDOB", "ALDOB"],
    "Chromosome": ["chr9", "chr9", "chr9", "chr9"],
    "Cytogenetic_Band": ["9q22.3", "9q22.3", "9q22.3", "9q22.3"],
    "Amino_Acid_Change": ["p.Ala149Pro (A149P)", "p.Gly189Val (G189Val)", "p.Arg227Trp (R227W)", "Wild Type (Pristine)"],
    "rsID": ["rs1800546", "rs76992523", "rs113883737", "None"],
    "Genomic_Position_GRCh38": ["chr9:101419730", "chr9:101420104", "chr9:101421033", "Consensus Sequence"],
    "Functional_Impact": [
        "Disrupts homotetramer assembly / severe HFI", 
        "Inactivates aldolase B catalytic site", 
        "Causes structural misfolding / unstable enzyme", 
        "Flawless fructose-to-ATP cellular conversion"
    ],
    "E_Haplogroup_Base_Freq_gnomAD": [0.0000, 0.0000, 0.0000, 1.0000],
    "Steppe_J_R_Lineage_Freq_gnomAD": [0.0071, 0.0024, 0.0019, 0.9886],
    "Selection_Pressure_Classification": [
        "Lethal Selector (High-Fructose Sieve)", 
        "Lethal Selector (High-Fructose Sieve)", 
        "Lethal Selector (High-Fructose Sieve)", 
        "Metabolic Alignment (Fruit & Honey Baseline)"
    ]
}

file_aldob = "data/aldob_variant_matrix.xlsx"
save_styled_excel(pd.DataFrame(aldob_data), file_aldob)
apply_conditional_formatting(file_aldob)
sig_aldob = generate_file_signature(file_aldob)
print(f"✔ Generated & Locked: {file_aldob}")

# ==========================================
# FILE 2: EXPANDED ARCHAEOGENETIC SAMPLE LOG
# ==========================================
archaeo_data = {
    "Sample_ID": ["Raqefet_Cave_1", "Raqefet_Cave_2", "Sidon_Bronze_Age_S1", "Megiddo_Bronze_Age_M3", "Ashkelon_Iron_Age_A1", "Pharaoh_Ramesses_III", "Klin_Yar_III_3", "Punic_Carthage_C2", "Valle_da_Gafaria_V1"],
    "Archaeological_Site": ["Raqefet Cave (Mt. Carmel)", "Raqefet Cave (Mt. Carmel)", "Sidon Maritime Site (Lebanon)", "Megiddo Stratum (Jezreel Valley)", "Ashkelon Sea Wall (Philistia)", "Valley of the Kings", "Caucasus Mountain Barrier", "Carthage Necropolis (Tunisia)", "Lagos Discard Pits (Portugal)"],
    "Historical_Era": ["Epipaleolithic (~12,000 BC)", "Epipaleolithic (~12,000 BC)", "Middle Bronze Age (~1600 BC)", "Late Bronze Age (~1450 BC)", "Early Iron Age (~1150 BC)", "20th Dynasty (~1155 BC)", "Iron Age Exile Window (~750 BC)", "Punic Expansion Era (~300 BC)", "Medieval Inquisition Era (~1493 AD)"],
    "Culture_Context": ["Natufian Core Base Layer", "Natufian Core Base Layer", "Pre-Deportation Coastal Canaanite", "Northern Zagros Migrant Contact Zone", "Sea Peoples Philistine Influx Window", "Northeast African New Kingdom", "Koban Culture Transit Frontier", "Western Mediterranean Phoenician Core", "Iberian Mass Expulsion Discard"],
    "Paternal_Haplogroup_Y_DNA": ["E1b1b1b2 (E-M215)", "E1b1b1b2 (E-M34/E-M123)", "E1b1b1b2a (Canaanite Core)", "J2a1a (Intrusive Mountain Line)", "R1b1a1a (Intrusive Steppe Admixture)", "E1b1a (100% Verified)", "E1a2a1b1b (Outlier Trace)", "E1b1b1b2 (Consolidated Base)", "E1b1a (Dominant Baseline)"],
    "Maternal_Haplogroup_mtDNA": ["N1a", "K1a", "H1bc", "HV1a (Zagros Affinity)", "T2c1a (European Signature)", "Unknown", "J1 (Dual-Uniparental Unit)", "L2a1 (Afro-Asiatic Sun Belt)", "L1b / L2b / L3d"],
    "Autosomal_ALDOB_Status": ["Pristine Tetramer Structure", "Pristine Tetramer Structure", "Pristine Tetramer Structure", "HFI Risk Mutation Carrier", "Hybrid Reduced Tetramer Capacity", "Pristine Tetramer Structure", "Consensus Sequence Trace", "Pristine Tetramer Structure", "Pristine Tetramer Structure"],
    "Targeted_Modern_Descendants": ["São Tomé / Diaspora Base Layer", "São Tomé / Diaspora Base Layer", "Levantine Relict Populations", "Modern Central Asian Substrates", "Evanescent Maritime Influx Traces", "Goshen Crucible Descendants", "Displaced Ten Tribes Remnant", "Maghreb & Andalusian Core Remains", "Bahia & Recife Afro-Descendants"]
}

file_archaeo = "data/archaeogenetic_sample_log.xlsx"
save_styled_excel(pd.DataFrame(archaeo_data), file_archaeo)
apply_conditional_formatting(file_archaeo)
sig_archaeo = generate_file_signature(file_archaeo)
print(f"✔ Generated & Locked: {file_archaeo}")

# ==========================================
# FILE 3: PHILOLOGICAL KEYWORD INDEX MATRIX
# ==========================================
philology_data = {
"Keyword": ["Oth", "Mopheth", "Sheninah", "Sod", "Tsephuni"],"Hebrew_Script": ["אות", "מופת", "שנינה", "סוד", "צפוני"],"Primary_Scripture_Anchor": ["Deuteronomy 28:46", "Deuteronomy 28:46", "Deuteronomy 28:37", "Psalm 83:3", "Psalm 83:3"],"Linguistic_Mechanism": ["The Tracking Beacon", "The Supernatural Phenomenon", "The Weaponized Byword", "The Covert Plot / Superpower Assembly", "The Concealed / Treasured Remnant"],"Analytical_Definition": ["A highly visible structural signal, flag, or material monument left frozen in the historical narrative to identify the scattered target lineage.","A supernatural, future-predicting token defying natural statistics; verified by the multi-generational survival of the E-core genome against mathematical odds.","A piercing, mocking taunt substituted for a population's legitimate legal name and records (e.g., re-classifying under broad color terms).","A highly coordinated political conspiracy between global empires and modern institutional information hubs to execute geographical re-labeling.","The hidden, densely covered house of Jacob (the converged Haplogroup E substrate) obscured beneath the overlayers of historical scattering."]}file_philology = "data/philological_keyword_index.xlsx"save_styled_excel(pd.DataFrame(philology_data), file_philology, sheet_title='Philological Matrix')apply_conditional_formatting(file_philology, sheet_title='Philological Matrix')sig_philology = generate_file_signature(file_philology)print(f"✔ Generated & Locked: {file_philology}")print("\n🎉 PHASE II THREE-SHEET DATABASE COMPILATION COMPLETE!")