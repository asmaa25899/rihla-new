# import matplotlib.pyplot as plt
# import seaborn as sns
# from PIL import Image
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import matplotlib.gridspec as gridspec

# # Load the image for the logo
# img_path = 'Rihla.jpeg'
# img = Image.open(img_path)

# # Create the main figure
# fig = plt.figure(figsize=(20, 18)) # Adjust figure size for dashboard

# # Define GridSpec for the layout: 4 rows, 2 columns
# # First row for KPIs, remaining three rows for plots (2 plots per row)
# gs = gridspec.GridSpec(4, 2, figure=fig, height_ratios=[0.3, 1, 1, 1]) # Adjust height ratios for KPI section

# # Subplot for KPIs (spanning both columns of the first row)
# ax_kpis = fig.add_subplot(gs[0, :])
# ax_kpis.set_title('Key Performance Indicators', fontsize=18, weight='bold')
# ax_kpis.axis('off') # Hide axes for KPI display

# # Display new KPIs as text in the dedicated subplot
# kpi_text_final = (
#     f"""Total Driver Cut from Rentals: ${total_driver_cut_from_rentals:,.2f}
# Maximum Trip Duration: {maximum_trip_duration} minutes
# Average Weight of Fragile Shipments: {average_weight_of_fragile_shipments:,.2f} kg
# Maximum Maintenance Cost for a Single Event: ${maximum_maintenance_cost_single_event:,.2f}
# """
# )
# ax_kpis.text(0.5, 0.5, kpi_text_final, ha='center', va='center', fontsize=14,
#              bbox=dict(boxstyle="round,pad=0.3", fc="lightgray", ec="blue", lw=1, alpha=0.6))

# # Subplot 1: Count of Rentals by Status (Bar Chart)
# ax1 = fig.add_subplot(gs[1, 0])
# sns.barplot(x='status', y='rental_count', data=rental_counts_by_status,
#             hue='status', palette='Blues_d', legend=False, ax=ax1)
# ax1.set_title('Count of Rentals by Status', fontsize=14)
# ax1.set_xlabel('Status', fontsize=12)
# ax1.set_ylabel('Number of Rentals', fontsize=12)

# # Subplot 2: Scatter Plot of Trip Distance vs. Trip Duration
# ax2 = fig.add_subplot(gs[1, 1])
# sns.scatterplot(x='duration', y='distance', data=trips_df, ax=ax2, color='deepskyblue', alpha=0.6)
# ax2.set_title('Trip Distance vs. Trip Duration', fontsize=14)
# ax2.set_xlabel('Duration (minutes)', fontsize=12)
# ax2.set_ylabel('Distance (km)', fontsize=12)

# # Subplot 3: Distribution of Freight Volume (Histogram with KDE)
# ax3 = fig.add_subplot(gs[2, 0])
# sns.histplot(freight_df['volume'], kde=True, bins=30, ax=ax3, color='skyblue')
# ax3.set_title('Distribution of Freight Volume', fontsize=14)
# ax3.set_xlabel('Volume', fontsize=12)
# ax3.set_ylabel('Frequency', fontsize=12)

# # Subplot 4: Average Maintenance Cost by Top 5 Malfunction Parts (Bar Chart)
# ax4 = fig.add_subplot(gs[2, 1])
# sns.barplot(y='malfunction_part', x='average_cost', data=avg_maintenance_cost_by_top_5_parts,
#             hue='malfunction_part', palette='Blues_d', legend=False, ax=ax4)
# ax4.set_title('Average Maintenance Cost by Top 5 Malfunction Parts', fontsize=14)
# ax4.set_xlabel('Average Cost ($)', fontsize=12)
# ax4.set_ylabel('Malfunction Part', fontsize=12)

# # Add Rihla.jpeg logo to the entire figure
# imagebox = OffsetImage(img, zoom=0.3) # Increased zoom further to make it more prominent
# ab = AnnotationBbox(imagebox, (0.05, 0.95), xycoords='figure fraction', frameon=False, box_alignment=(0, 1), zorder=10) # Added zorder=10
# fig.add_artist(ab)

# # Add a main title for the dashboard
# plt.suptitle('Rihla Logistics Operations Dashboard - New KPIs and Visualizations', y=0.99, fontsize=20, weight='bold')

