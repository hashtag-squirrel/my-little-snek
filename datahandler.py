import gspread
from google.oauth2.service_account import Credentials


class Datahandler:
    """Class to handle all data transactions to and from Google Sheets"""

    # Setting up Google Sheet
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('my_little_snek')

    # Declaring constants for sheets
    PETS = SHEET.worksheet('alive')
    DECEASED = SHEET.worksheet('dead')

    def get_pet_from_file(id):
        """Accesses the pets file, checks whether the id exists
        and returns row matching the id"""
        print('Looking for pet in database...')
        first_column = Datahandler.PETS.col_values(1)
        row = Datahandler.PETS.get_all_values()
        # Iterates over id column
        for i in range(len(first_column)):
            # checks if value of cell in id column matches id given
            # and returns the whole row
            if first_column[i] == id:
                print(f'Found pet {row[i][1]}!')
                return row[i]

    def save_new_pet_to_file(pet):
        """Accesses the pets file, checks whether the id exists
        and rewrites the row with current values"""
        print('Trying to save new pet in database...')
        pet_data = [pet.id,
                    pet.name,
                    pet.type,
                    pet.age,
                    pet.hunger,
                    pet.poop,
                    pet.sadness,
                    '']
        Datahandler.PETS.append_row(pet_data)

    def save_pet_to_file(pet):
        """Accesses the pets file, checks whether the id exists
        and rewrites the row with current values"""
        print('Trying to save pet in database...')
        first_column = Datahandler.PETS.col_values(1)
        row = Datahandler.PETS.get_all_values()
        # Iterates over id column
        for i in range(len(first_column)):
            # checks if value of cell in id column matches id given
            # and returns the whole row
            if first_column[i] == pet.id:
                print(f'Saving pet {row[i][1]}!')
                data = [
                    pet.id,
                    pet.name,
                    pet.type,
                    pet.age,
                    pet.hunger,
                    pet.poop,
                    pet.sadness,
                    '']
                Datahandler.PETS.update(f'A{i+1}:H{i+1}', [data])
                break
