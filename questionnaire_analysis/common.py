import pandas as pd
# from questionnaire_analysis.questionnaires import cbcl, eerq, upps  # import other modules as needed
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
        'CBCL_': cbcl.main,
        'EERQ_': eerq.main,
        'UPPS_': upps.main,
        
    }
    detected = {}
    for prefix, main_fn in questionnaire_map.items():
        if any(col.startswith(prefix) for col in df.columns):
            detected[prefix] = main_fn
    return detected