# # Adjust layout and display
# plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust rect to make space for the suptitle
# plt.show()

# print("Extended Dashboard with new KPI cards and visualizations displayed.")





# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from PIL import Image
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import matplotlib.gridspec as gridspec

# # -----------------------------
# # Mock KPI Values
# # -----------------------------
# total_driver_cut_from_rentals = 125000
# maximum_trip_duration = 180
# average_weight_of_fragile_shipments = 32.5
# maximum_maintenance_cost_single_event = 4500

# # -----------------------------
# # Mock DataFrames
# # -----------------------------

# # Rentals by status
# rental_counts_by_status = pd.DataFrame({
#     "status": ["Completed", "Cancelled", "Ongoing"],
#     "rental_count": [320, 45, 75]
# })

# # Trips data
# trips_df = pd.DataFrame({
#     "duration": np.random.randint(10, 200, 200),
#     "distance": np.random.randint(1, 120, 200)
# })

# # Freight data
# freight_df = pd.DataFrame({
#     "volume": np.random.normal(50, 15, 300)
# })

# # Maintenance data
# avg_maintenance_cost_by_top_5_parts = pd.DataFrame({
#     "malfunction_part": ["Engine", "Brakes", "Tires", "Battery", "Transmission"],
#     "average_cost": [3200, 1800, 1200, 950, 4100]
# })

# # -----------------------------
# # Load Logo Image
# # -----------------------------
# # ⚠️ تأكدي إن الصورة موجودة جنب الملف
# img_path = "Rihla.jpeg"
# try:
#     img = Image.open(img_path)
# except FileNotFoundError:
#     img = None

# # -----------------------------
# # Create Figure & Layout
# # -----------------------------
# fig = plt.figure(figsize=(20, 18))
# gs = gridspec.GridSpec(4, 2, figure=fig, height_ratios=[0.35, 1, 1, 1])

# # -----------------------------
# # KPI Section
# # -----------------------------
# ax_kpis = fig.add_subplot(gs[0, :])
# ax_kpis.axis("off")
# ax_kpis.set_title("Key Performance Indicators", fontsize=20, weight="bold")

# kpi_text = f"""
# Total Driver Cut from Rentals: ${total_driver_cut_from_rentals:,.2f}
# Maximum Trip Duration: {maximum_trip_duration} minutes
# Average Weight of Fragile Shipments: {average_weight_of_fragile_shipments:.2f} kg
# Maximum Maintenance Cost (Single Event): ${maximum_maintenance_cost_single_event:,.2f}
# """

# ax_kpis.text(
#     0.5, 0.5, kpi_text,
#     ha="center", va="center",
#     fontsize=14,
#     bbox=dict(boxstyle="round,pad=0.5", fc="#EAF4FF", ec="#1f77b4")
# )

# # -----------------------------
# # Chart 1: Rentals by Status
# # -----------------------------
# ax1 = fig.add_subplot(gs[1, 0])
# sns.barplot(
#     data=rental_counts_by_status,
#     x="status",
#     y="rental_count",
#     palette="Blues",
#     ax=ax1
# )
# ax1.set_title("Count of Rentals by Status")
# ax1.set_xlabel("Status")
# ax1.set_ylabel("Number of Rentals")

# # -----------------------------
# # Chart 2: Trip Distance vs Duration
# # -----------------------------
# ax2 = fig.add_subplot(gs[1, 1])
# sns.scatterplot(
#     data=trips_df,
#     x="duration",
#     y="distance",
#     alpha=0.6,
#     ax=ax2
# )
# ax2.set_title("Trip Distance vs Trip Duration")
# ax2.set_xlabel("Duration (minutes)")
# ax2.set_ylabel("Distance (km)")

# # -----------------------------
# # Chart 3: Freight Volume Distribution
# # -----------------------------
# ax3 = fig.add_subplot(gs[2, 0])
# sns.histplot(
#     freight_df["volume"],
#     kde=True,
#     bins=30,
#     color="skyblue",
#     ax=ax3
# )
# ax3.set_title("Distribution of Freight Volume")
# ax3.set_xlabel("Volume")
# ax3.set_ylabel("Frequency")

