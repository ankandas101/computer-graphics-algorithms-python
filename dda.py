import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x, y, 'ro')

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x = x1
    y = y1
    print("DDA Line Drawing Points:")
    for _ in range(steps + 1):
        print(f"({round(x)}, {round(y)})")
        plot(round(x), round(y))
        x += x_inc
        y += y_inc

if __name__ == "__main__":
    plt.figure()
    DDA(2, 2, 10, 6)
    plt.title("DDA Line Drawing Algorithm")
    plt.grid(True)
    plt.show()
