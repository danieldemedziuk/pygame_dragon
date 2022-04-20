from csv import reader


def import_csv_layout(path):
    terrian_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrian_map.append(list(row))
        return terrian_map
