import pandas as pd
from .common import access_csv, detect_questionnaires
import argparse
import sys

def main():
    summary_dfs = []
    parser = argparse.ArgumentParser(description="Process a questionnaire CSV file.")
    parser.add_argument("csv_path", type=str, help="Path to the questionnaire CSV file")

    args = parser.parse_args()

    df = access_csv(args.csv_path)
    # input_file_path = '/Users/ayusmankhuntia/Desktop/Package/questionnaire-package/questionnaire_analysis/Risk-Taking+and+Emotion+Regulation_February+4,+2025_15.23.csv'  # Update this to your CSV path
    # df = access_csv(input_file_path)
    if df is None:
        return

    detected = detect_questionnaires(df)
    if not detected:
        print("No recognized questionnaires detected in the CSV.")
        return

    # Call the main() function of each detected questionnaire module
    for prefix, main_fn in detected.items():
        print(f"\nProcessing questionnaire with prefix '{prefix}'...")
        summary_df = main_fn(df)

    summary_output_path = args.csv_path.replace(".csv", "_summary.csv")
    summary_df.to_csv(summary_output_path, index=False)
    print(f"\n Summary saved to: {summary_output_path}")
    return summary_df

if __name__ == "__main__":
    main()
