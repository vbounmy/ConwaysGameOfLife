import numpy

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 1, 1, 1, 0, 0 ],
                     [0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 0, 0, 0, 0, 0 ]])

def compute_number_neighbors(padded_frame, index_line, index_column):
    number_neighbors = 0
    neighbors = [[-1, -1],
                 [-1, 0],
                 [-1, 1],
                 [0, -1],
                 [0, 1],
                 [1, -1],
                 [1, 0],
                 [1, 1]]

    for neighbor in neighbors:
        neighbors_line = index_line + neighbor[0]
        neighbors_column = index_column + neighbor[1]
        if padded_frame[neighbors_line, neighbors_column] == 1:
            number_neighbors += 1

    return number_neighbors

def compute_next_frame(frame):
    padded_frame = numpy.pad(frame, 1, mode="constant")

    for line in range(1, padded_frame.shape[0] - 1):
        for column in range(1, padded_frame.shape[1] - 1):
            cell_state = padded_frame[line, column]
            number_neighbors = compute_number_neighbors(padded_frame, line, column)
            if cell_state == 1:
                if number_neighbors != 2 or number_neighbors != 3:
                    cell_state = 0
            else:
                if number_neighbors == 3:
                    cell_state = 1
            frame[line - 1, column - 1] = cell_state

    return frame

while True:
    print(frame)
    frame = compute_next_frame(frame)