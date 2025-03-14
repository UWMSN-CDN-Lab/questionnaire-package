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
    item_columns = [f'Item_{item}' for item in items]
    mean_score = df[item_columns].mean(axis=1)
    df[label] = mean_score
    return df

# Process the data to calculate subscale scores
def MASQ_process_data(df):
    """
    Process the data by calculating subscale and overall scores.
    """
    # Calculate mean scores for subscales
    df = MASQ_calculate_mean(df, positive_affect_items, 'Positive_Affect_Score')
    df = MASQ_calculate_mean(df, negative_affect_items, 'Negative_Affect_Score')
    df = MASQ_calculate_mean(df, physical_symptom_items, 'Physical_Symptom_Score')
    
    # Calculate overall mean score across all items
    all_items = positive_affect_items + negative_affect_items + physical_symptom_items
    df = MASQ_calculate_mean(df, all_items, 'Overall_Score')
    
    return df

# Summarize the results
def MASQ_summarize_results(df):
    """
    Summarize the subscale scores and the overall score.
    """
    print("\nSummary of Scores:")
    print(df[['Positive_Affect_Score', 'Negative_Affect_Score', 'Physical_Symptom_Score', 'Overall_Score']])
    
    summary = {
        'Mean Positive Affect Score': df['Positive_Affect_Score'].mean(),
        'Mean Negative Affect Score': df['Negative_Affect_Score'].mean(),
        'Mean Physical Symptom Score': df['Physical_Symptom_Score'].mean(),
        'Mean Overall Score': df['Overall_Score'].mean()
    }
    
    for key, value in summary.items():
        print(f"{key}: {value:.2f}")
    
    return summary

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

if __name__ == "__main__":
    main()
