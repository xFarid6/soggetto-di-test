import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 4, 5, 6])

np.save('filename', a)  # If you want to store more than one ndarray object in a single file, 
                        # save it as a .npz file using np.savez.

b = np.load('filename.npy')


csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', csv_arr)
np.loadtxt('new_file.csv')          # optional parameters such as header, footer, and delimiter

# While text files can be easier for sharing, .npy and .npz files are smaller and faster to read.

# maybe try loading a reply input file with this? or is pandas still better?


# TOGHETER WITH pandas  - maybe best option for reply big numbers

a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

df = pd.DataFrame(a)
print(df)
df.to_csv('pd.csv')             # save
data = pd.read_csv('pd.csv')    # read

np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')  # saving with np

# np.loadtxt('simple.csv', delimiter = ',', skiprows = 1) 