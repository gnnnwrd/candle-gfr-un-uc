import openmc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##################################################### LEGENDRE ##########################################################
H = 370
D = 252.41 + 2*67.31 
zmin, zmax, radius = -H/2., H/2, D/2
id= [0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	
11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	
21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	
31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	
41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	
51,	52,	53,	54,	55,	56,	57,	58,	59,	60,] #per tahun dari 10 tahun
#id = [0,1,2,3,4,5,6,7,8,9,10,11,12] #328.5 hari
#id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] #500 hari
axial = []
fission_legendre = []
for i in id :
    sp = openmc.StatePoint('openmc_simulation_n'+ str(i) + '.h5')
    legendre_fission = sp.get_tally(name = 'fission legendre').get_pandas_dataframe()
    legendre_fission_mean = legendre_fission['mean']
    legendre_exponential = openmc.legendre_from_expcoef(legendre_fission_mean, domain=(zmin,zmax))
    z = np.linspace(zmin,zmax, 100)
    fission_legendre_z = legendre_exponential(z)
    fission_legendre.append(fission_legendre_z)
    axial.append(z)
'''
import openpyxl
axial_data =  pd.DataFrame(list(map(np.ravel, axial)))

fission_legendre_data =  pd.DataFrame(list(map(np.ravel, fission_legendre)))
fission_legendre_data.append(axial_data[0])
fission_legendre_data.to_excel('data distribusi fluks legendre.xlsx')
'''

fig, ax = plt.subplots()
for i in range (61):
#for i in range (13):
#for i in range (15):
    label = "tahun ke-"+str(i)
    x = fission_legendre[i]
    y = axial[i]
    ax.plot(x,y, label =label)
    ax.set_xlabel('fission [neutron/source]')
    ax.set_ylabel('Core Height Position [cm]')
ax.legend(loc='upper right', #bbox_to_anchor=(1.31, 1),
          fancybox=True, shadow=True, ncol=1)
plt.title('Distribusi Fluks Aksial (Legendre) Teras SFR 1000 MWth', y = 1.08)
plt.savefig('Distribusi Fluks Aksial Legendre.jpg',dpi = 1000, bbox_inches = 'tight')
fig.show()

##################################################### ZERNIKE RADIAL ##########################################################
radial = []
fission_zernikerad = []
for i in id:
    sp = openmc.StatePoint('openmc_simulation_n'+str(i)+'.h5')
    zernikerad_fission = sp.get_tally(name = 'fission zernike radial').get_pandas_dataframe()
    zernikerad_fission_mean = zernikerad_fission['mean']
    zernikerad_exponential = openmc.ZernikeRadial(zernikerad_fission_mean, radius=radius)
    r = np.linspace(-radius, radius, 100)
    fission_zernikerad_r = zernikerad_exponential(r)
    fission_zernikerad.append(fission_zernikerad_r)
    radial.append(r)
'''
import openpyxl
radial_data =  pd.DataFrame(list(map(np.ravel, radial)))

fission_zernikerad_data =  pd.DataFrame(list(map(np.ravel, fission_zernikerad)))
fission_zernikerad_data.append(radial_data[0])
fission_zernikerad_data.to_excel('data distribusi fluks zernikerad.xlsx')
'''

fig, ax = plt.subplots()
for i in range (11):
#for i in range (13):
#for i in range (15):
    label = "tahun ke-"+str(i)
    y = fission_zernikerad[i]
    x = radial[i]
    ax.plot(x,y, label =label)
    ax.set_ylabel('fission [neutron/source]')
    ax.set_xlabel('Core Diamater Position [cm]')
ax.legend(loc='upper right', #bbox_to_anchor=(1.31, 1),
          fancybox=True, shadow=True, ncol=1)
plt.title('Distribusi Fluks Aksial (zernikerad) Teras SFR 1000 MWth', y = 1.08)
plt.savefig('Distribusi Fluks Aksial zernikerad.jpg',dpi = 1000, bbox_inches = 'tight')
fig.show()
##################################################### AKSIAL RADIAL ##########################################################


for i in range (11):
#for i in range (13):
#for i in range (15):
	fig = plt.figure()
    	sp = openmc.StatePoint('openmc_simulation_n'+str(i)+'.h5')
    	legendre_fission = sp.get_tally(name = 'fission legendre').get_pandas_dataframe()
    	legendre_fission_mean = legendre_fission['mean']
    	legendre_exponential = openmc.legendre_from_expcoef(legendre_fission_mean, domain=(zmin, zmax))
    	z = np.linspace(zmin,zmax, 100)
    	zernikerad_fission = sp.get_tally(name = 'fission zernike radial').get_pandas_dataframe()
    	zernikerad_fission_mean = zernikerad_fission['mean']
    	zernikerad_exponential = openmc.ZernikeRadial(zernikerad_fission_mean, radius=radius)
    	r = np.linspace(-radius, radius, 100)
    	fission_zernikerad_r = zernikerad_exponential(r)
    	fission = np.array([legendre_exponential(z)]).T  @ np.array([zernikerad_exponential(r)])
    	plt.title('fission distribution '+str(i)+' years')
    	plt.xlabel('Radial Position [cm]')
    	plt.ylabel('Axial Height [cm]')
    	plt.pcolor(r, z, fission, cmap='jet')
    	plt.colorbar()
    	plt.savefig('Distribusi Fluks Aksial Radial tahun ke '+str(i)+'tahun.jpg',dpi = 1000, bbox_inches = 'tight')
    	fig.show()

