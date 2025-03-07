import pandas as pd
from questionnaire_analysis.questionnaires import (
    ucla, dtcgt, PANAS, ras, GCF_c, ECR_c, mspss, SWLS, ALQ, BEQ, IRQ_t,
    cesdr, mini_MASQ, PMERQ, BFI, su, EERQ, hexaco, care, SD4, cbcl, upps,
    BSSS, sias, pss, LOTR_t, DOSPERT, ippa
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
    "UCLA_": ucla.main,
    "DTCGT_": dtcgt.main,
    "PANAS_": PANAS.main,
    "RAS_": ras.main,
    "GCF_": GCF_c.main,
    "ECR_": ECR_c.main,
    "MSPSS_": mspss.main,
    "SWLS_": SWLS.main,
    "ALQ_": ALQ.main,
    "BEQ_": BEQ.main,
    "IRQ_": IRQ_t.main,
    "CESDR_": cesdr.main,
    "MASQ_": mini_MASQ.main,
    "PMERQ_": PMERQ.main,
    "BFI_": BFI.main,
    "SU_": su.main,
    "EERQ_": EERQ.main,
    "HEXACO_": hexaco.main,
    "CARE_": care.main,
    "SD4_": SD4.main,
    "CBCL_": cbcl.main,
    "UPPS_": upps.main,
    "BSSS_": BSSS.main,
    "SIAS_": sias.main,
    "PSS_": pss.main,
    "LOTR_": LOTR_t.main,
    "DOSPERT_": DOSPERT.main,
    "IPPA_": ippa.main
}
    detected = {}
    for prefix, main_fn in questionnaire_map.items():
        if any(col.startswith(prefix) for col in df.columns):
            detected[prefix] = main_fn
    return detected



