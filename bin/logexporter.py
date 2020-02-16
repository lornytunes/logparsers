#!/usr/bin/env python3

import sys
import csv
import argparse

from logparsers import READER_MAP

# egrep -h '/maillist/[A-Za-z@-\.]+/add/' test.log.* > mltest.log
# logexporter -v -f apache -o mltest.tsv mltest.log 2>errs.txt
# csvcut -t -n mlrequests.csv
# group by column 5, count column 1
# aggregate -d '\t' -k5  -c1 -p mltest.tsv
# csvformat -t mltest.tsv > mltest.csv
# logexporter -v -f postfix all.log -o mail.tsv 2>errs.txt


def main(reader, filenames, output, verbose):
    for i, filename in enumerate(filenames, start=1):
        numfailed = 0
        writer = csv.DictWriter(output, fieldnames=reader.FIELD_NAMES, dialect='excel-tab')
        if i == 1:
            writer.writeheader()
        for d in reader(filename):
            if d:
                writer.writerow(d)
            else:
                numfailed += 1
        if verbose and numfailed > 0:
            sys.stderr.write('{}: {} failed\n'.format(filename, numfailed))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Exports logfiles to CSV.')
    parser.add_argument(
        'filenames',
        metavar='FILENAMES',
        nargs='+',
        help='List of input files'
    )
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='Inputfile format; one of {}'.format(', '.join(READER_MAP.keys())))
    parser.add_argument(
        '-o', '--out',
        type=argparse.FileType('w'), default=sys.stdout,
        metavar='OUTPUT',
        help='The file where the output should be written (default: write to stdout)')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='output parse errors')
    args = parser.parse_args()
    if args.format not in READER_MAP.keys():
        print('*** Usage error: invalid logfile format')
        parser.print_usage()
        sys.exit(1)
    # separate logfiles
    main(READER_MAP[args.format], args.filenames, args.out, args.verbose)
