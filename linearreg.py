# y = m* x + c
from matplotlib import pyplot as plt
from random import randint

#assigns values for coefficient (m) and constant (c) for the system to itterate through later
all_ms = [x*0.1 for x in range(-100, 100)]
all_cs = [x*0.1 for x in range(-100, 100)]

x_vals = []
y_vals = []
y_vals2 = []

#selects random values of x and y
for x in range(10):
    x_vals.append(randint(0, 30))
    y_vals.append(randint(0, 30))

d1 = list(zip(x_vals, y_vals))

#calculates y for selected m, c and x values 
def get_y(m, c, point):
    x = point[0]
    y = m * x+c
    return y

#calculate error between point and slope
def find_error(m, c, point):
    y_point = point[1]
    y_slope = get_y(m, c, point)
    return abs(y_point - y_slope)

#calculates collective error between all points and slope to determine how well the model fits
def calculate_all_error(m, c, points):
    error = 0
    for point in points:
        error += find_error(m, c, point)
    return error

#returning best fitting slope
def print_slope(best_m, best_c, x_vals):
    for x in x_vals:
        y_vals2.append(best_m * x + best_c)
    return y_vals2

#calculates the best fitting slope by itterating through all m coefficients and all c constants between -100 to 100
def find_coefficients(all_ms, all_cs, points):
    best_error = float("inf")
    best_m = 0
    best_c = 0
    for m in all_ms:
        for c in all_cs:
            if best_error > calculate_all_error(m, c, points):
                best_m = m
                best_c = c
                best_error = calculate_all_error(m, c, points)
    print_slope(best_m, best_c, x_vals)
    return(best_m, best_c, best_error)


print(find_coefficients(all_ms, all_cs, d1))

sorted_y = sorted(y_vals2)

#visualising the datapoints
plt.plot(x_vals, y_vals, linestyle='', marker='o', color='green')

#visualising the linear regression slope
plt.plot(sorted(x_vals), sorted_y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Linear regression of randomised data points')

plt.show()
