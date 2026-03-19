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
    
    # Reverse-scored items for each subscale (using string column names)
    reverse_honesty_humility = ['HEXACO_04', 'HEXACO_16', 'HEXACO_24']
    reverse_emotionality = ['HEXACO_10', 'HEXACO_22']
    reverse_extraversion = ['HEXACO_12', 'HEXACO_27']
    reverse_agreeableness = ['HEXACO_18', 'HEXACO_31']
    reverse_conscientiousness = ['HEXACO_05', 'HEXACO_14']
    reverse_openness = ['HEXACO_07', 'HEXACO_19']

    # All HEXACO columns for numeric conversion
    all_hexaco_items = [f'HEXACO_{i:02d}' for i in range(1, 37)]

    # Convert all columns to numeric FIRST
    for col in all_hexaco_items:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Apply reverse scoring for relevant items
    all_reverse_items = (reverse_honesty_humility + reverse_emotionality +
                         reverse_extraversion + reverse_agreeableness +
                         reverse_conscientiousness + reverse_openness)
    for item in all_reverse_items:
        if item in df.columns:
            df[item] = 6 - df[item]  # Assuming a 1-5 scale, reverse scoring is 6 - original response

    # Calculate all subscale scores at once to avoid fragmentation
    hexaco_scores = {
        'HEXACO_Honesty_Humility': df[['HEXACO_01', 'HEXACO_04', 'HEXACO_09', 'HEXACO_16', 'HEXACO_24']].mean(axis=1),
        'HEXACO_Emotionality': df[['HEXACO_02', 'HEXACO_10', 'HEXACO_18', 'HEXACO_22', 'HEXACO_30']].mean(axis=1),
        'HEXACO_Extraversion': df[['HEXACO_03', 'HEXACO_12', 'HEXACO_15', 'HEXACO_27', 'HEXACO_36']].mean(axis=1),
        'HEXACO_Agreeableness': df[['HEXACO_05', 'HEXACO_14', 'HEXACO_18', 'HEXACO_26', 'HEXACO_31']].mean(axis=1),
        'HEXACO_Conscientiousness': df[['HEXACO_06', 'HEXACO_11', 'HEXACO_17', 'HEXACO_21', 'HEXACO_25']].mean(axis=1),
        'HEXACO_Openness': df[['HEXACO_07', 'HEXACO_13', 'HEXACO_19', 'HEXACO_23', 'HEXACO_28']].mean(axis=1)
    }
    df = df.assign(**hexaco_scores)

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
        # HEXACO_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
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
