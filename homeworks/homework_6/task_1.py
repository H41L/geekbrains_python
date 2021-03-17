def parse_line(line):
    remote_addr = line.split(' - - ')[0]
    temp = line.split('] "')[1].split(' /')
    request_type = temp[0]
    requested_resource = '/' + temp[1].split(' HTTP')[0]
    return remote_addr, request_type, requested_resource


if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        parsed_result = [parse_line(line) for line in f]
        print(parsed_result)
