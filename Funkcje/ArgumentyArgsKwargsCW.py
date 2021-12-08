def calculate_paint(efficiency_ltr_per_m2, *args):
    area = sum(args)
    paint = efficiency_ltr_per_m2 * area
    return paint


def log_it(*args):
    with open("log_it.txt", "a")as file:
        for line in args:
            file.write(line)
            file.write(" ")
            file.write("\n")


log_it('Starting processing forecasting')
