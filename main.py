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

    for _ in neighbors:
        neighbors_line = index_line + neighbors[0]
        neighbors_column = index_column + neighbors[1]
        if padded_frame[neighbors_line, neighbors_column] == 1:
            number_neighbors += 1

    return number_neighbors

def compute_next_frame(frame):
    padded_frame = numpy.pad(frame, 1, mode="constant")

    for line in padded_frame[]

    return frame

while True:
    print(frame)
    frame = compute_next_frame(frame)