# Joseph Patambag
# August 19, 2024

#Module import
from Chap8Module import create_message_list

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to 
# make sure the messages were moved correctly.

msgs = ['The except clause(s) specify one or more exception handlers.',
        'When no exception occurs in the try clause, no exception handler is executed.',
        'When an exception occurs in the try suite, a search for an exception handler is started.',
        'This search inspects the except clauses in turn until one is found that matches the exception.']

messages = create_message_list(msgs, send_messages=[])

print(f"\nMessages : \n {messages[0]} \n")
print(f"New messages : \n {messages[1]} \n")
