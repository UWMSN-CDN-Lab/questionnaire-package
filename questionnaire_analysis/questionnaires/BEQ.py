import pandas as pd

# Access CSV file
def BEQ_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Reverse scoring for specific items
def BEQ_reverse_score(df):
    """
    Reverse score specific BEQ items (3, 8, 9).
    """
    # TODO
    df['BEQ_03r'] = 8 - df['BEQ_03']
    df['BEQ_08r'] = 8 - df['BEQ_08']
    df['BEQ_09r'] = 8 - df['BEQ_09']
    return df

# Calculate the BEQ scores
def BEQ_calculate_scores(df):
    """
    Calculate the subscale and total scores for the Berkeley Expressivity Questionnaire (BEQ).
    Three subscales: Negative Expressivity (nex), Positive Expressivity (pex), and Impulse Strength (str).
    """
    # Reverse scoring
    df = BEQ_reverse_score(df)
    # TODO
    # Calculate the BEQ subscale scores
    df['BEQ_Negative_Expressivity'] = df[['BEQ_09r', 'BEQ_13', 'BEQ_16', 'BEQ_03r', 'BEQ_05', 'BEQ_08r']].mean(axis=1)
    df['BEQ_Positive_Expressivity'] = df[['BEQ_06', 'BEQ_01', 'BEQ_04', 'BEQ_10']].mean(axis=1)
    df['BEQ_Impulse_Strength'] = df[['BEQ_15', 'BEQ_11', 'BEQ_14', 'BEQ_07', 'BEQ_02', 'BEQ_12']].mean(axis=1)

    # Calculate the overall BEQ score as the mean of all subscales
    df['Total_BEQ_Score'] = df[['BEQ_Negative_Expressivity', 'BEQ_Positive_Expressivity', 'BEQ_Impulse_Strength']].mean(axis=1)
    
    return df

# Summarize results
def BEQ_summarize_results(df):
    """
    Summarize the BEQ scores by calculating the mean and standard deviation for each subscale and the total score.
    """
    mean_scores = df[['BEQ_Negative_Expressivity', 'BEQ_Positive_Expressivity', 'BEQ_Impulse_Strength', 'Total_BEQ_Score']].mean()
    std_scores = df[['BEQ_Negative_Expressivity', 'BEQ_Positive_Expressivity', 'BEQ_Impulse_Strength', 'Total_BEQ_Score']].std()

    print("\nSummary of BEQ Scores:")
    print(df[['Total_BEQ_Score', 'BEQ_Negative_Expressivity', 'BEQ_Positive_Expressivity', 'BEQ_Impulse_Strength']])

    print(f"\nMean Total BEQ Score: {mean_scores['Total_BEQ_Score']:.2f}")
    print(f"Standard Deviation of Total BEQ Scores: {std_scores['Total_BEQ_Score']:.2f}")

    return {
        'Mean Total BEQ Score': mean_scores['Total_BEQ_Score'],
        'Std Dev Total BEQ Score': std_scores['Total_BEQ_Score'],
        'Mean Negative Expressivity': mean_scores['BEQ_Negative_Expressivity'],
        'Mean Positive Expressivity': mean_scores['BEQ_Positive_Expressivity'],
        'Mean Impulse Strength': mean_scores['BEQ_Impulse_Strength'],
        'Std Dev Negative Expressivity': std_scores['BEQ_Negative_Expressivity'],
        'Std Dev Positive Expressivity': std_scores['BEQ_Positive_Expressivity'],
        'Std Dev Impulse Strength': std_scores['BEQ_Impulse_Strength'],
    }

# Save the results to CSV
def BEQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main():
    input_file_path = './data/BEQ_DATA_SET.csv'
    output_file_path = 'processed_beq_results.csv'
    
    # Load the CSV file
    df = BEQ_access_csv(input_file_path)

    if df is not None:
        # Calculate BEQ scores
        df = BEQ_calculate_scores(df)

        # Summarize results
        summary = BEQ_summarize_results(df)

        # Save results to CSV
        BEQ_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
