import pandas as pd

# --- Step 1: Load Data and Initial Inspection ---
file_path = 'fabric_defect_synthetic.csv'
df = pd.read_csv(file_path)

print("Initial Data Info:")
print(df.info())
print("\n---")


# --- Step 2: Handle Missing Values ---
# Fill the 440 missing values in 'Defect_Type' with 'None'
df['Defect_Type'].fillna('None', inplace=True)


# --- Step 3: Standardize Data Types and Format ---
# Convert 'Inspection_Date' from object (string) to datetime
df['Inspection_Date'] = pd.to_datetime(df['Inspection_Date'])


# --- Step 4: Handle Duplicates and Categorical Consistency ---
# Check for duplicates (0 were found)
df.drop_duplicates(inplace=True)

# The 'Brand' and 'Severity' columns were inspected and found to be consistent
# (e.g., no 'zara' vs 'ZARA' issues).


# --- Step 5: Save the Cleaned Data ---
cleaned_file_path = 'fabric_defect_synthetic_cleaned.csv'
df.to_csv(cleaned_file_path, index=False)

print("\nCleaning complete!")
print(f"Final data saved to: '{cleaned_file_path}'")
print("\nFinal Data Info:")
print(df.info())