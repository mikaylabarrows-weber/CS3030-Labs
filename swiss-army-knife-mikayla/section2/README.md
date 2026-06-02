# Developers should never use shell=True because user input can be mistaken for executable commands.
# This can create an injection vulnerability where a user could intentionally or unintentionally
# exploit a CLI and send a command that could damage or compromise a system.

# Passing arguments as a list causes the input to be understood as data rather than potential commands.

