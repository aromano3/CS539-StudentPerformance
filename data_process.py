import numpy as np

def get_data():

    with open('student-por.csv') as f:
        por_data = np.genfromtxt(f, delimiter=';', dtype='unicode')  

    for row_idx in range(len(por_data)):
        for col_idx in range(len(por_data[row_idx])):
            por_data[row_idx, col_idx] = por_data[row_idx, col_idx].strip('"')
    por_headers = por_data[0,:]
    por_data = por_data[1:, :]

    with open('student-mat.csv') as f:
        mat_data = np.genfromtxt(f, delimiter=';', dtype='unicode')  

    for row_idx in range(len(mat_data)):
        for col_idx in range(len(mat_data[row_idx])):
            mat_data[row_idx, col_idx] = mat_data[row_idx, col_idx].strip('"')
    mat_headers = mat_data[0,:]
    mat_data = mat_data[1:, :]
    
    return ((mat_headers,mat_data),(por_headers,por_data))