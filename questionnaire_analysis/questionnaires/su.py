import pandas as pd

# SU NOT SETUP FOR OUR SU QUESTIONS!

# Access CSV file for Substance Use
def SU_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

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
        df[f'Q{item}'] = 6 - df[f'Q{item}']  # Assuming a 1-5 scale, reverse scoring is 6 - original response

    # Calculate subscale scores
    df['Frequency_Use'] = df[['Q1', 'Q2', 'Q3']].mean(axis=1)
    df['Substance_Type_Use'] = df[['Q4', 'Q5', 'Q6']].mean(axis=1)
    df['Consequences_Use'] = df[['Q7', 'Q8', 'Q9', 'Q10']].mean(axis=1)

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
def main():
    input_file_path = './data/SU_DATA_SET.csv'
    output_file_path = 'processed_su_results.csv'
    
    # Load CSV
    df = SU_access_csv(input_file_path)

    if df is not None:
        # Calculate Substance Use subscale scores
        df = SU_calculate_scores(df)

        # Summarize results
        summary = SU_summarize_results(df)

        # Save individual scores to CSV
        SU_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
