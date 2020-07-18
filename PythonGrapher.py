import matplotlib.pyplot as plt;
import pandas as pd;
import os;

# Get local directory
localDirectory = os.path.dirname(os.path.realpath(__file__));
fileToGraphPath = localDirectory+"\\FileToGraph.csv";
file = pd.read_csv(fileToGraphPath);

# Format data from read file
df = pd.DataFrame({'X': file.loc[:,"xAxis"], 'Y': file.loc[:,"yAxis"]});

# Use the formatted data and plot to their chosen axis
plt.plot(df.X, df.Y);

# Display the graph
plt.show();
