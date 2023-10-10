from TV import TV


def read_file(file):
    tvs = []
    f = open(file, 'r', encoding='utf8')
    for line in f:
        line = line.replace('\n', '')
        line = line.split(',')
        tvs.append(TV(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4])))
    return tvs


def write_file(tv_list, file):
    out_str = ''
    for tv in tv_list:
        out_str += f"{tv.str_for_file()}\n"
    f = open(file, 'w', encoding='utf8')
    f.write(out_str)


tvlista = read_file("db.txt")
for tv in tvlista: print(tv)     # Här ska programmet skriva namn, inställd kanal
                                 # och ljudnivå för båda tv-apparaten som finns i filen

tvlista[0].change_channel(5)
tvlista[1].increase_volume()
for tv in tvlista: print(tv)     # Här ska programmet skriva ut information
                                 # om båda tv-apparaterna (Observera att kanalen för
                                 # första tv:n måste ha ändrats till 1)
write_file(tvlista, "db.txt")
tvlista = read_file("db.txt")
for tv in tvlista: print(tv)