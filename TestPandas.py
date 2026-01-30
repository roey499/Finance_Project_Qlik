import pandas as pd
from datetime import datetime
import os

# ודא שהתיקיה קיימת
os.makedirs("/data", exist_ok=True)

df = ps.DataFrame({
    "name": ["Dan", "Roey", "Nofar"],
    "score": [90, 85, 95]
})

filename = f"/data/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(filename, index=False)

print(f"Excel file saved to {filename}")