import pandas as pd


# Calculate HEXACO subscale scores
def HEXACO_calculate_scores(df):
    """
    Calculate the subscale scores for the HEXACO Personality Inventory.
    Subscales include:
    - Honesty-Humility
    - Emotionality
    - Extraversion
    - Agreeableness
    - Conscientiousness
    - Openness to Experience
    Reverse scoring is applied where necessary.
    """
    
    # Reverse-scored items for each subscale
    reverse_honesty_humility = [4, 16, 24]  # Example reverse items for Honesty-Humility
    reverse_emotionality = [10, 22]  # Example reverse items for Emotionality
    reverse_extraversion = [12, 27]  # Example reverse items for Extraversion
    reverse_agreeableness = [18, 31]  # Example reverse items for Agreeableness
    reverse_conscientiousness = [5, 14]  # Example reverse items for Conscientiousness
    reverse_openness = [7, 19]  # Example reverse items for Openness

    # Apply reverse scoring for relevant items
    for item in reverse_honesty_humility:
        df[f'HEXACO_{item:02d}'] = 6 - df[f'HEXACO_{item:02d}']  # Assuming a 1-5 scale, reverse scoring is 6 - original response
    
    for item in reverse_emotionality:
        df[f'HEXACO_{item:02d}'] = 6 - df[f'HEXACO_{item:02d}']

    for item in reverse_extraversion:
        df[f'HEXACO_{item:02d}'] = 6 - df[f'HEXACO_{item:02d}']

    for item in reverse_agreeableness:
        df[f'HEXACO_{item:02d}'] = 6 - df[f'HEXACO_{item:02d}']

    for item in reverse_conscientiousness:
        df[f'HEXACO_{item:02d}'] = 6 - df[f'HEXACO_{item:02d}']

    for item in reverse_openness:
        df[f'HEXACO_{item:02d}'] = 6 - df[f'HEXACO_{item:02d}']

    # Calculate subscale scores
    df['HEXACO_Honesty_Humility'] = df[['HEXACO_01', 'HEXACO_04', 'HEXACO_09', 'HEXACO_16', 'HEXACO_24']].mean(axis=1)
    df['HEXACO_Emotionality'] = df[['HEXACO_02', 'HEXACO_10', 'HEXACO_18', 'HEXACO_22', 'HEXACO_30']].mean(axis=1)
    df['HEXACO_Extraversion'] = df[['HEXACO_03', 'HEXACO_12', 'HEXACO_15', 'HEXACO_27', 'HEXACO_36']].mean(axis=1)
    df['HEXACO_Agreeableness'] = df[['HEXACO_05', 'HEXACO_14', 'HEXACO_18', 'HEXACO_26', 'HEXACO_31']].mean(axis=1)
    df['HEXACO_Conscientiousness'] = df[['HEXACO_06', 'HEXACO_11', 'HEXACO_17', 'HEXACO_21', 'HEXACO_25']].mean(axis=1)
    df['HEXACO_Openness'] = df[['HEXACO_07', 'HEXACO_13', 'HEXACO_19', 'HEXACO_23', 'HEXACO_28']].mean(axis=1)

    return df

# Summarize results
def HEXACO_summarize_results(df):
    """
    Summarize the HEXACO subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['HEXACO_Honesty_Humility', 'HEXACO_Emotionality', 'HEXACO_Extraversion', 
                      'HEXACO_Agreeableness', 'HEXACO_Conscientiousness', 'HEXACO_Openness']].mean()
    std_scores = df[['HEXACO_Honesty_Humility', 'HEXACO_Emotionality', 'HEXACO_Extraversion', 
                     'HEXACO_Agreeableness', 'HEXACO_Conscientiousness', 'HEXACO_Openness']].std()

    print("\nSummary of HEXACO Scores:")
    print(df[['HEXACO_Honesty_Humility', 'HEXACO_Emotionality', 'HEXACO_Extraversion', 
              'HEXACO_Agreeableness', 'HEXACO_Conscientiousness', 'HEXACO_Openness']])
    
    return {
        'Mean Honesty-Humility': mean_scores['HEXACO_Honesty_Humility'],
        'Mean Emotionality': mean_scores['HEXACO_Emotionality'],
        'Mean Extraversion': mean_scores['HEXACO_Extraversion'],
        'Mean Agreeableness': mean_scores['HEXACO_Agreeableness'],
        'Mean Conscientiousness': mean_scores['HEXACO_Conscientiousness'],
        'Mean Openness': mean_scores['HEXACO_Openness'],
        'Std Dev Honesty-Humility': std_scores['HEXACO_Honesty_Humility'],
        'Std Dev Emotionality': std_scores['HEXACO_Emotionality'],
        'Std Dev Extraversion': std_scores['HEXACO_Extraversion'],
        'Std Dev Agreeableness': std_scores['HEXACO_Agreeableness'],
        'Std Dev Conscientiousness': std_scores['HEXACO_Conscientiousness'],
        'Std Dev Openness': std_scores['HEXACO_Openness']
    }

# Save the results to CSV
def HEXACO_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_hexaco_results.csv'

    if df is not None:
        # Calculate HEXACO subscale scores
        df = HEXACO_calculate_scores(df)

        # Summarize results
        summary = HEXACO_summarize_results(df)

        # Save individual scores to CSV
        HEXACO_save_results_to_csv(df, output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'HEXACO_Honesty_Humility',
            'HEXACO_Emotionality',
            'HEXACO_Extraversion',
            'HEXACO_Agreeableness',
            'HEXACO_Conscientiousness',
            'HEXACO_Openness'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
