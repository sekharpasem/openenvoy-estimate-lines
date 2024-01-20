import os.path
import sys

"""
Lines of code estimator
    - Blank lines
    - Comment lines
    - Code lines
    - Total lines
    
 @author: Sekhar P
"""
from src.estimators import JavaLinesOfCodeEstimator

class Estimator:

    def find_lines(self):
        """
        finds lines with blanks, comments
        :return:
        """
        file_paths = []
        for i in range(1, len(sys.argv)):
            file_paths.append(sys.argv[i])

        if len(file_paths) == 0:
            print('No file paths provided')
            sys.exit(0)

        print("Finding lines of code \n")
        for path in file_paths:
            if path.endswith('.java'):
                estimator = JavaLinesOfCodeEstimator(path)
            else:
                print("We do not have an implementation provided for this type of file")

            print("{}".format(path))
            print(' - Blank lines: ', estimator.noOfBlankLines())
            print(' - Comment lines: ', estimator.noOfCommentLines())
            print(' - Code lines: ', estimator.noOfCodeLines())
            print(' - Total lines: ', estimator.noOfTotalLines())
            print(' - Multi line comment lines: ', estimator.noOfMultiLineCommentLines())

            print('\n')


if __name__ == '__main__':
    Estimator().find_lines()
