import pandas as pd

# Access CSV file for BFI
def BFI_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculate BFI subscale scores
def BFI_calculate_scores(df):
    """
    Calculate the subscale scores for the Big Five Inventory (BFI).
    Subscales include:
    - Extraversion
    - Agreeableness
    - Conscientiousness
    - Neuroticism
    - Openness
    Reverse scoring is applied where necessary.
    """
    
    # Reverse-scored items for each subscale
    reverse_extraversion = ["BFI_06", "BFI_21", "BFI_31"]  # Reverse items for Extraversion
    reverse_agreeableness = ["BFI_02", "BFI_12", "BFI_27", "BFI_37"]  # Reverse items for Agreeableness
    reverse_conscientiousness = ["BFI_08", "BFI_18", "BFI_23", "BFI_43"]  # Reverse items for Conscientiousness
    reverse_neuroticism = ["BFI_09", "BFI_24", "BFI_34"]  # Reverse items for Neuroticism
    reverse_openness = ["BFI_35", "BFI_41"]  # Reverse items for Openness

    # Apply reverse scoring for relevant items
    for item in reverse_extraversion:
        df[f'{item}r'] = 6 - df[item]  # 1-5 scale, reverse scoring is 6 - original response
    
    for item in reverse_agreeableness:
        df[f'{item}r'] = 6 - df[item]

    for item in reverse_conscientiousness:
        df[f'{item}r'] = 6 - df[item]

    for item in reverse_neuroticism:
        df[f'{item}r'] = 6 - df[item]

    for item in reverse_openness:
        df[f'{item}r'] = 6 - df[item]

    # Calculate subscale scores
    df['Extraversion'] = df[['BFI_01', 'BFI_06r', 'BFI_11', 'BFI_16', 'BFI_21r', 'BFI_26', 'BFI_31r', 'BFI_36']].mean(axis=1)
    df['Agreeableness'] = df[['BFI_02r', 'BFI_07', 'BFI_12r', 'BFI_17', 'BFI_22', 'BFI_27r', 'BFI_32', 'BFI_37r', 'BFI_42']].mean(axis=1)
    df['Conscientiousness'] = df[['BFI_03', 'BFI_08r', 'BFI_13', 'BFI_18r', 'BFI_23r', 'BFI_28', 'BFI_33', 'BFI_38', 'BFI_43r']].mean(axis=1)
    df['Neuroticism'] = df[['BFI_04', 'BFI_09r', 'BFI_14', 'BFI_19', 'BFI_24r', 'BFI_29', 'BFI_34r', 'BFI_39']].mean(axis=1)
    df['Openness'] = df[['BFI_05', 'BFI_10', 'BFI_15', 'BFI_20', 'BFI_25', 'BFI_30', 'BFI_35r', 'BFI_40', 'BFI_41r', 'BFI_44']].mean(axis=1)

    return df

# Summarize results
def BFI_summarize_results(df):
    """
    Summarize the BFI subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['Extraversion', 'Agreeableness', 'Conscientiousness', 
                      'Neuroticism', 'Openness']].mean()
    std_scores = df[['Extraversion', 'Agreeableness', 'Conscientiousness', 
                     'Neuroticism', 'Openness']].std()

    print("\nSummary of BFI Scores:")
    print(df[['Extraversion', 'Agreeableness', 'Conscientiousness', 
              'Neuroticism', 'Openness']])
    
    return {
        'Mean Extraversion': mean_scores['Extraversion'],
        'Mean Agreeableness': mean_scores['Agreeableness'],
        'Mean Conscientiousness': mean_scores['Conscientiousness'],
        'Mean Neuroticism': mean_scores['Neuroticism'],
        'Mean Openness': mean_scores['Openness'],
        'Std Dev Extraversion': std_scores['Extraversion'],
        'Std Dev Agreeableness': std_scores['Agreeableness'],
        'Std Dev Conscientiousness': std_scores['Conscientiousness'],
        'Std Dev Neuroticism': std_scores['Neuroticism'],
        'Std Dev Openness': std_scores['Openness']
    }

# Save the results to CSV
def BFI_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main():
    input_file_path = './data/BFI_DATA_SET.csv'
    output_file_path = 'processed_bfi_results.csv'
    
    # Load CSV
    df = BFI_access_csv(input_file_path)

    if df is not None:
        # Calculate BFI subscale scores
        df = BFI_calculate_scores(df)

        # Summarize results
        summary = BFI_summarize_results(df)

        # Save individual scores to CSV
        BFI_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
