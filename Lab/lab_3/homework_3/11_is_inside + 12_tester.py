def is_inside(point, rec):
    Bx = point[0]
    By = point[1]
    rec_x = rec [0]
    rec_y = rec [1]
    width = rec [2]
    height = rec [3]
    if (rec_x + width) > Bx > rec_x and (rec_y + height) > By > rec_y:
        return True
    else:
        return False


point_inside = is_inside([200,250],[140,60,100,200])
if point_inside == True:
    print("Your point is inside a rectangle :)")
else:
    print("Oops, your point is outside now!")
