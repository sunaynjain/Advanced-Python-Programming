import numpy as np
import pandas as pd

room_rents = np.array([2500, 3500, 4500, 5000, 6000])

print("Mean Rent:", np.mean(room_rents))
print("Median Rent:", np.median(room_rents))
print("Maximum Rent:", np.max(room_rents))
print("Minimum Rent:", np.min(room_rents))

data = {
    "Room Number": [101, 102, 103, 104, 105],
    "Rent": room_rents
}

df = pd.DataFrame(data)

print("\nAll Hotel Rooms:")
print(df)

print("\nRooms with Rent Greater than 4000:")
print(df[df["Rent"] > 4000])
