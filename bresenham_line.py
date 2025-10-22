import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x, y, 'ro')

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    print("Bresenham Line Points:")
    while True:
        print(f"({x1}, {y1})")
        plot(x1, y1)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

if __name__ == "__main__":
    plt.figure()
    bresenham_line(2, 2, 10, 6)
    plt.title("Bresenham Line Drawing Algorithm")
    plt.grid(True)
    plt.show()
