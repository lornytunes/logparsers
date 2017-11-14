#!/usr/bin/env python3

import sys
import argparse

from logparsers import READER_MAP


def main(reader, filenames, output, verbose):
    for filename in filenames:
        numread = 0
        numfailed = 0
        # get an instance of reader - we'll need to query its data property if an empty dictionary is returned
        logreader = reader(filename)
        for d in logreader:
            if d:
                numread += 1
            else:
                numfailed += 1
                output.write(logreader.data)
                output.write('\n')
        if verbose:
            print('{}: {} read, {} failed'.format(filename, numread, numfailed))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Separate parseable and non-parseable lines in server logfiles.')
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
        type=argparse.FileType('w'), default=sys.stderr,
        metavar='OUTPUT',
        help='The file where the unparseable lines should be written (default: write to stderr)')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='output detailed progress info')
    args = parser.parse_args()
    if args.format not in READER_MAP.keys():
        print('*** Usage error: invalid logfile format')
        parser.print_usage()
        sys.exit(1)
    # separate logfiles
    main(READER_MAP[args.format], args.filenames, args.out, args.verbose)
