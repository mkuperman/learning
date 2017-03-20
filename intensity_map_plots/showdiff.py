import matplotlib.pyplot as plt;

maxx = 40000

#path with filename prefix
path='./1kk/day'
days=30

def show_diff(intensity_from = 1,intensity_to = 100):
    for i in range(days):
        lst2 = list();
        with open(path + str(i), 'r') as file:
            lines = file.readlines()
            lst = [0 for i in range(maxx)]
            for line in lines:
                if line != '_\n':
                    (x, y) = (line.split())
                    if int(x) < maxx - 1:
                        lst[int(x)] = (float(y))
                else:
                    lst2.append(sum(lst[intensity_from:intensity_to]))
                    lst = [0 for i in range(maxx)]
                    continue;
        plt.plot(lst2);
    plt.xlabel('hours')
    plt.ylabel('meters')
    plt.show()


def show_diff_at_time(time):
    plt.axes()
    for i in range(days):
        with open(path + str(i), 'r') as file:
            lines = file.readlines();
            currenttime = 0
            lst = [0 for i in range(maxx)]
            for line in lines:
                if line == '_\n':
                    currenttime += 1
                elif currenttime == time:
                    (x, y) = (line.split());
                    if int(x)!=0 & int(x) < maxx - 1:
                        lst[int(x)] = (float(y))
                else:
                    continue
            print(lst)
            plt.plot(lst)
    plt.xlabel('intensity')
    plt.ylabel('meters')
    plt.show()



show_diff();
show_diff_at_time(5)
