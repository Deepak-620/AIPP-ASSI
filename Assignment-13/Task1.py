def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    dispatch = {
        "rectangle": lambda x, y: area_rectangle(x, y),
        "square": lambda x, _: area_square(x),
        "circle": lambda x, _: area_circle(x),
    }
    shape = shape.lower()
    if shape in dispatch:
        return dispatch[shape](x, y)
    else:
        raise ValueError(f"Unknown shape: {shape}")
