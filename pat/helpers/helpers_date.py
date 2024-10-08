#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from datetime import datetime


def get_current_date() -> str:
    # Get the current date
    current_date = datetime.now()

    # Format the date as dd-mm-yyyy
    formatted_date = current_date.strftime("%d-%m-%Y")
    return formatted_date
