import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openmc.deplete
import openmc

results = openmc.deplete.ResultsList.from_hdf5('./depletion_results.h5')

time, k = results.get_eigenvalue() 

kdata =  pd.DataFrame(k)
kdata.to_excel('Data keff.xlsx') #data keff per step
'''
k = np.delete(k,[1,2,3,4,5,6,7,8,9,10,11,12],0) #data keff per tahun
time = np.delete(time,[1,2,3,4,5,6,7,8,9,10,11,12],0) #waktu per tahun
time = time/(60*60*24*365)



fig = plt.figure()
plt.errorbar(time, k[:, 0], yerr=k[:, 1], label = Keff)
plt.title('Grafik nilai K-eff vs waktu burn up', y = 1.08)
plt.xlabel("Time [years]")
plt.ylabel("$k_{eff}\pm \sigma$")
plt.title('Faktor Multiplikasi Efektif', y = 1.08)
plt.legend()
plt.savefig('Keff.jpg',dpi = 1000, bbox_inches = 'tight')
fig.show()
'''
