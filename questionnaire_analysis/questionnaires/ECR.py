import pandas as pd
# Check for reverse scoring


# Calculate ECR-S subscale scores
def ECR_calculate_scores(df):
    """
    Calculate the subscale scores for the ECR-S questionnaire.
    Subscales include:
    - Anxiety
    - Avoidance
    """
    df['Anxiety'] = df[['ECR_02', 'ECR_04', 'ECR_06', 'ECR_08', 'ECR_10', 'ECR_12']].mean(axis=1)
    df['Avoidance'] = df[['ECR_01', 'ECR_03', 'ECR_05', 'ECR_07', 'ECR_09', 'ECR_11']].mean(axis=1)
    
    return df

# Summarize results
def ECR_summarize_results(df):
    """
    Summarize the ECR-S subscale scores by calculating mean and standard deviation.
    """
    mean_scores = df[['Anxiety', 'Avoidance']].mean()
    std_scores = df[['Anxiety', 'Avoidance']].std()

    print("\nSummary of ECR-S Scores:")
    print(df[['Anxiety', 'Avoidance']])
    
    return {
        'Mean Anxiety': mean_scores['Anxiety'],
        'Mean Avoidance': mean_scores['Avoidance'],
        'Std Dev Anxiety': std_scores['Anxiety'],
        'Std Dev Avoidance': std_scores['Avoidance']
    }

# Save the results to CSV
def ECR_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function
def main(df):

    output_file_path = 'processed_ecr_results.csv'
    

    if df is not None:
        # Calculate ECR-S subscale scores
        df = ECR_calculate_scores(df)

        # Summarize results
        summary = ECR_summarize_results(df)

        # Save individual scores to CSV
        ECR_save_results_to_csv(df, output_file_path)
        return df
    return None

if __name__ == "__main__":
    main()
