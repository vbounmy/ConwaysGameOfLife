import numpy

# frame = numpy.array([[0, 0, 0, 0, 0, 0, 0 ],
#                      [0, 0, 0, 0, 0, 0, 0 ],
#                      [0, 0, 0, 0, 0, 0, 0 ],
#                      [0, 0, 1, 1, 1, 0, 0 ],
#                      [0, 0, 0, 0, 0, 0, 0 ],
#                      [0, 0, 0, 0, 0, 0, 0 ],
#                      [0, 0, 0, 0, 0, 0, 0 ]])

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 0, 0, 0, 0, 0 ],
                     [0, 0, 0, 1, 1, 0, 0 ],
                     [0, 0, 1, 1, 0, 0, 0 ],
                     [0, 0, 0, 1, 0, 0, 0 ],
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
    next_frame = numpy.copy(frame)

    for line in range(1, padded_frame.shape[0] - 1):
        for column in range(1, padded_frame.shape[1] - 1):
            number_neighbors = compute_number_neighbors(padded_frame, line, column)
            if padded_frame[line, column] == 1:
                if number_neighbors != 2 and number_neighbors != 3:
                    next_frame[line - 1, column - 1] = 0
            else:
                if number_neighbors == 3:
                    next_frame[line - 1, column - 1] = 1

    frame = next_frame

    return frame

# while True:
for _ in range(10):
    print(frame)
    print("\n")
    frame = compute_next_frame(frame)