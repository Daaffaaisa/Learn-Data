import matplotlib.pyplot as plt

cities = ("Bogor", "Bandung", "Jakarta", "Semarang", "yogyakarta", "Surakarta", "Surabarya", "Medan", "Makasar")

population = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)

#Membuat Char Bar 
plt.bar(x=cities, height=population)
#Memberi jarak pada setiap nama kota, agar tidak bertabrakan satu dengan yang lain
plt.xticks(rotation=45)
plt.show()

#Bisa juga menggunakan parameter y dan width dar chart yang ingin dibuat
#plt.barh(y=cities, width=population)

#Mengurutkan nilainya berdasarkan jumlah populasi terbanyak
import pandas as pd

df = pd.DataFrame({
    "Cities" : cities,
    "Population" : population,
})

df.sort_values(by="Population", inplace=True)

plt.barh(y=df["Cities"], width=df["Population"])
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
plt.show()


#membuat BarChart menggunakan seaborn
import seaborn as sns

sns.barplot(y=df["Cities"], x=df["Population"], orient="h", color="green")
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
plt.show()