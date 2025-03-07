import pandas as pd

# Access CSV file
def BSSS_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculate total sensation seeking score
def BSSS_calculate_bsss_score(df):
    """
    Calculate the total score for the Brief Sensation Seeking Scale (BSSS).
    """
    # Items contributing to the BSSS score
    bsss_items = ["BSSS_01", "BSSS_02", "BSSS_03", "BSSS_04", "BSSS_05", "BSSS_08", "BSSS_07", "BSSS_08"]
    
    # Calculate total BSSS score by summing the responses to all items
    df['Total_BSSS_Score'] = df[[item for item in bsss_items]].sum(axis=1)
    
    return df

# Summarize results
def BSSS_summarize_results(df):
    """
    Summarize the BSSS scores by calculating the mean and standard deviation.
    """
    mean_bsss_score = df['Total_BSSS_Score'].mean()
    std_bsss_score = df['Total_BSSS_Score'].std()
    
    print("\nSummary of BSSS Scores:")
    print(df[['Total_BSSS_Score']])
    
    print(f"\nMean BSSS Score: {mean_bsss_score:.3f}")
    print(f"Standard Deviation of BSSS Scores: {std_bsss_score:.3f}")
    
    return {
        'Mean BSSS Score': mean_bsss_score,
        'Standard Deviation': std_bsss_score
    }

# Save the results to CSV
def BSSS_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main():
    input_file_path = './data/BSSS_DATA_SET.csv'
    output_file_path = 'processed_bsss_results.csv'
    
    # Load the CSV file
    df = BSSS_access_csv(input_file_path)

    if df is not None:
        # Calculate BSSS scores
        df = BSSS_calculate_bsss_score(df)

        # Summarize results
        summary = BSSS_summarize_results(df)

        # Save results to CSV
        BSSS_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
# script to abbr _ package
