#!python ./convert_image.py
# usage: run from folder that contains the script.

import os
import pathlib
import re
import sys
from PIL import Image
import numpy as np


def create_header_file(name: str, section: str, tensor_name: str, tensor_data: np.ndarray, output_path: str):
    """
    This function generates a header file containing the data from the numpy array provided.
    """
    file_path = pathlib.Path(f"{output_path}/" + name).resolve()
    # Create header file with npy_data as a C array
    raw_path = file_path.with_suffix(".h").resolve()
    with open(raw_path, "w") as header_file:
        header_file.write(
            "#include <tvmgen_default.h>\n"
            + f"const size_t {tensor_name}_len = {tensor_data.size};\n"
            + f'uint8_t {tensor_name}[] __attribute__((section("{section}"), aligned(16))) = "'
        )
        data_hexstr = tensor_data.tobytes().hex()
        for i in range(0, len(data_hexstr), 2):
            header_file.write(f"\\x{data_hexstr[i:i+2]}")
        header_file.write('";\n\n')


def create_headers():
    CREATE_HEADERS_FLAG = True
    PRINT_OUTPUT = False
    
    BASE_PATH=os.path.abspath(os.curdir)

    PREV_BASE_PATH=os.path.abspath(os.path.join(BASE_PATH, ".."))
    OUTPUT_PATH = os.path.join(PREV_BASE_PATH, "include")
    print(OUTPUT_PATH)
    # load data
    INP_DATA_PATH=os.path.join(BASE_PATH, "inp.npy")
    OUTP_DATA_PATH=os.path.join(BASE_PATH, "outp.npy")

    inp_data: np.ndarray = np.load(INP_DATA_PATH)
    outp_data: np.ndarray = np.load(OUTP_DATA_PATH)

    # input
    if CREATE_HEADERS_FLAG:
        create_header_file(
            name="input.h",
            section="input_data_sec",
            tensor_name="input",
            tensor_data=inp_data,
            output_path=OUTPUT_PATH
        )

    # output
    if CREATE_HEADERS_FLAG:
        create_header_file(
            name="output.h",
            section="output_data_sec",
            tensor_name="output",
            tensor_data=outp_data,
            output_path=OUTPUT_PATH
        )
    
    if PRINT_OUTPUT:
        outp_data_copy = outp_data.copy().flatten()
        inp_data_copy = inp_data.copy().flatten()

        print("Input >")
        for p in inp_data_copy:
            print(p)
        print("<")

        print("Output >")
        for p in outp_data_copy:
            print(p)
        print("<")





if __name__ == "__main__":
    create_headers()
