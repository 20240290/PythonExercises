# Joseph Patambag
# August 19, 2024

#Module import
import Chap8Module as module

# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), 
# which prints each text message.

module.show_messages(['The except clause(s) specify one or more exception handlers.',
                      'When no exception occurs in the try clause, no exception handler is executed.',
                      'When an exception occurs in the try suite, a search for an exception handler is started.',
                      'This search inspects the except clauses in turn until one is found that matches the exception.'])