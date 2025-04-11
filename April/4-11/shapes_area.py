
def calculate_area(shape, *args, **kwargs):  # declare function with args and kwargs
    try:
        # calculate area for circle
        if shape == "circle":
            for arg in args:
                area = 3.14*(pow(arg, 2))
        # calculate area for rectangle
        elif shape == "rectangle":
            width = kwargs.get("width")
            hight = kwargs.get("hight")
            area = width*hight
        # calculate area for triangle
        elif shape == "triangle":
            base = kwargs.get("base")
            hight_trian = kwargs.get("hight_trian")
            area = 0.5 * base * hight_trian

        return area

    except Exception as e:
        print("Error: ", e)


# call values for circle
area_circle = calculate_area("circle", 2)
print(f'area of circle is: {area_circle}')
# call values for rectangle
area_rect = calculate_area("rectangle", width=2, hight=2)
print(f'area of circle is: {area_rect}')

# call values for triangle
area_trian = calculate_area("triangle", base=4, hight_trian=6)
print(f'area of triangle is: {area_trian}')

# call error value
area_tri = calculate_area("tri", base=4, hight_trian=6)
print(area_tri)
