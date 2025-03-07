import pandas as pd

# Access CSV file for HEXACO
def HEXACO_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

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
        df[f'Q{item}'] = 6 - df[f'Q{item}']  # Assuming a 1-5 scale, reverse scoring is 6 - original response
    
    for item in reverse_emotionality:
        df[f'Q{item}'] = 6 - df[f'Q{item}']

    for item in reverse_extraversion:
        df[f'Q{item}'] = 6 - df[f'Q{item}']

    for item in reverse_agreeableness:
        df[f'Q{item}'] = 6 - df[f'Q{item}']

    for item in reverse_conscientiousness:
        df[f'Q{item}'] = 6 - df[f'Q{item}']

    for item in reverse_openness:
        df[f'Q{item}'] = 6 - df[f'Q{item}']

    # Calculate subscale scores
    df['Honesty_Humility'] = df[['Q1', 'Q4', 'Q9', 'Q16', 'Q24']].mean(axis=1)
    df['Emotionality'] = df[['Q2', 'Q10', 'Q18', 'Q22', 'Q30']].mean(axis=1)
    df['Extraversion'] = df[['Q3', 'Q12', 'Q15', 'Q27', 'Q36']].mean(axis=1)
    df['Agreeableness'] = df[['Q5', 'Q14', 'Q18', 'Q26', 'Q31']].mean(axis=1)
    df['Conscientiousness'] = df[['Q6', 'Q11', 'Q17', 'Q21', 'Q25']].mean(axis=1)
    df['Openness'] = df[['Q7', 'Q13', 'Q19', 'Q23', 'Q28']].mean(axis=1)

    return df

# Summarize results
def HEXACO_summarize_results(df):
    """
    Summarize the HEXACO subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['Honesty_Humility', 'Emotionality', 'Extraversion', 
                      'Agreeableness', 'Conscientiousness', 'Openness']].mean()
    std_scores = df[['Honesty_Humility', 'Emotionality', 'Extraversion', 
                     'Agreeableness', 'Conscientiousness', 'Openness']].std()

    print("\nSummary of HEXACO Scores:")
    print(df[['Honesty_Humility', 'Emotionality', 'Extraversion', 
              'Agreeableness', 'Conscientiousness', 'Openness']])
    
    return {
        'Mean Honesty-Humility': mean_scores['Honesty_Humility'],
        'Mean Emotionality': mean_scores['Emotionality'],
        'Mean Extraversion': mean_scores['Extraversion'],
        'Mean Agreeableness': mean_scores['Agreeableness'],
        'Mean Conscientiousness': mean_scores['Conscientiousness'],
        'Mean Openness': mean_scores['Openness'],
        'Std Dev Honesty-Humility': std_scores['Honesty_Humility'],
        'Std Dev Emotionality': std_scores['Emotionality'],
        'Std Dev Extraversion': std_scores['Extraversion'],
        'Std Dev Agreeableness': std_scores['Agreeableness'],
        'Std Dev Conscientiousness': std_scores['Conscientiousness'],
        'Std Dev Openness': std_scores['Openness']
    }

# Save the results to CSV
def HEXACO_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main():
    input_file_path = './data/HEXACO_DATA_SET.csv'
    output_file_path = 'processed_hexaco_results.csv'
    
    # Load CSV
    df = HEXACO_access_csv(input_file_path)

    if df is not None:
        # Calculate HEXACO subscale scores
        df = HEXACO_calculate_scores(df)

        # Summarize results
        summary = HEXACO_summarize_results(df)

        # Save individual scores to CSV
        HEXACO_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
