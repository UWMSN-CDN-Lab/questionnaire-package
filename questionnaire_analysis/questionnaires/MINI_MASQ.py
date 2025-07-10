import pandas as pd

# Define subscales (if applicable, otherwise overall scoring)
positive_affect_items = [1, 9, 15, 19, 23, 25]  # Items representing positive feelings
negative_affect_items = [2, 3, 5, 7, 11, 12, 17, 20, 21]  # Items representing negative feelings
physical_symptom_items = [4, 6, 8, 10, 14, 16, 18, 22, 24, 26]  # Items representing physical symptoms

# Calculate mean scores for a set of items
def MASQ_calculate_mean(df, items, label):
    """
    Calculate the mean score for a given list of item numbers.
    """
    item_columns = [f'MASQ_{item:02d}' for item in items]
    mean_score = df[item_columns].mean(axis=1)
    df[label] = mean_score
    return df

# Process the data to calculate subscale scores
def MASQ_process_data(df):
    """
    Calculate subscale and overall scores for the MINI-MASQ.
    Subscales:
    - Positive Affect
    - Negative Affect
    - Physical Symptom
    """
    df['MASQ_Positive_Affect_Score'] = df[['MASQ_01', 'MASQ_02', 'MASQ_03', 'MASQ_04']].mean(axis=1)
    df['MASQ_Negative_Affect_Score'] = df[['MASQ_05', 'MASQ_06', 'MASQ_07', 'MASQ_08']].mean(axis=1)
    df['MASQ_Physical_Symptom_Score'] = df[['MASQ_09', 'MASQ_10', 'MASQ_11', 'MASQ_12']].mean(axis=1)
    df['MASQ_Overall_Score'] = df[['MASQ_Positive_Affect_Score', 'MASQ_Negative_Affect_Score', 'MASQ_Physical_Symptom_Score']].mean(axis=1)
    return df

# Summarize results
def MASQ_summarize_results(df):
    """
    Summarize the MINI-MASQ subscale and overall scores by calculating mean and standard deviation.
    """
    mean_scores = df[['MASQ_Positive_Affect_Score', 'MASQ_Negative_Affect_Score', 'MASQ_Physical_Symptom_Score', 'MASQ_Overall_Score']].mean()
    std_scores = df[['MASQ_Positive_Affect_Score', 'MASQ_Negative_Affect_Score', 'MASQ_Physical_Symptom_Score', 'MASQ_Overall_Score']].std()

    print("\nSummary of MINI-MASQ Scores:")
    print(df[['MASQ_Positive_Affect_Score', 'MASQ_Negative_Affect_Score', 'MASQ_Physical_Symptom_Score', 'MASQ_Overall_Score']])

    return {
        'Mean Positive Affect Score': mean_scores['MASQ_Positive_Affect_Score'],
        'Mean Negative Affect Score': mean_scores['MASQ_Negative_Affect_Score'],
        'Mean Physical Symptom Score': mean_scores['MASQ_Physical_Symptom_Score'],
        'Mean Overall Score': mean_scores['MASQ_Overall_Score'],
        'Std Dev Positive Affect': std_scores['MASQ_Positive_Affect_Score'],
        'Std Dev Negative Affect': std_scores['MASQ_Negative_Affect_Score'],
        'Std Dev Physical Symptom': std_scores['MASQ_Physical_Symptom_Score'],
        'Std Dev Overall': std_scores['MASQ_Overall_Score']
    }

# Save the results to CSV
def MASQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_emotion_survey_results.csv'


    if df is not None:
        # Process the data to calculate subscale and overall scores
        df = MASQ_process_data(df)

        # Summarize results
        summary = MASQ_summarize_results(df)

        # Save results to CSV
        MASQ_save_results_to_csv(df, output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'MASQ_Positive_Affect_Score',
            'MASQ_Negative_Affect_Score',
            'MASQ_Physical_Symptom_Score',
            'MASQ_Overall_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
