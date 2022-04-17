import numpy as np

def process_data(data, headers):
    for header_idx, header in enumerate(headers):
        if header == "school":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "GP":
                    data[row_idx, header_idx] = 0
                else:
                    data[row_idx, header_idx] = 1
        elif header == "sex":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "F":
                    data[row_idx, header_idx] = 0
                else:
                    data[row_idx, header_idx] = 1
        elif header == "address":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "U":
                    data[row_idx, header_idx] = 0
                else:
                    data[row_idx, header_idx] = 1
        elif header == "famsize":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "LE3":
                    data[row_idx, header_idx] = 0
                else:
                    data[row_idx, header_idx] = 1
        elif header == "Pstatus":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "T":
                    data[row_idx, header_idx] = 0
                else:
                    data[row_idx, header_idx] = 1
        elif header == "Mjob" or header == "Fjob":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "teacher":
                    data[row_idx, header_idx] = 0
                elif data[row_idx, header_idx] == "health":
                    data[row_idx, header_idx] = 1
                elif data[row_idx, header_idx] == "services":
                    data[row_idx, header_idx] = 2
                elif data[row_idx, header_idx] == "at_home":
                    data[row_idx, header_idx] = 3
                else:
                    data[row_idx, header_idx] = 4
        elif header == "reason":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "home":
                    data[row_idx, header_idx] = 0
                elif data[row_idx, header_idx] == "reputation":
                    data[row_idx, header_idx] = 1
                elif data[row_idx, header_idx] == "course":
                    data[row_idx, header_idx] = 2
                else:
                    data[row_idx, header_idx] = 3
        elif header == "guardian":
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "mother":
                    data[row_idx, header_idx] = 0
                elif data[row_idx, header_idx] == "father":
                    data[row_idx, header_idx] = 1
                else:
                    data[row_idx, header_idx] = 2
        elif (header == "schoolsup" or header == "famsup" or header == "paid"
            or header == 'activities' or header == 'nursery' or header == 'higher'
            or header == 'higher' or header == 'internet' or header == 'romantic'):
            for row_idx in range(len(data[0:, header_idx])):
                if data[row_idx, header_idx] == "yes":
                    data[row_idx, header_idx] = 0
                else:
                    data[row_idx, header_idx] = 1
    return data.astype(int)

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
