import argparse
import datetime
import sys
import psutil

VERSION='1.0'

class PyPs(object):
    """
    pyps - Python process reporting tool.

    """

    def __init__(self, arg_dict):
        """
        Constructor

        """

        # Dynamically populate our local attributes from the dictionary
        self.__dict__.update(arg_dict)

        # pid is required argument and is guaranteed to exist
        # Check that provided pid is a valid running process
        if self.pid not in psutil.get_pid_list():
            print 'Error: Invalid PID (%d)' % self.pid
            sys.exit(1)

    def age(self):
        """
        Age
        """
        pass

    def ram(self):
        """
        RAM
        """
        print "RAM"
        return self

    def detailed(self):
        """
        Detail
        """
        print "Detail"
        return self

def main():
    """
    Process reporting tool in Python.

    - provide a time option to list all process at least this old

    """

    parser = argparse.ArgumentParser(description='Python process reporting tool.', version=VERSION)
    parser.add_argument('pid', help='The process to show information about.', type=int)
    parser.add_argument('-d', '--detail', action='store_true')
    args = vars(parser.parse_args())

    pyps = PyPs(args)
    print pyps.ram().detailed()

#    created_epoch = psutil.Process(pid).create_time
#    delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(created_epoch)
#    print 'Process was created at: ', datetime.datetime.fromtimestamp(created_epoch).strftime('%Y-%m-%d %H:%m:%s')
#    print 'Process has been running for ', delta


if __name__ == '__main__':
    main()
