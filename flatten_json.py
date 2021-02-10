import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog


# Open file with dialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path) as f:
    data = json.load(f)

# Define feature list for dataframe
features = [
    "row_id",
    "sequence_id",
    "end_date",
    "name",
    "orderable",
    "period",
    "period_uom",
    "phone_number_flag",
    "price_type",
    "product_category",
    "product_sub_category",
    "product_type_code",
    "type",
    "vendor_part_number",
    "created_date",
    "created_by",
    "last_updated_date",
    "last_updated_by",
    "ts_event_notification_time"
]

# Create dataframe using json_normalize pandas function with necessary parameters
df = pd.json_normalize(data['OrderMaster']['Order']['item'],['OrderItems', 'item'], features)
print(df)

# Ask for directory where file should be exported
directory = filedialog.askdirectory()
save_file_path = directory+'/orders.csv'
print(save_file_path)

# Export dataframe to CSV file
df.to_csv(save_file_path, index=False)