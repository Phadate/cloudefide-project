import pandas as pd

OPERATOR = ('+', '-', '*')

# define function to check for valid column name
def is_column_name_valid(column_name:str) -> bool:
    if not column_name:
        # return false if empty string
        return False
    for letter in column_name:
        if not (letter.isalpha() or letter == '_'):
            return False
    return True


def find_operator(role: str):
    """"
    function to find the operator
    """
    for letter in role:
        if letter in OPERATOR:
            return letter
    return None


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    for col in df.columns:
        if not is_column_name_valid(col):
            return pd.DataFrame([])

    # check if the new_column name is valid and fit our set rule
    if not is_column_name_valid(new_column):
        return pd.DataFrame([])

    # find the operator in the role
    role = role.strip()  # first remove whitespaces
    operation = find_operator(role)

    # return empty dataframe if we have no operation
    if operation is None:
        return pd.DataFrame([])

    # use the operator to split the columns
    role_parts = role.split(operation)

    # check if we don't have the two columns
    if len(role_parts) != 2:
        return pd.DataFrame([])

    first_column = role_parts[0].strip()
    second_column = role_parts[-1].strip()

    # validate the columns in the roles
    if not is_column_name_valid(first_column) or not is_column_name_valid(second_column):
        return pd.DataFrame([])

    # check if the columns in role matches the existing colum in the dataframe
    if first_column not in df.columns or second_column not in df.columns:
        return pd.DataFrame([])

    # Make a copy of the dataframe
    final_result_df = df.copy()

    # perform the operation
    if operation == '+':
        final_result_df[new_column] = df[first_column] + df[second_column]
    elif operation == '-':
        final_result_df[new_column] = df[first_column] - df[second_column]
    elif operation == '*':
        final_result_df[new_column] = df[first_column] * df[second_column]

    return final_result_df


