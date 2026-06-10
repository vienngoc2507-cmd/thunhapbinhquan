import wbdata
import pandas as pd
import matplotlib.pyplot as plt
# GDP bình quân đầu người (USD hiện hành)
indicator = {
    'NY.GDP.PCAP.CD': 'GDP_PER_CAPITA'
}
# Lấy dữ liệu Việt Nam từ 2000-2024
df = wbdata.get_dataframe(
    indicator,
    country='VN',
    date=('2000', '2024')
)
# Sắp xếp theo năm tăng dần
df = df.sort_index()
# Hiển thị dữ liệu
print(df)
# Vẽ biểu đồ
plt.figure(figsize=(10, 4))
plt.plot(
    df.index,
    df['GDP_PER_CAPITA'],
    marker='o',
    linewidth=2
)
plt.title('GDP bình quân đầu người Việt Nam (2000-2024)', fontsize=15)
plt.xlabel('Năm')
plt.ylabel('USD/người')
plt.grid(True, linestyle='--', alpha=0.7)
# Hiển thị giá trị trên từng điểm
for x, y in zip(df.index, df['GDP_PER_CAPITA']):
    plt.text(x, y, f'{y:.0f}', fontsize=8)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
