#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/env python
# coding: utf-8
# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
# Membaca database
data = pd.read_csv("D:/UAS/605603222_bukalapak.csv")
# Membuat bar chart dengan jumlah_sold sebagai sumbu X dan jumlah_rating sebagai sumbu Y
plt.plot(data['jumlah_sold'], data['jumlah_rating'])
# Menambahkan judul ke plot
plt.title("Jumlah Rating dan Jumlah Sold")
# Menetapkan label sumbu X dan Y
plt.xlabel('Jumlah Sold')
plt.ylabel('Jumlah Rating')
# Menampilkan plot
plt.show()


# In[ ]:




