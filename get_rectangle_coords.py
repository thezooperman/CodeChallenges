# Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0. The image you get is known to have a single rectangle of 0s on a background of 1s.

# Write a function that takes in the image and returns the coordinates of the rectangle of 0's -- either top-left and bottom-right; or top-left, width, and height.

# Sample output:
# x: 3, y: 2, width: 3, height: 2
# 2,3 3,5
# 3,2 5,3 -- it's ok to reverse columns/rows as long as you're consistent


image = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

# image = [
#   [0]
# ]


def get_rectangle(image):
    start = None
    width = height = 0
    row = len(image)

    # find start
    for r in range(row):
        for c in range(len(image[r])):
            if image[r][c] == 0:
                start = (r, c)
                break
        if start is not None:
            break
    # width
    for c in range(start[1], len(image[0])):
        if image[start[0]][c] == 0:
            width += 1
    # height
    for r in range(start[0], row):
        if image[r][start[1]] == 0:
            height += 1
    return (start, width, height)


if __name__ == '__main__':
    print(get_rectangle(image))
