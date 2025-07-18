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

    # Calculate all attachment scores at once to avoid fragmentation
    ippa_scores = {
        'IPPA_Parent_Trust': df[['IPPA_01', 'IPPA_02', 'IPPA_04', 'IPPA_13', 'IPPA_21']].mean(axis=1),
        'IPPA_Parent_Communication': df[['IPPA_05', 'IPPA_07', 'IPPA_15', 'IPPA_17']].mean(axis=1),
        'IPPA_Parent_Alienation': df[['IPPA_09', 'IPPA_18']].mean(axis=1),
        'IPPA_Peer_Trust': df[['IPPA_06', 'IPPA_08', 'IPPA_12', 'IPPA_13']].mean(axis=1),
        'IPPA_Peer_Communication': df[['IPPA_01', 'IPPA_02', 'IPPA_07']].mean(axis=1),
        'IPPA_Peer_Alienation': df[['IPPA_09', 'IPPA_11', 'IPPA_18']].mean(axis=1)
    }
    df = df.assign(**ippa_scores)

    return df

# Summarize results
def IPPA_summarize_results(df):
    """
    Summarize the IPPA scores by calculating mean and standard deviation for each subscale.
    """
    mean_scores = df[['IPPA_Parent_Trust', 'IPPA_Parent_Communication', 'IPPA_Parent_Alienation',
                      'IPPA_Peer_Trust', 'IPPA_Peer_Communication', 'IPPA_Peer_Alienation']].mean()
    std_scores = df[['IPPA_Parent_Trust', 'IPPA_Parent_Communication', 'IPPA_Parent_Alienation',
                     'IPPA_Peer_Trust', 'IPPA_Peer_Communication', 'IPPA_Peer_Alienation']].std()

    print("\nSummary of IPPA Scores:")
    print(df[['IPPA_Parent_Trust', 'IPPA_Parent_Communication', 'IPPA_Parent_Alienation',
              'IPPA_Peer_Trust', 'IPPA_Peer_Communication', 'IPPA_Peer_Alienation']])

    return {
        'Mean Parent Trust': mean_scores['IPPA_Parent_Trust'],
        'Mean Parent Communication': mean_scores['IPPA_Parent_Communication'],
        'Mean Parent Alienation': mean_scores['IPPA_Parent_Alienation'],
        'Mean Peer Trust': mean_scores['IPPA_Peer_Trust'],
        'Mean Peer Communication': mean_scores['IPPA_Peer_Communication'],
        'Mean Peer Alienation': mean_scores['IPPA_Peer_Alienation'],
        'Std Dev Parent Trust': std_scores['IPPA_Parent_Trust'],
        'Std Dev Parent Communication': std_scores['IPPA_Parent_Communication'],
        'Std Dev Parent Alienation': std_scores['IPPA_Parent_Alienation'],
        'Std Dev Peer Trust': std_scores['IPPA_Peer_Trust'],
        'Std Dev Peer Communication': std_scores['IPPA_Peer_Communication'],
        'Std Dev Peer Alienation': std_scores['IPPA_Peer_Alienation']
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
            'IPPA_Parent_Trust',
            'IPPA_Parent_Communication',
            'IPPA_Parent_Alienation',
            'IPPA_Peer_Trust',
            'IPPA_Peer_Communication',
            'IPPA_Peer_Alienation'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None
if __name__ == "__main__":
    main()
