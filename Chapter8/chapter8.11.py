# Joseph Patambag
# August 19, 2024

#Module import
from Chap8Module import archived_messages

# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the 
# original list has retained its messages.

msgs = ['The except clause(s) specify one or more exception handlers.',
        'When no exception occurs in the try clause, no exception handler is executed.',
        'When an exception occurs in the try suite, a search for an exception handler is started.',
        'This search inspects the except clauses in turn until one is found that matches the exception.']

messages = archived_messages(msgs, send_messages=[])

print(f"\nMessages : \n {messages[0]} \n")
print(f"New messages : \n {messages[1]} \n")