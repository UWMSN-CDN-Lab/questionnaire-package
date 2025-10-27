# Questionnaire Analysis Package

A comprehensive Python package for automated scoring and analysis of psychological questionnaires from CSV data files.

## Overview

This package provides a modular system for processing psychological questionnaire data with automatic questionnaire detection, scoring, and summary generation. It currently supports **27 standardized questionnaires** and includes a powerful module generator for adding new questionnaires.

## Key Features

- 🔍 **Automatic Questionnaire Detection** - Scans CSV columns and identifies questionnaires by prefix
- 📊 **Standardized Scoring** - Handles reverse scoring, subscales, and total scores automatically  
- 🚀 **Module Generator** - Create new questionnaire modules from JSON configuration files
- 📈 **Batch Processing** - Process multiple questionnaires in a single CSV file
- 🛠️ **CLI & Programmatic APIs** - Use from command line or import into Python scripts
- ⚡ **Performance Optimized** - Efficient DataFrame operations to avoid fragmentation

## Supported Questionnaires

The package currently supports these psychological instruments:

**Emotion & Affect:**
- PANAS (Positive and Negative Affect Schedule)
- EERQ (Extended Emotion Regulation Questionnaire) 
- PMERQ (Process Model of Emotion Regulation Questionnaire)
- BEQ (Berkeley Expressivity Questionnaire)

**Risk & Decision Making:**
- DOSPERT (Domain-Specific Risk-Taking Scale)
- UPPS (Impulsive Behavior Scale)
- CARE (Cognitive Reappraisal of Risky Events)

**Personality & Individual Differences:**
- BFI (Big Five Inventory)
- HEXACO (Personality Inventory)
- SD4 (Short Dark Tetrad)
- BSSS (Brief Sensation Seeking Scale)

**Social & Relationships:**
- UCLA (Loneliness Scale)
- ECR (Experiences in Close Relationships)
- MSPSS (Multidimensional Scale of Perceived Social Support)
- RAS (Relationship Assessment Scale)
- IPPA (Inventory of Parent and Peer Attachment)

**Mental Health & Well-being:**
- CESDR (Center for Epidemiologic Studies Depression Scale)
- MINI_MASQ (Mini Mood and Anxiety Symptom Questionnaire)
- PSS (Perceived Stress Scale)
- SWLS (Satisfaction with Life Scale)
- LOTR (Life Orientation Test Revised)

**And more:** ALQ, IRQ, GCF, SU, CBCL, SIAS

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd questionnaire-package

# Install dependencies
pip install pandas
```

### Basic Usage

#### Command Line Interface

```bash
# Process a CSV file with questionnaire data
python -m questionnaire_analysis your_data.csv

# This will create your_data_summary.csv with computed scores
```

#### Python Script Usage

```python
from questionnaire_analysis.common import analyze_questionnaire_csv

# Analyze questionnaire data
summary_df = analyze_questionnaire_csv("your_data.csv")
print(summary_df.head())
```

## How It Works

### 1. Data Input Format

Your CSV file should contain questionnaire responses with standardized column naming:

```csv
SubjectIDPANAS_01,PANAS_02,DOSPERT_01,DOSPERT_02,UCLA_01,UCLA_02,...
S001,4,2,3,5,2,4,...
S002,5,1,4,3,3,2,...
```

### 2. Automatic Detection

The system scans your CSV columns and automatically detects questionnaires:

```python
# Detects questionnaires by column prefixes
"PANAS_" → PANAS questionnaire detected
"DOSPERT_" → DOSPERT questionnaire detected  
"UCLA_" → UCLA questionnaire detected
```

### 3. Processing Pipeline

For each detected questionnaire:

1. **Data Validation** - Converts columns to numeric, handles missing data
2. **Reverse Scoring** - Applies reverse scoring to specified items
3. **Subscale Calculation** - Computes subscale scores (mean or sum)
4. **Total Scores** - Calculates overall questionnaire scores
5. **Summary Generation** - Creates summary statistics

### 4. Output

The system generates a summary CSV with computed scores:

```csv
ResponseId,PANAS_Positive_Affect,PANAS_Negative_Affect,DOSPERT_Overall_Score,UCLA_Total_Score,...
R001,3.8,2.1,3.2,2.4,...
R002,4.2,1.8,3.7,2.8,...
```

## Adding New Questionnaires

### Using the Module Generator

The package includes a powerful module generator that creates new questionnaire modules from JSON configuration files.

#### 1. Create Configuration File

```json
{
  "questionnaire_name": "NEWQ",
  "full_name": "New Example Questionnaire", 
  "prefix": "NEWQ_",
  "items": {
    "total_items": 12,
    "item_range": [1, 12]
  },
  "reverse_scoring": {
    "enabled": true,
    "items": [3, 7, 11],
    "scale_max": 5
  },
  "subscales": [
    {
      "name": "Positive_Emotions",
      "items": [1, 2, 4, 6, 9],
      "scoring_method": "mean"
    },
    {
      "name": "Negative_Emotions", 
      "items": [3, 5, 7, 8, 11],
      "scoring_method": "mean"
    }
  ],
  "total_score": {
    "enabled": true,
    "method": "mean_of_subscales"
  }
}
```

#### 2. Generate Module

```bash
# Generate questionnaire module from JSON config
python generate_questionnaire.py my_questionnaire.json

