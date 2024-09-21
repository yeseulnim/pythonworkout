# write a function, get_rainfall, that tracks rainfall in a number of cities
# users of your program will enter the name of a city
# if the city name is blank, then the function prints a report before exiting
# if the city name isn't blank, the program should also ask the user how much rain has fallen in that city
# after the user enters the quantity of rain, the program again asks them for city name, rainfall amount, etc
# until the user presses enter instead of typing the name of a city

def get_rainfall():
    all_rainfall = {}
    while True:
        city = input("input city:")
        if not city:
            break
        else:
            try:
                rainfall = int(input("input rainfall amount in numbers:"))
            except ValueError:
                print("Please enter number only.")
                continue
            all_rainfall[city] = all_rainfall.get(city, 0) + rainfall
    print("Report")
    for (key, value) in all_rainfall.items():
        print(f"{key}: {value}")

# get_rainfall()

# instead of printing just the total rainfall for each city,
# print the total rainfall and the average rainfall for reported days
# thus, if you were to enter 30, 20, and 40 for boston,
# you would see that the total was 90 and the average was 30

def get_avg_rainfall():
    all_rainfall = {}
    while True:
        city = input("input city:")
        if not city:
            break
        else:
            try:
                rainfall = int(input("input rainfall amount in numbers:"))
            except ValueError:
                print("Please enter number only.")
                continue
            base_rainfall = all_rainfall.get(city, [0,0])
            all_rainfall[city] = [base_rainfall[0]+1, base_rainfall[1]+rainfall]
    print("Report")
    for key, value in all_rainfall.items():
        print(f"{key}: total {value[1]}, average {value[1]/value[0]}")

# get_avg_rainfall()



# Open a log file from a Unix/Linux system - for example, one from the Apache server.
# For each response code (i.e. three-digit code indicating the HTTP request's success or failure)
# store a list of IP addresses that generated that code

logs = '''192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
127.0.0.1 - - [28/Jul/2006:10:22:04 -0300] "GET / HTTP/1.0" 200 2216
x.x.x.90 - - [13/Sep/2006:07:01:53 -0700] "PROPFIND /svn/[xxxx]/Extranet/branches/SOW-101 HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:01:51 -0700] "PROPFIND /svn/[xxxx]/[xxxx]/trunk HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:00:53 -0700] "PROPFIND /svn/[xxxx]/[xxxx]/2.5 HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:00:53 -0700] "PROPFIND /svn/[xxxx]/Extranet/branches/SOW-101 HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:00:21 -0700] "PROPFIND /svn/[xxxx]/[xxxx]/trunk HTTP/1.1" 401 587
127.0.0.1 - - [28/Jul/2006:10:27:32 -0300] "GET /hidden/ HTTP/1.0" 404 7218'''

def save_http(log):
    http_per_response_code = {}
    lines = log.split('\n')
    for line in lines:
        line_split = line.split(" ")
        response_code = line_split[-2]
        http = line_split[0]
        http_per_response_code[response_code] = http_per_response_code.get(response_code, []) + [http]
    for key, value in http_per_response_code.items():
        print(f"{key} : {set(value)}")

save_http(logs)

# read through a text file on disk.
# use a dict to track how many words of each length are in the file
# that is, how many three-letter words, four-letter words etc
# display your results


filepath = "C:/Users/user/Downloads/Noto_Serif_KR/OFL.txt"

def word_length(filepath):
    f = open(filepath, 'r')
    word_length_dict = {}
    while line := f.readline():
        words = line.split(" ")
        for word in words:
            word_length = len(word)
            word_length_dict[word_length] = word_length_dict.get(word_length,0) + 1
    f.close()
    for word_length, count in dict(sorted(word_length_dict.items())).items():
        print(f"{word_length} lettered word : {count} times")

word_length(filepath)

