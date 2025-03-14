from .common import access_csv, detect_questionnaires

def main():
    input_file_path = '/Users/ayusmankhuntia/Desktop/Package/questionnaire-package/questionnaire_analysis/Risk-Taking+and+Emotion+Regulation_February+4,+2025_15.23.csv'  # Update this to your CSV path
    df = access_csv(input_file_path)
    if df is None:
        return

    detected = detect_questionnaires(df)
    if not detected:
        print("No recognized questionnaires detected in the CSV.")
        return

    # Call the main() function of each detected questionnaire module
    for prefix, main_fn in detected.items():
        print(f"\nProcessing questionnaire with prefix '{prefix}'...")
        main_fn(df)

if __name__ == "__main__":
    main()
