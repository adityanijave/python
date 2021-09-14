file = open("text2.txt","r")
# for_line_reading = file.readline()
# print(for_line_reading,end="")
# for_line_reading = file.readline()
# print(for_line_reading,end="")
# for_line_reading = file.readline()
# print(for_line_reading,end="")
# for_line_reading = file.readline()
# print(for_line_reading,end="")
# for_line_reading = file.readline()
# print(for_line_reading)

while True:
    for_line_reading = file.readline()
    print(for_line_reading,end="")
    if len(for_line_reading) == 0:
        break
file.close()