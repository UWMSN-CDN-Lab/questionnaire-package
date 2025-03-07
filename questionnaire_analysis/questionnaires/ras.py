# TODO
import pandas as pd

# Access CSV file for MSPSS
def MSPSS_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculating MSPSS scores
def MSPSS_calculate_scores(df):
    """
    Calculate the subscale scores for MSPSS.
    Subscales include:
    - Family
    - Friends
    - Significant Others
    """
    df['Family_Score'] = df[['Q3', 'Q4', 'Q8', 'Q11']].mean(axis=1)
    df['Friends_Score'] = df[['Q6', 'Q7', 'Q9', 'Q12']].mean(axis=1)
    df['Significant_Others_Score'] = df[['Q1', 'Q2', 'Q5', 'Q10']].mean(axis=1)
    
    # Total MSPSS score
    df['MSPSS_Total_Score'] = df[['Family_Score', 'Friends_Score', 'Significant_Others_Score']].mean(axis=1)
    
    return df

# Summarize results
def MSPSS_summarize_results(df):
    mean_scores = df[['Family_Score', 'Friends_Score', 'Significant_Others_Score', 'MSPSS_Total_Score']].mean()
    std_scores = df[['Family_Score', 'Friends_Score', 'Significant_Others_Score', 'MSPSS_Total_Score']].std()

    print("\nSummary of MSPSS Scores:")
    print(df[['Family_Score', 'Friends_Score', 'Significant_Others_Score', 'MSPSS_Total_Score']])
    
    return {
        'Mean Family Score': mean_scores['Family_Score'],
        'Mean Friends Score': mean_scores['Friends_Score'],
        'Mean Significant Others Score': mean_scores['Significant_Others_Score'],
        'Mean Total MSPSS Score': mean_scores['MSPSS_Total_Score'],
        'Std Dev Family Score': std_scores['Family_Score'],
        'Std Dev Friends Score': std_scores['Friends_Score'],
        'Std Dev Significant Others Score': std_scores['Significant_Others_Score'],
        'Std Dev Total MSPSS Score': std_scores['MSPSS_Total_Score']
    }

# Save the results to CSV
def MSPSS_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function
def main():
    input_file_path = './data/MSPSS_DATA_SET.csv'
    output_file_path = 'processed_mspss_results.csv'
    
    # Load CSV
    df = MSPSS_access_csv(input_file_path)
    
    if df is not None:
        # Calculate MSPSS scores
        df = MSPSS_calculate_scores(df)

        # Summarize results
        summary = MSPSS_summarize_results(df)

        # Save individual scores to CSV
        MSPSS_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
