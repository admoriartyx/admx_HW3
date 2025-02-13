# This is the .py file for Question 2

# Organization for this problem is kind of hairy. I am creating a new directory to store all of the heatmaps
# I generate for part a. My code will run a for loop that pulls each .txt file from the cloned repository
# and then outputs the associated heatmap into the new directory.

# Part a
import numpy as np
import matplotlib.pyplot as plt
import os

# Defining where to look for .txt files and where to store heatmaps
source_dir = './Local_density_of_states_near_band_edge'
output_dir = './local_density_of_states_heatmap'

# Double checking the output directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(11):  # Files are indexed from 0-10 with the same names essentially
    filename = f'local_density_of_states_for_level_{i}.txt'
    file_path = os.path.join(source_dir, filename)
    
    if os.path.exists(file_path):
        data = np.loadtxt(file_path, delimiter=',', converters={0: lambda s: float(s.decode('utf-8').strip(','))})
        
        plt.figure(figsize=(8, 6))
        heatmap = plt.imshow(data, cmap='viridis', aspect='auto')
        plt.colorbar(heatmap)
        plt.title(f'Local Density of States: Level {i}')
        plt.xlabel('Dimension 1') # I normally would label these x,y but the dimensions were ambiguous
        plt.ylabel('Dimension 2')
        
        # Heatmap routing
        output_file_path = os.path.join(output_dir, f'heatmap_level_{i}.png')
        plt.savefig(output_file_path)
        plt.close()
        print(f"Heatmap for Level {i} generated and saved.")
    else:
        print(f"File not found: {filename}")

# Part b
# Procedure here will be very similar, slight difference being the surface plotting function
# as opposed to heatmap

from mpl_toolkits.mplot3d import Axes3D

source_dir = './Local_density_of_states_near_band_edge'
output_dir = './local_density_of_states_height'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(11): 
    filename = f'local_density_of_states_for_level_{i}.txt'
    file_path = os.path.join(source_dir, filename)
    
    if os.path.exists(file_path):
        data = np.loadtxt(file_path, delimiter=',', converters={0: lambda s: float(s.decode('utf-8').strip(','))})

        fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 8))
        X = np.arange(data.shape[1])
        Y = np.arange(data.shape[0])
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(X, Y, data, cmap='viridis', linewidth=0, antialiased=False)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.title(f'Local Density of States Height Profile: Level {i}')
        ax.set_xlabel('Dimension 1')
        ax.set_ylabel('Dimension 2')
        ax.set_zlabel('Density')
        
        output_file_path = os.path.join(output_dir, f'height_profile_level_{i}.png')
        plt.savefig(output_file_path)
        plt.close()
        print(f"Height profile for Level {i} generated and saved.")
    else:
        print(f"File not found: {filename}")

# Note that my code indicates a file routing path that places the heatmap and state heights
# as different directories than the original location of the .txt files. This was for simplicity 
# when I was first approaching the problem and trying to organize the files, but as the problem asks,
# I will eventually move the heatmap and state heights folders into the original folder that contains
# the .txt files. This will disagree with the file paths indicated in the code, but just know that
# the code ran for the way I initially had the folders organized.

# Part c

# After consulting Dawson on the problem I will answer part c with an iterative analysis on each of the 
# data files given for Question 2. I will reference the heatmaps to come to some sort of
# conclusion about the physical phenomenon that occurred to produce such trends in the data.

# First I have to choose a subsection of the data to study. Every heatmap displays what look like 3
# vertices of sort, all spaced laterally between the values of 175 and 75 of dimension 2. I will pick
# these specific sector of the data to analyze across energy levels.

# Starting off with looking at the 0-3 energy levels, we notice a higher concentration, indicating
# a higher density of electrons around where the vertices appeear to be. The points are more tightly 
# packed and there is less variance from the highest point of concentration. As the energy levels increase
# into the 4-7 ranges, we see more scattering away from where the vertices lie. The average distance
# that the data sprawls away from the psuedo center of the data increases incrementally with each 
# increasing energy level. By the time we get to levels 9 and 10, the patterns look more so like 
# ripples in a pond or hexagonal lattices. This is a stark contrast to where we started at levels 0 and 1
# where the data was condensed into essentially points, as the heatmaps were far less colorful overall.

# The most simple explanation for this is that at higher energy levels, there exist more states of 
# quantum decoherence, contributing to more variance in the locations of the electrons and less confined
# patterns overall. At lower energy states, the data is more pronounced and confined because the electrons
# assume the lower energy states and are more stable. 

# Even in referencing the surface plots, there is a lot more decoherence and height variance across the
# studied band as the energy levels increase. This is my best interpretation of the data.

