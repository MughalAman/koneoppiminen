import pandas as pd
from pathlib import Path


def correct_csv():
    # Get the current script directory
    script_dir = Path(__file__).parent

    csv_path = script_dir / 'Terveys_v3.csv'

    # Load the original CSV file with 'ISO-8859-1' encoding
    df = pd.read_csv(csv_path, encoding='ISO-8859-1', sep=';')

    # Convert 'Tupakointi', 'Koettu onnellisuus', 'Paino' columns to integers
    df[['Tupakointi', 'Koettu onnellisuus', 'Paino']] = df[['Tupakointi', 'Koettu onnellisuus', 'Paino']].apply(pd.to_numeric, errors='coerce')

    # Fill missing or non-finite values with zeros for these columns
    df[['Tupakointi', 'Koettu onnellisuus', 'Paino']] = df[['Tupakointi', 'Koettu onnellisuus', 'Paino']].fillna(0)

    # Convert 'Tupakointi', 'Koettu onnellisuus', 'Paino' columns to integers after filling missing values
    df[['Tupakointi', 'Koettu onnellisuus', 'Paino']] = df[['Tupakointi', 'Koettu onnellisuus', 'Paino']].astype(int)

    # Replace 'Mies' with 'M' and 'Nainen' with 'N' in the 'Sukupuoli' column
    df['Sukupuoli'] = df['Sukupuoli'].replace({'Mies': 'M', 'Nainen': 'N'})

    # Ensure 'Sukupuoli' is of type string
    df['Sukupuoli'] = df['Sukupuoli'].astype(str)

    # Convert 'Kuukausitulo' and 'Syntymävuosi' columns to integers without rounding
    df['Kuukausitulo'] = pd.to_numeric(df['Kuukausitulo'], errors='coerce').fillna(0).astype(int)
    df['Syntymävuosi'] = pd.to_numeric(df['Syntymävuosi'], errors='coerce').fillna(0).astype(int)
    df['Kolesteroli'] = pd.to_numeric(df['Kolesteroli'], errors='coerce').fillna(0).round(1)

    # Fill any other missing values with an empty string
    df = df.fillna('')

    # Save the corrected dataframe to a new CSV file
    df.to_csv(f"{script_dir}/Terveys_v3_corrected.csv", index=False, encoding='ISO-8859-1', mode='w')


if __name__ == '__main__':
    correct_csv()
    print('CSV file corrected and saved to Terveys_v3_corrected.csv')
