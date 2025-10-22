import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x, y, 'ro')

def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        print(f"({px}, {py})")
        plot(px, py)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    print("Midpoint Circle Points:")
    while x <= y:
        plot_circle_points(xc, yc, x, y)
        x += 1
        if p < 0:
            p += 2 * x + 3
        else:
            y -= 1
            p += 2 * (x - y) + 5

if __name__ == "__main__":
    plt.figure()
    midpoint_circle(0, 0, 10)
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
