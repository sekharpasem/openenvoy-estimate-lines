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
from src.estimators import JavaLinesOfCodeEstimator, PythonLinesOfCodeEstimator
import estimator_mapping

class Estimator:
    def exists(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

    def find_lines(self):
        file_paths = []
        for i in range(1, len(sys.argv)):
            file_paths.append(sys.argv[i])

        if len(file_paths) == 0:
            print('No file paths provided')
            sys.exit(0)

        print("Finding lines of code \n")
        for path in file_paths:
            if not self.exists(path):
                print("Provided file path does not exists")
            estimator = estimator_mapping[path.split('.')[-1]]

            print("{}".format(path))
            print(' - Blank lines: ', estimator.noOfBlankLines())
            print(' - Comment lines: ', estimator.noOfCommentLines())
            print(' - Code lines: ', estimator.noOfCodeLines())
            print(' - Total lines: ', estimator.noOfTotalLines())
            print(' - Multi line comment lines: ', estimator.noOfMultiLineCommentLines())

            print('\n')

if __name__ == '__main__':
    Estimator().find_lines()

