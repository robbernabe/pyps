import argparse
import datetime
import sys
import psutil

def main():
    """
    Process reporting tool in Python.

    - provide a time option to list all process at least this old

    """

    parser = argparse.ArgumentParser(description='Python process reporting tool.')
    parser.add_argument('-p', '--pid', help='The process to display start time for.', required=True, type=int)
    args = vars(parser.parse_args())

    # Check that provided pid is a valid running process
    if args['pid'] not in psutil.get_pid_list():
        print "Not a valid running process."
        sys.exit(1)
    else:
        pid = args['pid']

    created_epoch = psutil.Process(pid).create_time
    delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(created_epoch)
    print 'Process was created at: ', datetime.datetime.fromtimestamp(created_epoch).strftime('%Y-%m-%d %H:%m:%s')
    print 'Process has been running for ', delta


if __name__ == '__main__':
    main()
