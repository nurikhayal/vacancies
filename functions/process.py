import pandas as pd
import numpy as np

def load_and_process_vacancy_data(number_of_previous_files):
    """
    Loads and processes multiple CSV files containing ONS vacancy data.

    Each file is expected to follow a specific format where:
    - The 'Release date' row contains the vintage information.
    - Monthly data starts from the row where 'Title' equals '2001 MAY'.
    - The first column is the date, the second is the number of vacancies, and the third will be used for the vintage.

    The function performs the following steps for each file:
    1. Reads the CSV file.
    2. Extracts the vintage row and monthly data.
    3. Resets the index.
    4. Adds a 'vintage' column based on the release date.
    5. Drops the vintage row.
    6. Renames columns to 'date', 'vacancies', and 'vintage'.
    7. Appends the processed data to a master DataFrame.

    Parameters:
    ----------
    number_of_previous_files : int
        The number of previous files to process. The function will process files
        from index 0 to `number_of_previous_files` inclusive.

    Returns:
    -------
    pd.DataFrame
        A concatenated DataFrame containing processed vacancy data from all files.
    """
    df = pd.DataFrame()

    for i in range(number_of_previous_files + 1):
        file_name = f"data/raw/ons_vacancies_{i}.csv"
        df_temp = pd.read_csv(file_name)

        # Keep only the vintage row and monthly data
        df_temp = pd.concat([
            df_temp[df_temp['Title'] == 'Release date'],
            df_temp.iloc[df_temp[df_temp['Title'] == '2001 MAY'].index[0]:]
        ])
        df_temp.reset_index(drop=True, inplace=True)

        # Add vintage column
        df_temp['vintage'] = df_temp.iloc[0, 1]

        # Drop the vintage row
        df_temp = df_temp.drop(index=0)

        # Rename columns
        df_temp = df_temp.rename(columns={
            df_temp.columns[0]: 'date',
            df_temp.columns[1]: 'vacancies',
            df_temp.columns[2]: 'vintage'
        })

        # Append to main dataframe
        df = pd.concat([df, df_temp], ignore_index=True)

    return df
