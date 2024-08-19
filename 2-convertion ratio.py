import numpy as np
import matplotlib.pyplot as plt
import openmc.deplete
import openmc
import pandas as pd
results = openmc.deplete.ResultsList.from_hdf5('./depletion_results.h5')

time = []
for i in range (1,161):
	time_variable = 'time'+str(i)
	time.append(time_variable)
ax_fis_1 = []
for i in range(1,161):
	ax_fis_1_variable = 'moxf1_'+str(i)
	ax_fis_1.append(ax_fis_1_variable)
ax_fis_2 = []
for i in range(1,161):
	ax_fis_2_variable = 'moxf2_'+str(i)
	ax_fis_2.append(ax_fis_2_variable)
	
ax_fis_3 = []
for i in range(1,161):
	ax_fis_3_variable = 'moxf3_'+str(i)
	ax_fis_3.append(ax_fis_3_variable)
	
ax_fis_4 = []
for i in range(1,161):
	ax_fis_4_variable = 'moxf4_'+str(i)
	ax_fis_4.append(ax_fis_4_variable)
	
ax_fis_5 = []
for i in range(1,161):
	ax_fis_5_variable = 'moxf5_'+str(i)
	ax_fis_5.append(ax_fis_5_variable)
	
ax_fis_6 = []
for i in range(1,161):
	ax_fis_6_variable = 'moxf6_'+str(i)
	ax_fis_6.append(ax_fis_6_variable)
	
ax_fis_7 = []
for i in range(1,161):
	ax_fis_7_variable = 'moxf7_'+str(i)
	ax_fis_7.append(ax_fis_7_variable)

ax_capture_1 = []
for i in range(1,161):
	ax_capture_1_variable = 'moxc1_'+str(i)
	ax_capture_1.append(ax_capture_1_variable)
	
ax_capture_2 = []
for i in range(1,161):
	ax_capture_2_variable = 'moxc2_'+str(i)
	ax_capture_2.append(ax_capture_2_variable)
	
ax_capture_3 = []
for i in range(1,161):
	ax_capture_3_variable = 'moxc3_'+str(i)
	ax_capture_3.append(ax_capture_3_variable)
	
ax_capture_4 = []
for i in range(1,161):
	ax_capture_4_variable = 'moxc4_'+str(i)
	ax_capture_4.append(ax_capture_4_variable)
	
ax_capture_5 = []
for i in range(1,161):
	ax_capture_5_variable = 'moxc5_'+str(i)
	ax_capture_5.append(ax_capture_5_variable)
	
ax_capture_6 = []
for i in range(1,161):
	ax_capture_6_variable = 'moxc6_'+str(i)
	ax_capture_6.append(ax_capture_6_variable)
	
ax_capture_7 = []
for i in range(1,161):
	ax_capture_7_variable = 'moxc7_'+str(i)
	ax_capture_7.append(ax_capture_7_variable)
material_id = []
for i in range(1,161):
    id = str(i)
    material_id.append(id)
sum_ax_fis_1 = 0
sum_ax_fis_2 = 0
sum_ax_fis_3 = 0
sum_ax_fis_4 = 0
sum_ax_fis_5 = 0
sum_ax_fis_6 = 0
sum_ax_fis_7 = 0

sum_ax_capture_1 = 0
sum_ax_capture_2 = 0
sum_ax_capture_3 = 0
sum_ax_capture_4 = 0
sum_ax_capture_5 = 0
sum_ax_capture_6 = 0
sum_ax_capture_7 = 0
	