# # -----------------------------
# # Chart 4: Maintenance Cost
# # -----------------------------
# ax4 = fig.add_subplot(gs[2, 1])
# sns.barplot(
#     data=avg_maintenance_cost_by_top_5_parts,
#     x="average_cost",
#     y="malfunction_part",
#     palette="Blues",
#     ax=ax4
# )
# ax4.set_title("Average Maintenance Cost by Top 5 Parts")
# ax4.set_xlabel("Average Cost ($)")
# ax4.set_ylabel("Part")

# # -----------------------------
# # Add Logo (if exists)
# # -----------------------------
# if img is not None:
#     imagebox = OffsetImage(img, zoom=0.25)
#     ab = AnnotationBbox(
#         imagebox,
#         (0.02, 0.95),
#         xycoords="figure fraction",
#         frameon=False
#     )
#     fig.add_artist(ab)

# # -----------------------------
# # Final Layout
# # -----------------------------
# plt.suptitle(
#     "Rihla Logistics Operations Dashboard",
#     fontsize=22,
#     weight="bold",
#     y=0.99
# )

# plt.tight_layout(rect=[0, 0, 1, 0.96])
# plt.show()





import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.gridspec as gridspec

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Rihla Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🚚 Rihla Logistics Operations Dashboard")

# -----------------------------
# Mock KPI Values
# -----------------------------
total_driver_cut_from_rentals = 125000
maximum_trip_duration = 180
average_weight_of_fragile_shipments = 32.5
maximum_maintenance_cost_single_event = 4500

# -----------------------------
# KPIs (Streamlit Style)
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Driver Cut", f"${total_driver_cut_from_rentals:,.0f}")
col2.metric("⏱ Max Trip Duration", f"{maximum_trip_duration} min")
col3.metric("📦 Avg Fragile Weight", f"{average_weight_of_fragile_shipments} kg")
col4.metric("🛠 Max Maintenance Cost", f"${maximum_maintenance_cost_single_event:,.0f}")

st.divider()

# -----------------------------
# Mock Data
# -----------------------------
rental_counts_by_status = pd.DataFrame({
    "status": ["Completed", "Cancelled", "Ongoing"],
    "rental_count": [320, 45, 75]
})

trips_df = pd.DataFrame({
    "duration": np.random.randint(10, 200, 200),
    "distance": np.random.randint(1, 120, 200)
})

freight_df = pd.DataFrame({
    "volume": np.random.normal(50, 15, 300)
})

avg_maintenance_cost_by_top_5_parts = pd.DataFrame({
    "malfunction_part": ["Engine", "Brakes", "Tires", "Battery", "Transmission"],
    "average_cost": [3200, 1800, 1200, 950, 4100]
})

# -----------------------------
# Create Figure
# -----------------------------
fig = plt.figure(figsize=(18, 14))
gs = gridspec.GridSpec(2, 2, figure=fig)

# Chart 1
ax1 = fig.add_subplot(gs[0, 0])
sns.barplot(
    data=rental_counts_by_status,
    x="status",
    y="rental_count",
    palette="Blues",
    ax=ax1
)
ax1.set_title("Rentals by Status")

# Chart 2
ax2 = fig.add_subplot(gs[0, 1])
sns.scatterplot(
    data=trips_df,
    x="duration",
    y="distance",
    alpha=0.6,
    ax=ax2
)
ax2.set_title("Trip Distance vs Duration")

# Chart 3
ax3 = fig.add_subplot(gs[1, 0])
sns.histplot(
    freight_df["volume"],
    kde=True,
    bins=30,
    color="skyblue",
    ax=ax3
)
ax3.set_title("Freight Volume Distribution")

# Chart 4
ax4 = fig.add_subplot(gs[1, 1])
sns.barplot(
    data=avg_maintenance_cost_by_top_5_parts,
    x="average_cost",
    y="malfunction_part",
    palette="Blues",
    ax=ax4
)
ax4.set_title("Maintenance Cost by Part")

plt.tight_layout()

# -----------------------------
# Show Figure in Streamlit
# -----------------------------
st.pyplot(fig)

# -----------------------------
# Optional: Show Data
# -----------------------------
with st.expander("📄 View Raw Data"):
    st.write("Rental Status Data")
    st.dataframe(rental_counts_by_status)

    st.write("Trips Data")
    st.dataframe(trips_df.head())

    st.write("Freight Data")
    st.dataframe(freight_df.head())
