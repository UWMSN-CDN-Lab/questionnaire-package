How to run it as a CLI, in your terminal. Run it from root, i.e, outside the directory questionnaire_analysis.

# How to Run:

python3 -m questionnaire_analysis file_path_to_csv

How to run it in a python script: 

from questionnaire_analysis.common import analyze_questionnaire_csv
summary_df = analyze_questionnaire_csv("file_path_to_csv")



