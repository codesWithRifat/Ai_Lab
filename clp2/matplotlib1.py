"""Plot a line graph showing temperature variations over a week."""
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [30, 32, 31, 29, 28, 27, 26]  # Example temperatures
plt.plot(days, temperatures, marker='o')
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.show()
