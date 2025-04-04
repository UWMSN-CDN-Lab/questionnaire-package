import pandas as pd

# SU NOT SETUP FOR OUR SU QUESTIONS!

# Calculate Substance Use scores
def SU_calculate_scores(df):
    """
    Calculate the scores for the Substance Use questionnaire.
    Subscales could include:
    - Frequency of Use
    - Substance Type (e.g., alcohol, tobacco, drugs)
    - Consequences of Use
    Reverse scoring is applied where necessary.
    """
    
    # Example: Reverse scoring (modify as needed)
    reverse_substance_use_items = [5, 10]  # Example reverse items for substance use
    
    # Apply reverse scoring for relevant items
    for item in reverse_substance_use_items:
        column_name = f'SU_{item:02d}'  # Ensure consistent formatting if needed (e.g., SU_05)
        # Convert the column to numeric first
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        # Apply reverse scoring: assuming a 1-5 scale, reverse is computed as 6 - value
        df[column_name] = 6 - df[column_name]  # Assuming a 1-5 scale, reverse scoring is 6 - original response

    # Calculate subscale scores
    numeric_columns = ['SU_01', 'SU_02', 'SU_03', 'SU_04', 'SU_05', 'SU_06',
                   'SU_07', 'SU_08', 'SU_09', 'SU_10']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['Frequency_Use'] = df[['SU_01', 'SU_02', 'SU_03']].mean(axis=1)
    df['Substance_Type_Use'] = df[['SU_04', 'SU_05', 'SU_06']].mean(axis=1)
    df['Consequences_Use'] = df[['SU_07', 'SU_08', 'SU_09', 'SU_10']].mean(axis=1)

    return df

# Summarize results
def SU_summarize_results(df):
    """
    Summarize the Substance Use subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['Frequency_Use', 'Substance_Type_Use', 'Consequences_Use']].mean()
    std_scores = df[['Frequency_Use', 'Substance_Type_Use', 'Consequences_Use']].std()

    print("\nSummary of Substance Use Scores:")
    print(df[['Frequency_Use', 'Substance_Type_Use', 'Consequences_Use']])
    
    return {
        'Mean Frequency of Use': mean_scores['Frequency_Use'],
        'Mean Substance Type Use': mean_scores['Substance_Type_Use'],
        'Mean Consequences of Use': mean_scores['Consequences_Use'],
        'Std Dev Frequency of Use': std_scores['Frequency_Use'],
        'Std Dev Substance Type Use': std_scores['Substance_Type_Use'],
        'Std Dev Consequences of Use': std_scores['Consequences_Use']
    }

# Save the results to CSV
def SU_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    if df is not None:
        # Step 1: Score calculations
        df = SU_calculate_scores(df)

        # Step 2: Optional summary logging
        _ = SU_summarize_results(df)
        return df
    return None

if __name__ == "__main__":
    main()
