"""Create a bar chart comparing sales revenue across different regions."""
import matplotlib.pyplot as plt

regions = ['DhakaNorth', 'DhakaSouth', 'Chittagong', 'Rangpur']
revenue = [50000, 70000, 45000, 30000]
plt.bar(regions, revenue, color='skyblue',width=0.2)
plt.xlabel('Regions')
plt.ylabel('Sales Revenue (BDT)')
plt.title('Sales Revenue Across Different Regions')
plt.show()
