import pandas as pd



# Calculate total and subscale scores
def IRQ_calculate_scores(df):
    """
    Calculate the subscale and total scores for the Interpersonal Regulation Questionnaire (IRQ).
    Subscales: 
    - Negative-Tendency (IRQ-NT)
    - Negative-Efficacy (IRQ-NE)
    - Positive-Tendency (IRQ-PT)
    - Positive-Efficacy (IRQ-PE)
    """
    df['IRQ_NT_Score'] = df[['IRQ_01', 'IRQ_02', 'IRQ_03', 'IRQ_04']].sum(axis=1)
    df['IRQ_NE_Score'] = df[['IRQ_05', 'IRQ_06', 'IRQ_07', 'IRQ_08']].sum(axis=1)
    df['IRQ_PT_Score'] = df[['IRQ_09', 'IRQ_10', 'IRQ_11', 'IRQ_12']].sum(axis=1)
    df['IRQ_PE_Score'] = df[['IRQ_13', 'IRQ_14', 'IRQ_15', 'IRQ_16']].sum(axis=1)
    
    # Total score is the sum of all subscales
    df['IRQ_Total_Score'] = df[['IRQ_NT_Score', 'IRQ_NE_Score', 'IRQ_PT_Score', 'IRQ_PE_Score']].sum(axis=1)
    
    return df

# Summarize results
def IRQ_summarize_results(df):
    """
    Summarize the IRQ subscale and total scores by calculating the mean and standard deviation for each.
    """
    mean_scores = df[['IRQ_NT_Score', 'IRQ_NE_Score', 'IRQ_PT_Score', 'IRQ_PE_Score', 'IRQ_Total_Score']].mean()
    std_scores = df[['IRQ_NT_Score', 'IRQ_NE_Score', 'IRQ_PT_Score', 'IRQ_PE_Score', 'IRQ_Total_Score']].std()

    print("\nSummary of IRQ Scores:")
    print(df[['IRQ_NT_Score', 'IRQ_NE_Score', 'IRQ_PT_Score', 'IRQ_PE_Score', 'IRQ_Total_Score']])

    print(f"\nMean IRQ Negative-Tendency: {mean_scores['IRQ_NT_Score']:.2f}")
    print(f"Mean IRQ Negative-Efficacy: {mean_scores['IRQ_NE_Score']:.2f}")
    print(f"Mean IRQ Positive-Tendency: {mean_scores['IRQ_PT_Score']:.2f}")
    print(f"Mean IRQ Positive-Efficacy: {mean_scores['IRQ_PE_Score']:.2f}")
    print(f"Mean IRQ Total Score: {mean_scores['IRQ_Total_Score']:.2f}")
    
    return {
        'Mean IRQ Negative-Tendency': mean_scores['IRQ_NT_Score'],
        'Mean IRQ Negative-Efficacy': mean_scores['IRQ_NE_Score'],
        'Mean IRQ Positive-Tendency': mean_scores['IRQ_PT_Score'],
        'Mean IRQ Positive-Efficacy': mean_scores['IRQ_PE_Score'],
        'Mean IRQ Total Score': mean_scores['IRQ_Total_Score'],
        'Std Dev IRQ Negative-Tendency': std_scores['IRQ_NT_Score'],
        'Std Dev IRQ Negative-Efficacy': std_scores['IRQ_NE_Score'],
        'Std Dev IRQ Positive-Tendency': std_scores['IRQ_PT_Score'],
        'Std Dev IRQ Positive-Efficacy': std_scores['IRQ_PE_Score'],
        'Std Dev IRQ Total Score': std_scores['IRQ_Total_Score']
    }

# Save the results to CSV
def IRQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main():
    output_file_path = 'processed_irq_results.csv'
    summary_output_file_path = 'irq_summary_results.csv'


    if df is not None:
        # Calculate IRQ subscale and total scores
        df = IRQ_calculate_scores(df)

        # Summarize results
        summary = IRQ_summarize_results(df)

        # Save individual scores to CSV
        IRQ_save_results_to_csv(df, output_file_path)
        return df
    return None

if __name__ == "__main__":
    main()
