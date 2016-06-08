#!/usr/env/bin python

def mkdir_p(path):
    '''
    Function to mimic  POSIX `mkdir -p` functionality
    '''
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


