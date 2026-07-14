import os
import psutil

process = psutil.Process(os.getpid())

starting_memory = process.memory_info().rss / (1024 ** 2) # Memory in MB
print(f"Starting memory footprint: {starting_memory:.2f} MB")

print ("Performing Computations...")

# Heavy computation!
numbers = list(range(1, 5000001))

ending_memory = process.memory_info().rss / (1024 ** 2)
print(f"Ending memory footprint: {ending_memory:.2f} MB")

memory_used = ending_memory - starting_memory
print(f"Memory consumed during computation: {memory_used:.2f} MB")

# MEMORY PEAK OBSERVED: Consumed 191.25MB of Memory!

# A "runaway script" with a memory leak can crash a production server. 
# Let's write an automation tool that monitors itself.

# Logic: Use psutil.Process(os.getpid()) to target the script's own active process ID and read its current memory usage and 
# CPU time.

# Action: Have the script print its starting memory footprint, 
# perform a heavy computational task (like generating a list of 5,000,000 numbers), 
# and then calculate and log how much memory it consumed to process that data.

# Deliverable: Push the script to GitHub. In the code's comments, specify the "Memory Peak" you observed during testing.