import pandas as pd



# Calculate positive and negative affect scores
def PANAS_calculate_affect_scores(df):
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
def PANAS_summarize_results(df):
    """
    Summarize the Positive and Negative Affect Scores
    """
    # Calculate means for the dataset
    positive_affect_mean = df['Positive_Affect_Score'].mean()
    negative_affect_mean = df['Negative_Affect_Score'].mean()
    
    return positive_affect_mean, negative_affect_mean

# Save the results to CSV
# try and catch here 
def PANAS_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_panas_sf_results.csv'


    if df is not None:
        # Calculate Positive and Negative Affect Scores
        df = PANAS_calculate_affect_scores(df)

        # Summarize results
        summary = PANAS_summarize_results(df)

        # Save results to CSV
        PANAS_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
# pschy273
# unique method names, prefix - abbr of the paper for all functions
