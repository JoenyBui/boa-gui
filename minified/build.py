import os

from pecutil.run import copy_folder_minify

__author__ = 'jbui'

if __name__ == '__main__':
    package_name = 'peui'

    LOCAL_FOLDER = os.path.dirname(__file__)
    SOURCE_LOCATION = os.path.join(os.path.split(LOCAL_FOLDER)[0], package_name)
    MINIFIED_LOCATION = os.path.join(LOCAL_FOLDER, package_name)

    # Copy folder and minify
    copy_folder_minify(SOURCE_LOCATION, MINIFIED_LOCATION)
