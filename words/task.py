country = "Azərbaycan"
region = "Cənubi Qafqaz"
neighbor_1 = "Rusiya"
neighbor_2 = "Türkiyə"
km_south = 765
km_west = 1007

print(f"{country} və ya rəsmi adı ilə Azərbaycan Respublikası — Şərqi Avropa və Qərbi Asiyanın sərhəddində yerləşən transkontinental ölkə. {country} Xəzər dənizi hövzəsinin qərbində, {region}da yerləşir. Şimaldan {neighbor_1} (Dağıstan), qərbdən {neighbor_2} ilə həmsərhəddir. Dövlət sərhədləri cənubdan İranla {km_south} km, qərbdən {neighbor_1} ilə {km_west} km həmsərhəddir.")
print("{} və ya rəsmi adı ilə Azərbaycan Respublikası — Şərqi Avropa və Qərbi Asiyanın sərhəddində yerləşən transkontinental ölkə. {} Xəzər dənizi hövzəsinin qərbində, {}da yerləşir. Şimaldan {} (Dağıstan), qərbdən {} ilə həmsərhəddir. Dövlət sərhədləri cənubdan İranla {} km, qərbdən {} ilə {} km həmsərhəddir.".format(country, country, region, neighbor_1, neighbor_2, km_south, neighbor_1, km_west, neighbor_2))
print("%s və ya rəsmi adı ilə Azərbaycan Respublikası — Şərqi Avropa və Qərbi Asiyanın sərhəddində yerləşən transkontinental ölkə. %s Xəzər dənizi hövzəsinin qərbində, %sda yerləşir. Şimaldan %s (Dağıstan), qərbdən %s ilə həmsərhəddir. Dövlət sərhədləri cənubdan İranla %d km, qərbdən %s ilə %d km həmsərhəddir." % (country, country, region, neighbor_1, neighbor_2, km_south, neighbor_1, km_west, neighbor_2))
