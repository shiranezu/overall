def grade_average(grades):
    avrg_grade= (sum(grades) / len(grades))

    if avrg_grade >=90:
        print('A')
    elif avrg_grade >=80:
        print('B')
    elif avrg_grade >=70:
        print('C')
    elif avrg_grade >=60:
        print('D')
    else :
        print('F')

grade_average([90, 95, 87, 78])

