import pandas as pd

# Access CSV file for IPPA
def IPPA_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculate IPPA scores
def IPPA_calculate_scores(df):
    """
    Calculate the subscale scores for the IPPA questionnaire.
    Subscales include:
    - Trust
    - Communication
    - Alienation
    There are separate scores for Parents (Mother, Father) and Peers.
    Reverse scoring is applied where needed.
    """
    # Reverse-scored items for parent and peer sections
    reverse_parent = ['Q3', 'Q10', 'Q14', 'Q23']
    reverse_peer = ['Q4', 'Q9', 'Q11', 'Q18', 'Q22']

    # Reverse scoring for parent items
    for item in reverse_parent:
        df[item] = 6 - df[item]  # Assuming 1-5 Likert scale

    # Reverse scoring for peer items
    for item in reverse_peer:
        df[item] = 6 - df[item]

    # Parent Attachment Scores (Trust, Communication, Alienation)
    df['Parent_Trust'] = df[['Q1', 'Q2', 'Q4', 'Q13', 'Q21']].mean(axis=1)
    df['Parent_Communication'] = df[['Q5', 'Q7', 'Q15', 'Q17']].mean(axis=1)
    df['Parent_Alienation'] = df[['Q9', 'Q18']].mean(axis=1)

    # Peer Attachment Scores (Trust, Communication, Alienation)
    df['Peer_Trust'] = df[['Q6', 'Q8', 'Q12', 'Q13']].mean(axis=1)
    df['Peer_Communication'] = df[['Q1', 'Q2', 'Q7']].mean(axis=1)
    df['Peer_Alienation'] = df[['Q9', 'Q11', 'Q18']].mean(axis=1)

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
def main():
    input_file_path = './data/IPPA_DATA_SET.csv'
    output_file_path = 'processed_ippa_results.csv'
    
    # Load CSV
    df = IPPA_access_csv(input_file_path)
    
    if df is not None:
        # Calculate IPPA subscale scores
        df = IPPA_calculate_scores(df)

        # Summarize results
        summary = IPPA_summarize_results(df)

        # Save individual scores to CSV
        IPPA_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
