import pandas as pd

# Access CSV file
def panas_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculate positive and negative affect scores
def panas_calculate_affect_scores(df):
    """
    Calculate the Positive and Negative Affect scores based on the PANAS-SF items.
    """
    # Items contributing to Positive Affect
    positive_affect_items = [
        "PANAS_01", "PANAS_03", "PANAS_05", "PANAS_09", "PANAS_10",
        "PANAS_12", "PANAS_14", "PANAS_16", "PANAS_17", "PANAS_19"
    ]
    
    # Items contributing to Negative Affect
    negative_affect_items = [
        "PANAS_02", "PANAS_04", "PANAS_06", "PANAS_07", "PANAS_08",
        "PANAS_11", "PANAS_13", "PANAS_15", "PANAS_18", "PANAS_20"
    ]
    
    # Calculate Positive Affect score
    df['Positive_Affect_Score'] = df[[item for item in positive_affect_items]].sum(axis=1)
    
    # Calculate Negative Affect score
    df['Negative_Affect_Score'] = df[[item for item in negative_affect_items]].sum(axis=1)
    
    return df

# Summarize results and compare to normative data
def panas_summarize_results(df):
    """
    Summarize the Positive and Negative Affect Scores
    """
    # Calculate means for the dataset
    positive_affect_mean = df['Positive_Affect_Score'].mean()
    negative_affect_mean = df['Negative_Affect_Score'].mean()
    
    return positive_affect_mean, negative_affect_mean

# Save the results to CSV
# try and catch here 
def panas_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main():
    input_file_path = './data/PANAS_SF_DATA_SET.csv'
    output_file_path = 'processed_panas_sf_results.csv'
    
    # Load the CSV file
    df = panas_access_csv(input_file_path)

    if df is not None:
        # Calculate Positive and Negative Affect Scores
        df = panas_calculate_affect_scores(df)

        # Summarize results
        summary = panas_summarize_results(df)

        # Save results to CSV
        panas_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
# pschy273
# unique method names, prefix - abbr of the paper for all functions
