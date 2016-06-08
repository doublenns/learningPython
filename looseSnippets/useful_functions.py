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


from contextlib import closing
def make_tarfile(output_filename, source_dir):
    '''
    Funtion to create tar files
    '''
    # contextlib.closing() needed for earlier versions of Python to use "with"
    with closing(tarfile.open(output_filename, "w:gz")) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
