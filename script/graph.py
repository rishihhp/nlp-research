import matplotlib.pyplot as plt

# Data
file_sizes = [7547, 13248, 28496]
runtimes_trial_1 = [9.75, 15.77, 32.59]
runtimes_trial_2 = [9.75, 15.77, 32.59]
runtimes_trial_3 = [9.75, 15.77, 32.59]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(file_sizes, runtimes_trial_1, marker='o', label='Trial 1')
plt.plot(file_sizes, runtimes_trial_2, marker='o', label='Trial 2')
plt.plot(file_sizes, runtimes_trial_3, marker='o', label='Trial 3')

plt.xlabel('File Size (bytes)')
plt.ylabel('Runtime (s)')
plt.title('Runtime analysis for varying byte size in the computational model')
plt.legend()
plt.grid(True)

plt.show()
