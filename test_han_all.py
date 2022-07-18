def get_coordinates(word, frameScale):
    from xml.dom import minidom
    from svg.path import parse_path
    import ast

    width = 1024
    height = 1024
    #fixed for the center
    division = 2

    #framescale
    # frameScale = 0.0002
    # frameScale = 0.00015
    # frameScale = 0.00008

    # pen up (m)
    pen_up= 0.03/frameScale

    #load zh2name file
    file = open("dict_zh2name.txt")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()

    #find the words
    filename = dictionary[word]

    #open the word file
    doc = minidom.parse(str(filename))


    coordinates_3d = [ [[] for i in range(3) ] for i in range(1)]


    total_len= len(doc.getElementsByTagName('path'))
    tick_matrix = [[0]*2]
    for ipath, path in enumerate(doc.getElementsByTagName('path')):
        if(ipath<total_len/2):
            continue
        # print(ipath)
        # print('Path', ipath)
        d = path.getAttribute('d')
        parsed = parse_path(d)
        # print('Objects:\n', parsed, '\n' + '-' * 20)
        coordinates_2d = [ [0]*3 ]
        
        for obj in parsed:
            # print(obj)
            # print(type(obj).__name__)
            # print(type(obj).__name__, ', start/end coords:', ((round(obj.start.real, 3), round(obj.start.imag, 3)), (round(obj.end.real, 3), round(obj.end.imag, 3))))
            # print('start/end coords:', ((round(obj.start.real, 3), round(obj.start.imag, 3)), (round(obj.end.real, 3), round(obj.end.imag, 3))))


            if not (tick_matrix[0]==round(obj.start.real, 3) and tick_matrix[1]==round(obj.start.imag, 3)):             
                coordinate = [round(obj.start.real-width/division, 3), -round(obj.start.imag-height/division, 3), 0]
                coordinates_2d.append(coordinate)
                #duplicate check
                tick_matrix = [round(obj.start.real, 3), round(obj.start.imag, 3)]

            if(type(obj).__name__ =='CubicBezier'):
                #control 1
                coordinate = [round(obj.control1.real-width/division, 3), -round(obj.control1.imag-height/division, 3), 0]
                coordinates_2d.append(coordinate)
                #control 2
                coordinate = [round(obj.control2.real-width/division, 3), -round(obj.control2.imag-height/division, 3), 0]
                coordinates_2d.append(coordinate)
            if(type(obj).__name__ =='QuadraticBezier'):
                #control
                coordinate = [round(obj.control.real-width/division, 3), -round(obj.control.imag-height/division, 3), 0]
                coordinates_2d.append(coordinate)

            if not (tick_matrix[0]==round(obj.end.real, 3) and tick_matrix[1]==round(obj.end.imag, 3)):     
                coordinate = [round(obj.end.real-width/division, 3), -round(obj.end.imag-height/division, 3), 0]
                coordinates_2d.append(coordinate)
                #duplicate check
                tick_matrix = [round(obj.end.real, 3), round(obj.end.imag, 3)]
        # print('-' * 20)

        del coordinates_2d[0]
        # pen up
        coordinate_pen_up = [round(obj.end.real-width/division, 3), -round(obj.end.imag-height/division, 3), pen_up]
        coordinates_2d.append(coordinate_pen_up)
        # 3D coordinates
        coordinates_3d.append(coordinates_2d)
        

    doc.unlink()
    del coordinates_3d[0]


    return(coordinates_3d)