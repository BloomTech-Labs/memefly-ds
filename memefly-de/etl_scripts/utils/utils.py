import json
import os
import pprint
import pandas as pd
from pathlib import Path


def read_json(base_dir: str, file_name: str):
    """
    Reads json file, and loads it into memory
    """
    if not Path(base_dir).is_dir():
        raise ValueError(f'Parameter {base_dir} is not a directory.')
    full_path = Path(base_dir, file_name)
    with open(full_path) as robj:
        data = json.load(robj)
    return data


def write_df_to_json(df: pd.DataFrame, base_dir: str, file_name: str, indent=False, orient='records', keep_index=False, verbose=False):
    """
    Writes pandas dataframe to json

    Parameters
    ==========

    df: Pandas DataFrame object - data loaded in memory
    base_dir: str - data/base directory/folder name
    file_name: str - JSON file name to save it as
    indent: bool - True makes indent 4 space when saving JSON file, otherwise defaults to regular JSON with no indents
    orient: str - Default is 'records', otherwise refer to pandas.to_json api
    keep_index: bool - Only applicable when orient is set to 'records'
    verbose: bool - Prints out messsage to confirm where the file is saved and lists directory contents for visual verfication.

    Returns
    =======
    NoneType
    """
    if not Path(base_dir).is_dir():
        raise ValueError(f'Parameter {base_dir} is not a directory.')
    full_path = Path(base_dir, file_name)
    if orient == 'records':
        if indent:
            with open(full_path, 'w') as wobj:
                json.dump(json.loads(df.to_json(orient=orient)),
                          wobj, indent=4)
        df.to_json(full_path, orient=orient)
    else:
        df.to_json(full_path, orient=orient, index=keep_index)
        if indent:
            with open(full_path, 'w') as wobj:
                json.dump(json.loads(df.to_json(orient=orient, index=keep_index)),
                          wobj, indent=4)

    if verbose:
        print(
            f"Wrote data of type {type(df)} as {file_name} in {base_dir} directory.")
        print(f"File path is: {full_path}")
        print("Directory contents: ")
        pprint.pprint(os.listdir(base_dir))


def write_json(data, base_dir: str, file_name: str, verbose=False):
    """
    Writes python list or dictonary data type to json.

    Parameters
    ==========
    data: list or dict - python data loaded in memory
    base_dir: str - directory/folder to save json file
    file_name: str - name of json file to save as
    verbose: bool - Prints out messsage to confirm where the file is saved and lists directory contents for visual verfication.

    Returns
    =======
    NoneType
    """

    if not Path(base_dir).is_dir():
        raise ValueError(f'Parameter {base_dir} is not a directory.')
    if not (isinstance(data, dict) or isinstance(data, list)):
        raise ValueError(
            f'Parameter {data} must be either python list or dict type, value passed is of {type(data)}')
    full_path = Path(base_dir, file_name)
    with open(full_path, "w") as wobj:
        json.dump(data, wobj, indent=4)

    if verbose:
        print(
            f"Wrote data of type {type(data)} as {file_name} in {base_dir} directory.")
        print(f"File path is: {full_path}")
        print("Directory contents: ")
        pprint.pprint(os.listdir(base_dir))
