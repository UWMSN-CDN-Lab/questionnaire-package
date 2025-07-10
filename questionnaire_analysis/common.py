import pandas as pd
from questionnaire_analysis.questionnaires import (
UCLA, PANAS, RAS, GCF, ECR, MSPSS, SWLS, ALQ, BEQ, IRQ,
CESDR, MINI_MASQ, PMERQ, BFI, SU, EERQ, HEXACO, CARE, SD4, CBCL, UPPS,
BSSS, SIAS, PSS, LOTR, DOSPERT, IPPA
)

def access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Questionnaire List 
def detect_questionnaires(df):
    questionnaire_map = {
    "UCLA_": UCLA.main,
    "PANAS_": PANAS.main,
    "RAS_": RAS.main,
    "GCF_": GCF.main,
    "ECR_": ECR.main,
    "MSPSS_": MSPSS.main,
    "SWLS_": SWLS.main,
    "ALQ_": ALQ.main,
    "BEQ_": BEQ.main,
    "IRQ_": IRQ.main,
    "CESDR_": CESDR.main,
    "MASQ_": MINI_MASQ.main,
    "PMERQ_": PMERQ.main,
    "BFI_": BFI.main,
    "SU_": SU.main,
    "EERQ_": EERQ.main,
    "HEXACO_": HEXACO.main,
    "CARE_": CARE.main,
    "SD4_": SD4.main,
    "CBCL_": CBCL.main,
    "UPPS_": UPPS.main,
    "BSSS_": BSSS.main,
    "SIAS_": SIAS.main,
    "PSS_": PSS.main,
    "LOTR_": LOTR.main,
    "DOSPERT_": DOSPERT.main,
    "IPPA_": IPPA.main
}
    detected = {}
    for prefix, main_fn in questionnaire_map.items():
        if any(col.startswith(prefix) for col in df.columns):
            detected[prefix] = main_fn
    return detected
def analyze_questionnaire_csv(csv_path, output_summary=True):
    """
    Loads a CSV, detects questionnaires, runs analyses, and returns or saves the summary.
    """
    df = access_csv(csv_path)
    if df is None:
        return None

    detected = detect_questionnaires(df)
    if not detected:
        print("No recognized questionnaires detected in the CSV.")
        return None

    # Run all detected questionnaires and concatenate results
    summary_dfs = []
    for prefix, main_fn in detected.items():
        print(f"Processing questionnaire with prefix '{prefix}'...")
        try:
            summary_df = main_fn(df)
            if summary_df is not None:
                summary_dfs.append(summary_df)
        except Exception as e:
            print(f"Error processing questionnaire '{prefix}': {e}")
            continue

    # Combine all summaries (if multiple)
    if summary_dfs:
        final_summary = pd.concat(summary_dfs, axis=1)
        if output_summary:
            summary_output_path = csv_path.replace(".csv", "_summary.csv")
            final_summary.to_csv(summary_output_path, index=False)
            print(f"Summary saved to: {summary_output_path}")
        return final_summary
    return None