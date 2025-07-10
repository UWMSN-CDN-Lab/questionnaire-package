import pandas as pd


# Calculate IPPA scores
def IPPA_calculate_scores(df):
    """
    Calculate the subscale scores for the IPPA IPPA_uestionnaire.
    Subscales include:
    - Trust
    - Communication
    - Alienation
    There are separate scores for Parents (Mother, Father) and Peers.
    Reverse scoring is applied where needed.
    """
    # Reverse-scored items for parent and peer sections
    reverse_parent = ['IPPA_03', 'IPPA_10', 'IPPA_14', 'IPPA_23']
    reverse_peer = ['IPPA_04', 'IPPA_09', 'IPPA_11', 'IPPA_18', 'IPPA_22']

    # Reverse scoring for parent items
    for item in reverse_parent:
        df[item] = 6 - df[item]  # Assuming 1-5 Likert scale

    # Reverse scoring for peer items
    for item in reverse_peer:
        df[item] = 6 - df[item]

    # Parent Attachment Scores (Trust, Communication, Alienation)
    df['Parent_Trust'] = df[['IPPA_01', 'IPPA_02', 'IPPA_04', 'IPPA_13', 'IPPA_21']].mean(axis=1)
    df['Parent_Communication'] = df[['IPPA_05', 'IPPA_07', 'IPPA_15', 'IPPA_17']].mean(axis=1)
    df['Parent_Alienation'] = df[['IPPA_09', 'IPPA_18']].mean(axis=1)

    # Peer Attachment Scores (Trust, Communication, Alienation)
    df['Peer_Trust'] = df[['IPPA_06', 'IPPA_08', 'IPPA_12', 'IPPA_13']].mean(axis=1)
    df['Peer_Communication'] = df[['IPPA_01', 'IPPA_02', 'IPPA_07']].mean(axis=1)
    df['Peer_Alienation'] = df[['IPPA_09', 'IPPA_11', 'IPPA_18']].mean(axis=1)

    return df

# Summarize results
def IPPA_summarize_results(df):
    """
    Summarize the IPPA scores by calculating mean and standard deviation for each subscale.
    """
    mean_scores = df[['Parent_Trust', 'Parent_Communication', 'Parent_Alienation',
                      'Peer_Trust', 'Peer_Communication', 'Peer_Alienation']].mean()
    std_scores = df[['Parent_Trust', 'Parent_Communication', 'Parent_Alienation',
                     'Peer_Trust', 'Peer_Communication', 'Peer_Alienation']].std()

    print("\nSummary of IPPA Scores:")
    print(df[['Parent_Trust', 'Parent_Communication', 'Parent_Alienation',
              'Peer_Trust', 'Peer_Communication', 'Peer_Alienation']])

    return {
        'Mean Parent Trust': mean_scores['Parent_Trust'],
        'Mean Parent Communication': mean_scores['Parent_Communication'],
        'Mean Parent Alienation': mean_scores['Parent_Alienation'],
        'Mean Peer Trust': mean_scores['Peer_Trust'],
        'Mean Peer Communication': mean_scores['Peer_Communication'],
        'Mean Peer Alienation': mean_scores['Peer_Alienation'],
        'Std Dev Parent Trust': std_scores['Parent_Trust'],
        'Std Dev Parent Communication': std_scores['Parent_Communication'],
        'Std Dev Parent Alienation': std_scores['Parent_Alienation'],
        'Std Dev Peer Trust': std_scores['Peer_Trust'],
        'Std Dev Peer Communication': std_scores['Peer_Communication'],
        'Std Dev Peer Alienation': std_scores['Peer_Alienation']
    }

# Save the results to CSV
def IPPA_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):

    output_file_path = 'processed_ippa_results.csv'

    
    if df is not None:
        # Calculate IPPA subscale scores
        df = IPPA_calculate_scores(df)

        # Summarize results
        summary = IPPA_summarize_results(df)

        # Only return the summary columns for concatenation
        summary_columns = [
            'IPPA_Trust_Score',
            'IPPA_Communication_Score',
            'IPPA_Alienation_Score',
            'IPPA_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None
if __name__ == "__main__":
    main()
