import requests

# Function for vacancy data download
def download_vacancy_data(url_latest, url_first_previous, number_of_previous_files, save_path = "data/raw"):
    """
    Download the latest and previous ONS vacancy data files and save them locally.

    Parameters:
    url_latest (str): URL of the latest file.
    url_first_previous (str): URL of the first previous file (URLs for other files will be derived from this).
    number_of_previous_files (int): Number of previous files to download.
    save_path (str): Directory where the files will be saved. Default is "data/raw".
    """
    # Download the latest file and save in the specified folder
    r = requests.get(url_latest, verify=False)  # Download the file
    with open(f"{save_path}/ons_vacancies_0.csv", "wb") as f:  # Save the file
        f.write(r.content)

    # Download the previous files and save in the specified folder
    for i in range(number_of_previous_files):  # Loop to download previous files
        version_number = url_first_previous.split("v")[-1].split("/")[0]
        new_version = int(version_number) - i
        r = requests.get(url_first_previous.replace(f"v{version_number}", f"v{new_version}"), verify = False)
        with open(f"{save_path}/ons_vacancies_{i + 1}.csv", "wb") as f:
            f.write(r.content)