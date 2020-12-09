#!/usr/bin/python

import os
import argparse
import json


def parse_logs(log_path, result, save_json=False):
    top_queries = 10
    total = 0
    requests_type = {'GET': 0, 'HEAD': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0, 'CONNECT': 0, 'OPTIONS': 0, 'TRACE': 0}
    top_largest_requests = {}
    top_client_errors = {}
    top_redirect_requests = {}
    with open(log_path) as file:
        for line in file:
            total += 1
            split_line = line.strip().split()
            requests_type[split_line[5][1:]] += 1
            top_largest_requests[split_line[9]] = [split_line[6], split_line[8], split_line[0]]
            if len(top_client_errors) <= top_queries and 399 < int(split_line[8]) < 500:
                top_client_errors[split_line[9]] = [split_line[6], split_line[8], split_line[0]]
            if len(top_redirect_requests) <= top_queries and 299 < int(split_line[8]) < 400:
                top_redirect_requests[split_line[9]] = [split_line[6], split_line[8], split_line[0]]
    top_ten_largest_requests = list(
        reversed(sorted(top_largest_requests.iteritems(), key=lambda x: int(x[0]) if x[0].isdigit() else 0)))[
                               :top_queries]
    top_ten_client_errors = list(
        reversed(sorted(top_client_errors.iteritems(), key=lambda x: int(x[0]) if x[0].isdigit() else 0)))[
                            :top_queries]
    top_ten_redirect_requests = list(
        reversed(sorted(top_redirect_requests.iteritems(), key=lambda x: int(x[0]) if x[0].isdigit() else 0)))[
                                :top_queries]
    with open('{}.txt'.format(result), 'w') as file:
        file.write("total count in log is ")
        file.write(str(total))
        for key, value in requests_type.items():
            if value > 0:
                file.write('count of {} is {}\n'.format(key, value))
        file.write("\ntop ten logs by size:\n\n")
        for el in top_ten_largest_requests:
            file.write(
                '{} {} {} {}\n'.format(el[0], el[1][0], el[1][1], el[1][2]))
        file.write("\ntop ten logs of client errors:\n\n")
        for el in top_ten_client_errors:
            file.write('{} {} {}\n'.format(el[1][0], el[1][1], el[1][2]))
        file.write("\ntop ten logs of server errors:\n\n")
        for el in top_ten_redirect_requests:
            file.write('{} {} {}\n'.format(el[1][0], el[1][1], el[1][2]))

    if save_json:
        with open('{}.json'.format(result), 'w') as file:
            json.dump({
                'total': total,
                'requests_type': requests_type,
                'top_largest': top_ten_largest_requests,
                'top_client_errors': top_ten_client_errors,
                'top_server_errors': top_ten_redirect_requests
            }, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default=None)
    parser.add_argument('--dir', type=str, default=None)
    parser.add_argument('--json', type=int, default=0)
    args = parser.parse_args()

    if args.dir:
        for name in os.listdir(args.dir):
            parse_logs(os.path.join(args.dir, name), name, args.json)
    else:
        parse_logs(args.file, args.file, args.json)
