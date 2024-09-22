numbers = [1,2,3,1,2,3,4,1]

def how_many_different_numbers(l):
    return len(set(l))

print(how_many_different_numbers(numbers))

# read through a server (e.g. apache or ngnix) log file.
# what were the different ip addresses that tried to access your server?

logs = '''192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
127.0.0.1 - - [28/Jul/2006:10:22:04 -0300] "GET / HTTP/1.0" 200 2216
x.x.x.90 - - [13/Sep/2006:07:01:53 -0700] "PROPFIND /svn/[xxxx]/Extranet/branches/SOW-101 HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:01:51 -0700] "PROPFIND /svn/[xxxx]/[xxxx]/trunk HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:00:53 -0700] "PROPFIND /svn/[xxxx]/[xxxx]/2.5 HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:00:53 -0700] "PROPFIND /svn/[xxxx]/Extranet/branches/SOW-101 HTTP/1.1" 401 587
x.x.x.90 - - [13/Sep/2006:07:00:21 -0700] "PROPFIND /svn/[xxxx]/[xxxx]/trunk HTTP/1.1" 401 587
127.0.0.1 - - [28/Jul/2006:10:27:32 -0300] "GET /hidden/ HTTP/1.0" 404 7218'''

def unique_ip_addresses(logs):
    ips = set()
    log_lines = logs.split('\n')
    for line in log_lines:
        words = line.split(' ')
        ips.add(words[0])
    return ips
print(unique_ip_addresses(logs))

# reading from the same server log, what response codes were returned to users?
# the 200 code represents OK, but there are also 403, 404 and 500 errors

def which_responses(logs):
    response_codes = {200:'OK', 401: 'Unauthorized', 404:'Not Found', 500:'Internal Server Error'}
    responses = set()
    log_lines = logs.split('\n')
    for line in log_lines:
        words = line.split(' ')
        response_code = int(words[-2])
        responses.add(response_codes[response_code])
    return responses

print(which_responses(logs))