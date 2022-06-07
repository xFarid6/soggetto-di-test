def find_line_gc(points):
    """
    Finds the line that best fits the points
    :param points: list of points
    :return: slope, y-intercept
    """
    x_sum = 0
    y_sum = 0
    x_squared_sum = 0
    x_y_product = 0
    for point in points:
        x_sum += point[0]
        y_sum += point[1]
        x_squared_sum += point[0] ** 2
        x_y_product += point[0] * point[1]
    n = len(points)
    slope = (n * x_y_product - x_sum * y_sum) / (n * x_squared_sum - x_sum ** 2)
    y_intercept = (y_sum - slope * x_sum) / n
    return slope, y_intercept


def find_line(x0, y0, x1, y1):
    if y0 == y1:
        return 0, y0
    if x0 == x1:
        return x0, 0
    else:
        # return (y1 - y0) / (x1 - x0), y0 - (y1 - y0) / (x1 - x0) * x0
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y0 - slope * x0
        return slope, y_intercept


from collections import defaultdict


def max_points_gc(points):
    slopes = defaultdict(int)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            slope, y_intercept = find_line(points[i][0], points[i][1], points[j][0], points[j][1])
            slopes[(slope, y_intercept)] += 1
    return max(slopes.values())


def max_points(points):
    if len(points) == 1:
        return 1
    lines = defaultdict(lambda: set())
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x0, y0 = points[i]
            x1, y1 = points[j]
            line = find_line(x0, y0, x1, y1)
            lines[line].add(i)
            lines[line].add(j)
    return max(len(lines[line]) for line in lines)


# time: O(n^2)
# space: O(n)