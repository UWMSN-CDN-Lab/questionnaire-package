import pandas as pd

# Access CSV file for DTC-GT
def DTCGT_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculate subscale scores for DTC-GT case studies
def DTCGT_calculate_scores(df):
    """
    Calculate the scores for DTC-GT case studies.
    Subscales may include:
    - Privacy concerns
    - Risks
    - Ethical considerations
    """
    df['Privacy_Concerns'] = df[['PR_1', 'PR_2', 'PR_3']].mean(axis=1)
    df['Ethical_Concerns'] = df[['EC_1', 'EC_2', 'EC_3']].mean(axis=1)
    
    df['Total_Score'] = df[['Privacy_Concerns', 'Ethical_Concerns']].sum(axis=1)
    
    return df

# Summarize results
def DTCGT_summarize_results(df):
    """
    Summarize the DTC-GT scores by calculating mean and standard deviation.
    """
    mean_scores = df[['Privacy_Concerns', 'Ethical_Concerns']].mean()
    std_scores = df[['Privacy_Concerns', 'Ethical_Concerns']].std()

    print("\nSummary of DTC-GT Scores:")
    print(df[['Privacy_Concerns', 'Ethical_Concerns']])
    
    return {
        'Mean Privacy Concerns': mean_scores['Privacy_Concerns'],
        'Mean Ethical Concerns': mean_scores['Ethical_Concerns'],
        'Std Dev Privacy Concerns': std_scores['Privacy_Concerns'],
        'Std Dev Ethical Concerns': std_scores['Ethical_Concerns']
    }

# Save the results to CSV
def DTCGT_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function
def main():
    input_file_path = './data/DTCGT_DATA_SET.csv'
    output_file_path = 'processed_dtcgt_results.csv'
    
    # Load CSV
    df = DTCGT_access_csv(input_file_path)

    if df is not None:
        # Calculate DTC-GT subscale scores
        df = DTCGT_calculate_scores(df)

        # Summarize results
        summary = DTCGT_summarize_results(df)

        # Save individual scores to CSV
        DTCGT_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
