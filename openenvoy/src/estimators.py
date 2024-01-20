class DefaultLinesOfCodeEstimator:

    def __init__(self, path, config):
        """
        path: path of the file

        """
        self.path = path

    def readFile(self):
        """
        Reads the file and returns the list of lines

        """
        with open(self.path, 'r') as f:
            return f.readlines()

    def noOfBlankLines(self):
        """
        Returns the number of blank lines in the file

        """
        lines = self.readFile()
        count = 0
        for line in lines:
            if line.strip() == '':
                count += 1
        return count

    def noOfCommentLines(self):
        """
        Returns the number of comment lines in the file

        """
        lines = self.readFile()
        count = 0
        for line in lines:
            if line.strip().startswith('#'):
                count += 1
        return count

    def noOfMultiLineCommentLines(self):
        """
        Returns the number of multi line comment lines in the file, there might be multiple block starting with 3 " and ending with 3 "
        """

        lines = self.readFile()
        count = 0
        is_comment = False
        for line in lines:
            if line.strip().startswith('"""') and not is_comment:
                is_comment = True
                count += 1
            elif line.strip().endswith('"""') and is_comment:
                is_comment = False
                count += 1
            elif is_comment:
                count += 1
        return count

    def noOfCodeLines(self):
        """
        Returns the number of code lines in the file

        """
        lines = self.readFile()
        count = 0
        for line in lines:
            if not line.strip().startswith('#') and line.strip() != '':
                count += 1
        return count

    def noOfTotalLines(self):
        """
        Returns the number of total lines in the file

        """
        lines = self.readFile()
        return len(lines)


class JavaLinesOfCodeEstimator(DefaultLinesOfCodeEstimator):

    def noOfBlankLines(self):
        """
        Returns the number of blank lines in the file
        """
        try:
            lines = self.readFile()
            count = 0
            for line in lines:
                if line.strip() == '':
                    count += 1
            return count
        except FileNotFoundError as e:
            print(e)
            raise ValueError('Invalid file path')

    def noOfCommentLines(self):
        """
        Returns the number of comment lines in the file
        """
        try:
            lines = self.readFile()
            count = 0
            for line in lines:
                if line.strip().startswith('//'):
                    count += 1
            return count
        except FileNotFoundError as e:
            print(e)
            raise ValueError('Invalid file path')

    def noOfCodeLines(self):
        """
        Returns the number of code lines in the file

        """

        try:
            lines = self.readFile()
            count = 0
            for line in lines:
                if not line.strip().startswith('//') \
                        and not line.strip().startswith('/*') \
                        and not line.strip().startswith('*') \
                        and not line.strip().startswith('/*') \
                        and line.strip() != '':
                    count += 1
            return count
        except FileNotFoundError as e:
            print(e)
            raise ValueError('Invalid file path')

    def noOfTotalLines(self):
        """
        Returns the number of total lines in the file
        """
        try:
            lines = self.readFile()
            return len(lines)
        except FileNotFoundError as e:
            print(e)
            raise ValueError('Invalid file path')

    def noOfMultiLineCommentLines(self):
        """
        Returns the number of multi line comment lines in the file, there might be multiple block starting with 3 " and ending with 3 "
        """

        lines = self.readFile()
        count = 0
        is_comment = False
        for line in lines:
            if line.strip().startswith('/*') and not is_comment:
                is_comment = True
                count += 1
            elif line.strip().endswith('*/') and is_comment:
                is_comment = False
                count += 1
            elif is_comment:
                count += 1
        return count


class PythonLinesOfCodeEstimator(DefaultLinesOfCodeEstimator):

    def noOfCommentLines(self):
        """
        Returns the number of comment lines in the file
        """
        try:
            lines = self.readFile()
            count = 0
            for line in lines:
                if line.strip().startswith('//'):
                    count += 1
            return count
        except FileNotFoundError as e:
            print(e)
            raise ValueError('Invalid file path')

    def noOfCodeLines(self):
        """
        Returns the number of code lines in the file

        """

        try:
            lines = self.readFile()
            count = 0
            for line in lines:
                if not line.strip().startswith('//') \
                        and not line.strip().startswith('"""') \
                        and not line.strip().startswith('*') \
                        and not line.strip().startswith('/*') \
                        and line.strip() != '':
                    count += 1
            return count
        except FileNotFoundError as e:
            print(e)
            raise ValueError('Invalid file path')

    def noOfMultiLineCommentLines(self):
        """
        Returns the number of multi line comment lines in the file, there might be multiple block starting with 3 " and ending with 3 "
        """

        lines = self.readFile()
        count = 0
        is_comment = False
        for line in lines:
            if line.strip().startswith('"""') and not is_comment:
                is_comment = True
                count += 1
            elif line.strip().endswith('"""') and is_comment:
                is_comment = False
                count += 1
            elif is_comment:
                count += 1
        return count
