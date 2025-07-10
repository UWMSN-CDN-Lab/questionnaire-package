import pandas as pd
# TODO
# Change column names



# Calculate CBCL subscale scores
def CBCL_calculate_scores(df):
    """
    Calculate the subscale scores for the CBCL.
    Subscales include:
    - Anxiety/Depression
    - Withdrawn/Depressed
    - Somatic Complaints
    - Social Problems
    - Thought Problems
    - Attention Problems
    - Aggressive Behavior
    """
    # Example subscale calculation (adjust the item numbers based on your CBCL_uestionnaire):
    df['CBCL_Anxiety_Depression'] = df[['CBCL_01', 'CBCL_02', 'CBCL_03', 'CBCL_04']].sum(axis=1)
    df['CBCL_Withdrawn_Depressed'] = df[['CBCL_05', 'CBCL_06', 'CBCL_07']].sum(axis=1)
    df['CBCL_Somatic_Complaints'] = df[['CBCL_08', 'CBCL_09', 'CBCL_10']].sum(axis=1)
    df['CBCL_Social_Problems'] = df[['CBCL_11', 'CBCL_12', 'CBCL_13']].sum(axis=1)
    df['CBCL_Thought_Problems'] = df[['CBCL_14', 'CBCL_15', 'CBCL_16']].sum(axis=1)
    df['CBCL_Attention_Problems'] = df[['CBCL_17', 'CBCL_18', 'CBCL_19']].sum(axis=1)
    df['CBCL_Aggressive_Behavior'] = df[['CBCL_20', 'CBCL_21', 'CBCL_22']].sum(axis=1)
    
    return df

# Summarize results
def CBCL_summarize_results(df):
    """
    Summarize the CBCL subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['CBCL_Anxiety_Depression', 'CBCL_Withdrawn_Depressed', 'CBCL_Somatic_Complaints', 
                      'CBCL_Social_Problems', 'CBCL_Thought_Problems', 'CBCL_Attention_Problems', 
                      'CBCL_Aggressive_Behavior']].mean()
    std_scores = df[['CBCL_Anxiety_Depression', 'CBCL_Withdrawn_Depressed', 'CBCL_Somatic_Complaints', 
                     'CBCL_Social_Problems', 'CBCL_Thought_Problems', 'CBCL_Attention_Problems', 
                     'CBCL_Aggressive_Behavior']].std()

    print("\nSummary of CBCL Scores:")
    print(df[['CBCL_Anxiety_Depression', 'CBCL_Withdrawn_Depressed', 'CBCL_Somatic_Complaints', 
              'CBCL_Social_Problems', 'CBCL_Thought_Problems', 'CBCL_Attention_Problems', 
              'CBCL_Aggressive_Behavior']])
    
    return {
        'Mean Anxiety/Depression': mean_scores['CBCL_Anxiety_Depression'],
        'Mean Withdrawn/Depressed': mean_scores['CBCL_Withdrawn_Depressed'],
        'Mean Somatic Complaints': mean_scores['CBCL_Somatic_Complaints'],
        'Mean Social Problems': mean_scores['CBCL_Social_Problems'],
        'Mean Thought Problems': mean_scores['CBCL_Thought_Problems'],
        'Mean Attention Problems': mean_scores['CBCL_Attention_Problems'],
        'Mean Aggressive Behavior': mean_scores['CBCL_Aggressive_Behavior'],
        'Std Dev Anxiety/Depression': std_scores['CBCL_Anxiety_Depression'],
        'Std Dev Withdrawn/Depressed': std_scores['CBCL_Withdrawn_Depressed'],
        'Std Dev Somatic Complaints': std_scores['CBCL_Somatic_Complaints'],
        'Std Dev Social Problems': std_scores['CBCL_Social_Problems'],
        'Std Dev Thought Problems': std_scores['CBCL_Thought_Problems'],
        'Std Dev Attention Problems': std_scores['CBCL_Attention_Problems'],
        'Std Dev Aggressive Behavior': std_scores['CBCL_Aggressive_Behavior']
    }

# Save the results to CSV
def CBCL_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_cbcl_results.csv'
    


    if df is not None:
        # Calculate CBCL subscale scores
        df = CBCL_calculate_scores(df)

        # Summarize results
        summary = CBCL_summarize_results(df)

        # Save individual scores to CSV
        CBCL_save_results_to_csv(df, output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'CBCL_Anxiety_Depression',
            'CBCL_Withdrawn_Depressed',
            'CBCL_Somatic_Complaints',
            'CBCL_Social_Problems',
            'CBCL_Thought_Problems',
            'CBCL_Attention_Problems',
            'CBCL_Aggressive_Behavior'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None
if __name__ == "__main__":
    main()
