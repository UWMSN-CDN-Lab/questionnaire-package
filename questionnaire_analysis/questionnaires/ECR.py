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
    df['ECR_Anxiety'] = df[['ECR_02', 'ECR_04', 'ECR_06', 'ECR_08', 'ECR_10', 'ECR_12']].mean(axis=1)
    df['ECR_Avoidance'] = df[['ECR_01', 'ECR_03', 'ECR_05', 'ECR_07', 'ECR_09', 'ECR_11']].mean(axis=1)
    
    return df

# Summarize results
def ECR_summarize_results(df):
    """
    Summarize the ECR-S subscale scores by calculating mean and standard deviation.
    """
    mean_scores = df[['ECR_Anxiety', 'ECR_Avoidance']].mean()
    std_scores = df[['ECR_Anxiety', 'ECR_Avoidance']].std()

    print("\nSummary of ECR-S Scores:")
    print(df[['ECR_Anxiety', 'ECR_Avoidance']])
    
    return {
        'Mean Anxiety': mean_scores['ECR_Anxiety'],
        'Mean Avoidance': mean_scores['ECR_Avoidance'],
        'Std Dev Anxiety': std_scores['ECR_Anxiety'],
        'Std Dev Avoidance': std_scores['ECR_Avoidance']
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
        # ECR_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'ECR_Anxiety',
            'ECR_Avoidance'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
