import pandas as pd



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
        df[f'{item}'] = 6 - df[item]  # 1-5 scale, reverse scoring is 6 - original response
    
    for item in reverse_agreeableness:
        df[f'{item}'] = 6 - df[item]

    for item in reverse_conscientiousness:
        df[f'{item}'] = 6 - df[item]

    for item in reverse_neuroticism:
        df[f'{item}'] = 6 - df[item]

    for item in reverse_openness:
        df[f'{item}'] = 6 - df[item]

    # Calculate subscale scores all at once to avoid fragmentation
    subscale_scores = {
        'BFI_Extraversion': df[['BFI_01', 'BFI_06', 'BFI_11', 'BFI_16', 'BFI_21', 'BFI_26', 'BFI_31', 'BFI_36']].mean(axis=1),
        'BFI_Agreeableness': df[['BFI_02', 'BFI_07', 'BFI_12', 'BFI_17', 'BFI_22', 'BFI_27', 'BFI_32', 'BFI_37', 'BFI_42']].mean(axis=1),
        'BFI_Conscientiousness': df[['BFI_03', 'BFI_08', 'BFI_13', 'BFI_18', 'BFI_23', 'BFI_28', 'BFI_33', 'BFI_38', 'BFI_43']].mean(axis=1),
        'BFI_Neuroticism': df[['BFI_04', 'BFI_09', 'BFI_14', 'BFI_19', 'BFI_24', 'BFI_29', 'BFI_34', 'BFI_39']].mean(axis=1),
        'BFI_Openness': df[['BFI_05', 'BFI_10', 'BFI_15', 'BFI_20', 'BFI_25', 'BFI_30', 'BFI_35', 'BFI_40', 'BFI_41', 'BFI_44']].mean(axis=1)
    }
    df = df.assign(**subscale_scores)

    return df

# Summarize results
def BFI_summarize_results(df):
    """
    Summarize the BFI subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['BFI_Extraversion', 'BFI_Agreeableness', 'BFI_Conscientiousness', 
                      'BFI_Neuroticism', 'BFI_Openness']].mean()
    std_scores = df[['BFI_Extraversion', 'BFI_Agreeableness', 'BFI_Conscientiousness', 
                     'BFI_Neuroticism', 'BFI_Openness']].std()

    print("\nSummary of BFI Scores:")
    print(df[['BFI_Extraversion', 'BFI_Agreeableness', 'BFI_Conscientiousness', 
              'BFI_Neuroticism', 'BFI_Openness']])
    
    return {
        'Mean Extraversion': mean_scores['BFI_Extraversion'],
        'Mean Agreeableness': mean_scores['BFI_Agreeableness'],
        'Mean Conscientiousness': mean_scores['BFI_Conscientiousness'],
        'Mean Neuroticism': mean_scores['BFI_Neuroticism'],
        'Mean Openness': mean_scores['BFI_Openness'],
        'Std Dev Extraversion': std_scores['BFI_Extraversion'],
        'Std Dev Agreeableness': std_scores['BFI_Agreeableness'],
        'Std Dev Conscientiousness': std_scores['BFI_Conscientiousness'],
        'Std Dev Neuroticism': std_scores['BFI_Neuroticism'],
        'Std Dev Openness': std_scores['BFI_Openness']
    }

# Save the results to CSV
def BFI_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):

    output_file_path = 'processed_bfi_results.csv'

    if df is not None:
        # Calculate BFI subscale scores
        df = BFI_calculate_scores(df)

        # Summarize results
        summary = BFI_summarize_results(df)

        # Save individual scores to CSV
        # BFI_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'BFI_Extraversion',
            'BFI_Agreeableness', 
            'BFI_Conscientiousness',
            'BFI_Neuroticism',
            'BFI_Openness'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
