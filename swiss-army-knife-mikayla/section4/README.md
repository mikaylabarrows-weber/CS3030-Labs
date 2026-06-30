# if you wanted the script to scale and be able to check 1,000 sites, I would use
# asynchronous loops as opposed to synchronous. Synchronous loops waits for a request
# to finish before continuing to the next, which can cause the process to slow down. 
# The asynchronous loop allows for multiple requests to run concurrently, which prevents
# the process from freezing. 
