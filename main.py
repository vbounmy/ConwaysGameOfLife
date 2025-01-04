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
        index_line = padded_frame[0] + neighbors[0]
        index_column = padded_frame[1] + neighbors[1]
        if padded_frame[index_line, index_column] == 1:
            number_neighbors += 1

    return number_neighbors

def compute_next_frame(frame):

    padded_frame = numpy.pad(frame, 1, mode="constant")

    return frame

while True:
    print(frame)
    frame = compute_next_frame(frame)