# Interactive configuration creation
python generate_questionnaire.py --interactive

# Create example configuration template
python generate_questionnaire.py --example
```

#### 3. Automatic Integration

The generator automatically:
- ✅ Creates new questionnaire module (`questionnaires/NEWQ.py`)
- ✅ Updates package imports (`questionnaires/__init__.py`)
- ✅ Adds to detection system (`common.py`)
- ✅ Makes questionnaire immediately available for use

## Advanced Features

### Direct Module Usage

```python
# Import specific questionnaire module
from questionnaire_analysis.questionnaires import PANAS, DOSPERT

# Process data with specific questionnaire
panas_scores = PANAS.main(your_dataframe)
dospert_scores = DOSPERT.main(your_dataframe)
```

### Batch Processing

```python
# Process multiple CSV files
import glob
from questionnaire_analysis.common import analyze_questionnaire_csv

csv_files = glob.glob("data/*.csv")
for csv_file in csv_files:
    summary = analyze_questionnaire_csv(csv_file)
    print(f"Processed {csv_file}: {summary.shape[0]} participants")
```

### Custom Analysis

```python
# Load and analyze data step by step
from questionnaire_analysis.common import access_csv, detect_questionnaires

# Load data
df = access_csv("your_data.csv")

# Detect available questionnaires
detected = detect_questionnaires(df)
print(f"Found questionnaires: {list(detected.keys())}")

# Process specific questionnaires
for prefix, main_fn in detected.items():
    scores = main_fn(df)
    print(f"{prefix} scores computed: {scores.columns.tolist()}")
```

## File Structure

```
questionnaire-package/
├── questionnaire_analysis/          # Main package
│   ├── __init__.py                 # Package initialization
│   ├── __main__.py                 # CLI entry point
│   ├── common.py                   # Core functionality
│   ├── module_generator.py         # Questionnaire generator
│   └── questionnaires/             # Individual questionnaire modules
│       ├── __init__.py
│       ├── PANAS.py               # PANAS questionnaire
│       ├── DOSPERT.py             # DOSPERT questionnaire
│       ├── UCLA.py                # UCLA questionnaire
│       └── ...                    # 27 questionnaire modules
├── generate_questionnaire.py       # Module generator CLI
├── sample_data.csv                 # Example data file
└── README.md                       # This file
```

## Data Requirements

### CSV Format
- **Required**: ResponseId or similar identifier column
- **Questionnaire columns**: Follow naming convention `QUESTIONNAIRE_##` (e.g., `PANAS_01`, `DOSPERT_15`)
- **Scale**: Most questionnaires use 1-5 or 1-7 Likert scales
- **Missing data**: Handled automatically with `pd.to_numeric(errors='coerce')`

### Naming Conventions
- **Prefix**: Each questionnaire has a unique prefix (e.g., `PANAS_`, `UCLA_`)
- **Item numbering**: Zero-padded numbers (e.g., `01`, `02`, `15`)
- **Consistency**: All items for a questionnaire must use the same prefix

## Performance Notes

- **Efficient processing**: Uses `df.assign()` and batch operations to avoid DataFrame fragmentation
- **Memory optimized**: Processes questionnaires individually to manage memory usage
- **Scalable**: Tested with datasets containing thousands of participants
- **Fast detection**: Column prefix matching is optimized for large datasets

## Contributing

### Adding New Questionnaires

1. **Use the generator** (recommended):
   ```bash
   python generate_questionnaire.py --interactive
   ```

2. **Manual creation**: Follow the existing module patterns in `questionnaires/`

3. **Testing**: Ensure your module works with sample data before integration

### Code Standards

- Follow existing naming conventions (`QUESTIONNAIRE_function_name`)
- Use efficient DataFrame operations (`df.assign()` over individual assignments)
- Include proper docstrings and error handling
- Test with realistic data before committing

## Troubleshooting

### Common Issues

**"No questionnaires detected"**
- Check column naming matches expected prefixes
- Verify CSV file loads correctly
- Ensure questionnaire columns contain numeric data

**"Module not found"**
- Check that questionnaire module exists in `questionnaires/` directory
- Verify imports are updated in `__init__.py` and `common.py`
- Try regenerating the module with the generator

**Performance issues**
- For large datasets, consider processing questionnaires individually
- Check for DataFrame fragmentation warnings
- Ensure sufficient memory for your dataset size

### Getting Help

1. Check existing questionnaire modules for examples
2. Use the interactive generator for new questionnaires
3. Verify your data format matches expected conventions
4. Test with small sample datasets first

## License

#TODO

## Citation

#TODO

---

*This package streamlines psychological questionnaire analysis by providing automated scoring, standardized processing, and easy extensibility for new instruments.*