for i,j in zip(range(160),range(1,161)):
	time[i],ax_fis_1[i] = results.get_reaction_rate(str(j), 'Th232', 'fission')
	time[i],ax_fis_2[i] = results.get_reaction_rate(str(j), 'U233', 'fission')
	time[i],ax_fis_3[i] = results.get_reaction_rate(str(j), 'U235', 'fission')
	time[i],ax_fis_4[i] = results.get_reaction_rate(str(j), 'U238', 'fission')
	time[i],ax_fis_5[i] = results.get_reaction_rate(str(j), 'Pu239', 'fission')
	time[i],ax_fis_6[i] = results.get_reaction_rate(str(j), 'Pu240', 'fission')
	time[i],ax_fis_7[i] = results.get_reaction_rate(str(j), 'Pu241', 'fission')
	
	time[i],ax_capture_1[i] = results.get_reaction_rate(str(j), 'Th232', '(n,gamma)')
	time[i],ax_capture_2[i] = results.get_reaction_rate(str(j), 'U233', '(n,gamma)')
	time[i],ax_capture_3[i] = results.get_reaction_rate(str(j), 'U235', '(n,gamma)')
	time[i],ax_capture_4[i] = results.get_reaction_rate(str(j), 'U238', '(n,gamma)')
	time[i],ax_capture_5[i] = results.get_reaction_rate(str(j), 'Pu239', '(n,gamma)')
	time[i],ax_capture_6[i] = results.get_reaction_rate(str(j), 'Pu240', '(n,gamma)')
	time[i],ax_capture_7[i] = results.get_reaction_rate(str(j), 'Pu241', '(n,gamma)')
	
	sum_fis1 = sum_ax_fis_1 + ax_fis_1[i]
	sum_fis2 = sum_ax_fis_2 + ax_fis_2[i]
	sum_fis3 = sum_ax_fis_3 + ax_fis_3[i]
	sum_fis4 = sum_ax_fis_4 + ax_fis_4[i]
	sum_fis5 = sum_ax_fis_5 + ax_fis_5[i]
	sum_fis6 = sum_ax_fis_6 + ax_fis_6[i]
	sum_fis7 = sum_ax_fis_7 + ax_fis_7[i]
	
	sum_capture1 = sum_ax_capture_1 + ax_capture_1[i]
	sum_capture2 = sum_ax_capture_2 + ax_capture_2[i]
	sum_capture3 = sum_ax_capture_3 + ax_capture_3[i]
	sum_capture4 = sum_ax_capture_4 + ax_capture_4[i]
	sum_capture5 = sum_ax_capture_5 + ax_capture_5[i]
	sum_capture6 = sum_ax_capture_6 + ax_capture_6[i]
	sum_capture7 = sum_ax_capture_7 + ax_capture_7[i]
	
## capture
Th232_capture = sum_capture1
U233_capture = sum_capture2
U235_capture = sum_capture3
U238_capture = sum_capture4
Pu239_capture = sum_capture5
Pu240_capture = sum_capture6
Pu241_capture = sum_capture7

## absorption
Th232_absorption = Th232_capture + sum_fis1
U233_absorption = U233_capture + sum_fis2
U235_absorption = U235_capture + sum_fis3
U238_absorption = U238_capture + sum_fis4
Pu239_absorption = Pu239_capture + sum_fis5
Pu240_absorption = Pu240_capture + sum_fis6
Pu241_absorption = Pu241_capture + sum_fis7

CR = (Th232_capture + U238_capture + Pu240_capture) / ( U233_absorption + U235_absorption  + Pu239_absorption  + Pu241_absorption)
time_k, k = results.get_eigenvalue()
time_k = time_k/(60*60*24*30*12)
CR_file = pd.DataFrame(CR)
CR_file.to_excel('CR_file.xlsx')
'''
k = np.delete(k,[1,2,3,4,5,6,7,8,9,10,11,12],0) #data keff per tahun
time_k = np.delete(time_k,[1,2,3,4,5,6,7,8,9,10,11,12],0) #waktu per tahun
time_k = time/(60*60*24*365)



fig = plt.figure()
plt.plot(time_k,CR,label='CR')
plt.xlabel('time_k (years)')
plt.ylabel('Convertion Ratio')
plt.title('Convertion Ratio', y = 1.08)
plt.legend()
plt.savefig('Convertion Ratio.jpg',dpi = 1000, bbox_inches = 'tight')
fig.show()
'''
