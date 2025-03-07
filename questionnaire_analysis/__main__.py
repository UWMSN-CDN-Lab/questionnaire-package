from questionnaire_analysis.common import access_csv, detect_questionnaires

def main():
    input_file_path = './data/your_data.csv'  # Update this to your CSV path
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
