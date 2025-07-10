#!/usr/bin/env python3
"""
Test script to verify that questionnaire analysis works correctly
"""

import pandas as pd
import sys
import os

# Add the package to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from questionnaire_analysis.common import analyze_questionnaire_csv

def create_test_data():
    """Create a simple test dataset with EERQ and DOSPERT columns"""
    data = {
        'ResponseId': [f'R{i:03d}' for i in range(1, 11)],
        'EERQ_01': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'EERQ_02': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'EERQ_03': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'EERQ_04': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'EERQ_05': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'EERQ_06': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'EERQ_07': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'EERQ_08': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'EERQ_09': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'EERQ_10': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'EERQ_11': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'EERQ_12': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'EERQ_13': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'EERQ_14': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'EERQ_15': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'EERQ_16': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'EERQ_17': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'EERQ_18': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'EERQ_19': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'EERQ_20': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'EERQ_21': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'EERQ_22': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_01': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_02': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_03': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_04': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_05': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_06': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_07': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_08': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_09': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_10': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_11': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_12': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_13': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_14': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_15': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_16': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_17': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_18': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_19': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_20': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_21': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_22': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_23': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_24': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_25': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_26': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
        'DOSPERT_27': [2, 5, 3, 4, 2, 5, 3, 4, 2, 5],
        'DOSPERT_28': [5, 2, 4, 3, 5, 2, 4, 3, 5, 2],
        'DOSPERT_29': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4],
        'DOSPERT_30': [4, 3, 5, 2, 4, 3, 5, 2, 4, 3],
    }
    return pd.DataFrame(data)

def test_questionnaire_analysis():
    """Test the questionnaire analysis with sample data"""
    print("Creating test data...")
    test_df = create_test_data()
    
    # Save test data
    test_csv_path = "test_questionnaire_data.csv"
    test_df.to_csv(test_csv_path, index=False)
    print(f"Test data saved to {test_csv_path}")
    
    print("\nRunning questionnaire analysis...")
    result = analyze_questionnaire_csv(test_csv_path, output_summary=True)
    
    if result is not None:
        print("\n✅ Analysis completed successfully!")
        print(f"Result shape: {result.shape}")
        print(f"Result columns: {list(result.columns)}")
        
        # Check if EERQ columns are present
        eerq_columns = [col for col in result.columns if 'EERQ' in col]
        if eerq_columns:
            print(f"✅ EERQ columns found: {eerq_columns}")
        else:
            print("❌ No EERQ columns found in result")
            
        # Check if DOSPERT columns are present
        dospert_columns = [col for col in result.columns if 'DOSPERT' in col]
        if dospert_columns:
            print(f"✅ DOSPERT columns found: {dospert_columns}")
        else:
            print("❌ No DOSPERT columns found in result")
            
        print(f"\nFirst few rows of result:")
        print(result.head())
        
    else:
        print("❌ Analysis failed!")
    
    # Clean up
    if os.path.exists(test_csv_path):
        os.remove(test_csv_path)
    if os.path.exists(test_csv_path.replace('.csv', '_summary.csv')):
        os.remove(test_csv_path.replace('.csv', '_summary.csv'))

if __name__ == "__main__":
    test_questionnaire_analysis() 