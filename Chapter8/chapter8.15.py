# Joseph Patambag
# August 19, 2024

#Module import
from Chap8Module import printed_models

# 8-15. Printing Models: Put the functions for the example printing_models.py 
# in a separate file called printing_functions.py. Write an import statement 
# at the top of printing_models.py, and modify 
# the file to use the imported functions.

models = printed_models(['phone case', 'robot pendant', 'dodecahedron'], [])

print(f"The following models have been printed: \n {models}")