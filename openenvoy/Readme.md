
# Source Tree:
tests:
- Sample.java
- SampleWithMulti.java
- test.txt

src:
 All the source implementation is here
- lines_of_code_estimator.py
- estimators.py
  - We have java implementation here to find java realted files

# How to run:
> python src/lines_of_code_estimator.py tests/SampleWithMulti.java tests/Sample.java


# Output:
Finding lines of code 

tests/SampleWithMulti.java
 - Blank lines:  5
 - Comment lines:  3
 - Code lines:  6
 - Total lines:  20
 - Multi line comment lines:  6


tests/Sample.java
 - Blank lines:  3
 - Comment lines:  3
 - Code lines:  6
 - Total lines:  12
 - Multi line comment lines:  0