#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openmc
import numpy as np
import openpyxl
import pandas as pd


# In[2]:


#membuat variabel material bahan bakar
fuel = []
for i in range(1,161):
    fuel_index = 'fuel'+str(i)
    fuel.append(fuel_index)
    
mat_id = []
for i in range (1,161):
    mat_id.append(i)
    
    
for i in range (0,128):
	fuel[i] = openmc.Material(material_id = mat_id[i])
	fuel[i] .temperature = 1200
	fuel[i] .set_density( 'g/cm3' , 14.310000 )
	fuel[i] .add_element( 'N' , 0.05559 , 'wo' )
	fuel[i] .add_nuclide( 'U234' , 0.000251987906941, 'wo' )
	fuel[i] .add_nuclide( 'U235' , 0.1227733 , 'wo' )
	fuel[i] .add_nuclide( 'U236' ,0.000129962266965 , 'wo' )
	fuel[i] .add_nuclide( 'U238' , 0.821254749826094, 'wo' )

for i in range (128,144):
	fuel[i] = openmc.Material(material_id = mat_id[i])
	fuel[i] .temperature = 1200
	fuel[i].set_density( 'g/cm3' , 14.310000 )
	fuel[i].add_element( 'N' , 0.05559 , 'wo' )
	fuel[i].add_nuclide( 'U234' , 0.000251987906941, 'wo' )
	fuel[i].add_nuclide( 'U235' , 0.0849969 , 'wo' )
	fuel[i].add_nuclide( 'U236' , 0.000129962266965 , 'wo' )
	fuel[i].add_nuclide( 'U238' , 0.859031149826094 , 'wo' )
	
for i in range (144,160):
	fuel[i] = openmc.Material(material_id = mat_id[i])
	fuel[i] .temperature = 1200
	fuel[i].set_density( 'g/cm3' , 14.310000 )
	fuel[i].add_element( 'N' , 0.05559 , 'wo' )
	fuel[i].add_nuclide( 'U234' , 0.000251987906941 , 'wo' )
	fuel[i].add_nuclide( 'U235' , 0.0661087, 'wo' )
	fuel[i].add_nuclide( 'U236' , 0.000129962266965 , 'wo' )
	fuel[i].add_nuclide( 'U238' , 0.877919349826094 , 'wo' )



# In[3]:


####### Membuat index depleted Uranium
depU = []
for i in range (161,401):
	    dep_index = 'depU'+str(i)
	    depU.append(dep_index)

dep_id = []
for i in range(161,401):
	dep_id.append(i)
	   
for i in range (0,240):
	depU[i] =openmc.Material(material_id = dep_id[i], name = depU[i] )
	depU[i] .temperature = 1200
	depU[i].set_density( 'g/cm3' , 18.951157 )
	depU[i].add_nuclide( 'U234' , 0.000005 , 'wo' )
	depU[i].add_nuclide( 'U235' , 0.002500 , 'wo' )
	depU[i].add_nuclide( 'U238' , 0.997495 , 'wo' )


# In[4]:



coolant=openmc.Material(401,name = 'coolant')
coolant.set_density( 'g/cm3' , 0.0037000 )
coolant.add_element( 'He' , 1, 'wo' )


clad = openmc.Material( 402 , name = 'Stainless Steel 316' )
clad.set_density( 'g/cm3' , 8.000000)
clad.add_element( 'C' , 0.000410 , 'wo' )
clad.add_element( 'Si' , 0.005070 , 'wo' )
clad.add_element( 'P' , 0.000230 , 'wo' )
clad.add_element( 'S' , 0.000150 , 'wo' )
clad.add_element( 'Cr' , 0.170000 , 'wo' )
clad.add_element( 'Mn' , 0.010140 , 'wo' )
clad.add_element( 'Fe' , 0.669000 , 'wo' )
clad.add_element( 'Ni' , 0.120000 , 'wo' )
clad.add_element( 'Mo' , 0.025000 , 'wo' )
    
gap=openmc.Material(403,name = 'gap')
gap.set_density( 'g/cm3' , 0.0006223)
gap.add_element( 'He' , 1, 'wo' )  
    
Reflector = openmc.Material( 404 , name = 'Berilium Oksida')
Reflector.set_density( 'g/cm3' , 3.010000 )
Reflector.add_element( 'Be' , 0.360320 , 'wo' )
Reflector.add_element( 'O' , 0.639680 , 'wo' )


# In[5]:


mat_file = openmc.Materials([gap,clad, Reflector,coolant, depU[0] ,   depU[1] ,   depU[2] ,   depU[3] ,   depU[4] ,   depU[5] ,   depU[6] ,   depU[7] ,   depU[8] ,   depU[9] ,   depU[10] ,   
                             depU[11] ,   depU[12] ,   depU[13] ,   depU[14] ,   depU[15] ,   depU[16] ,   depU[17] ,   depU[18] ,   depU[19] ,   depU[20] ,   depU[21] ,   depU[22] ,   
                             depU[23] ,   depU[24] ,   depU[25] ,   depU[26] ,   depU[27] ,   depU[28] ,   depU[29] ,   depU[30] ,   depU[31] ,   depU[32] ,   depU[33] ,   depU[34] ,   
                             depU[35] ,   depU[36] ,   depU[37] ,   depU[38] ,   depU[39] ,   depU[40] ,   depU[41] ,   depU[42] ,   depU[43] ,   depU[44] ,   depU[45] ,   depU[46] ,   
                             depU[47] ,   depU[48] ,   depU[49] ,   depU[50] ,   depU[51] ,   depU[52] ,   depU[53] ,   depU[54] ,   depU[55] ,   depU[56] ,   depU[57] ,   depU[58] ,   
                             depU[59] ,   depU[60] ,   depU[61] ,   depU[62] ,   depU[63] ,   depU[64] ,   depU[65] ,   depU[66] ,   depU[67] ,   depU[68] ,   depU[69] ,   depU[70] ,   
                             depU[71] ,   depU[72] ,   depU[73] ,   depU[74] ,   depU[75] ,   depU[76] ,   depU[77] ,   depU[78] ,   depU[79] ,   depU[80] ,   depU[81] ,   depU[82] ,   
                             depU[83] ,   depU[84] ,   depU[85] ,   depU[86] ,   depU[87] ,   depU[88] ,   depU[89] ,   depU[90] ,   depU[91] ,   depU[92] ,   depU[93] ,   depU[94] ,   
                             depU[95] ,   depU[96] ,   depU[97] ,   depU[98] ,   depU[99] ,   depU[100] ,   depU[101] ,   depU[102] ,   depU[103] ,   depU[104] ,   depU[105] ,   depU[106] ,   
                             depU[107] ,   depU[108] ,   depU[109] ,   depU[110] ,   depU[111] ,   depU[112] ,   depU[113] ,   depU[114] ,   depU[115] ,   depU[116] ,   depU[117] ,   depU[118] ,   
                             depU[119] ,   depU[120] ,   depU[121] ,   depU[122] ,   depU[123] ,   depU[124] ,   depU[125] ,   depU[126] ,   depU[127] ,   depU[128] ,   depU[129] ,   depU[130] ,   
                             depU[131] ,   depU[132] ,   depU[133] ,   depU[134] ,   depU[135] ,   depU[136] ,   depU[137] ,   depU[138] ,   depU[139] ,   depU[140] ,   depU[141] ,   depU[142] ,   
                             depU[143] ,   depU[144] ,   depU[145] ,   depU[146] ,   depU[147] ,   depU[148] ,   depU[149] ,   depU[150] ,   depU[151] ,   depU[152] ,   depU[153] ,   depU[154] ,   
                             depU[155] ,   depU[156] ,   depU[157] ,   depU[158] ,   depU[159] ,   depU[160] ,   depU[161] ,   depU[162] ,   depU[163] ,   depU[164] ,   depU[165] ,   depU[166] ,   
                             depU[167] ,   depU[168] ,   depU[169] ,   depU[170] ,   depU[171] ,   depU[172] ,   depU[173] ,   depU[174] ,   depU[175] ,   depU[176] ,   depU[177] ,   depU[178] ,   
                             depU[179] ,   depU[180] ,   depU[181] ,   depU[182] ,   depU[183] ,   depU[184] ,   depU[185] ,   depU[186] ,   depU[187] ,   depU[188] ,   depU[189] ,   depU[190] ,   
                             depU[191] ,   depU[192] ,   depU[193] ,   depU[194] ,   depU[195] ,   depU[196] ,   depU[197] ,   depU[198] ,   depU[199] ,   depU[200] ,   depU[201] ,   depU[202] ,   
                             depU[203] ,   depU[204] ,   depU[205] ,   depU[206] ,   depU[207] ,   depU[208] ,   depU[209] ,   depU[210] ,   depU[211] ,   depU[212] ,   depU[213] ,   depU[214] ,   
                             depU[215] ,   depU[216] ,   depU[217] ,   depU[218] ,   depU[219] ,   depU[220] ,   depU[221] ,   depU[222] ,   depU[223] ,   depU[224] ,   depU[225] ,   depU[226] ,   
                             depU[227] ,   depU[228] ,   depU[229] ,   depU[230] ,   depU[231] ,   depU[232] ,   depU[233] ,   depU[234] ,   depU[235] ,   depU[236] ,   depU[237] ,   depU[238] ,   
                             depU[239] , fuel[0] ,   fuel[1] ,   fuel[2] ,   fuel[3] ,   fuel[4] ,   fuel[5] ,   fuel[6] ,   fuel[7] ,   fuel[8] ,   fuel[9] ,   fuel[10] ,   fuel[11] ,   fuel[12] ,   
                             fuel[13] ,   fuel[14] ,   fuel[15] ,   fuel[16] ,   fuel[17] ,   fuel[18] ,   fuel[19] ,   fuel[20] ,   fuel[21] ,   fuel[22] ,   fuel[23] ,   fuel[24] ,   fuel[25] ,  
                             fuel[26] ,   fuel[27] ,   fuel[28] ,   fuel[29] ,   fuel[30] ,   fuel[31] ,   fuel[32] ,   fuel[33] ,   fuel[34] ,   fuel[35] ,   fuel[36] ,   fuel[37] ,   fuel[38] ,   
                             fuel[39] ,   fuel[40] ,   fuel[41] ,   fuel[42] ,   fuel[43] ,   fuel[44] ,   fuel[45] ,   fuel[46] ,   fuel[47] ,   fuel[48] ,   fuel[49] ,   fuel[50] ,   fuel[51] ,  
                             fuel[52] ,   fuel[53] ,   fuel[54] ,   fuel[55] ,   fuel[56] ,   fuel[57] ,   fuel[58] ,   fuel[59] ,   fuel[60] ,   fuel[61] ,   fuel[62] ,   fuel[63] ,   fuel[64] ,  
                             fuel[65] ,   fuel[66] ,   fuel[67] ,   fuel[68] ,   fuel[69] ,   fuel[70] ,   fuel[71] ,   fuel[72] ,   fuel[73] ,   fuel[74] ,   fuel[75] ,   fuel[76] ,   fuel[77] ,   
                             fuel[78] ,   fuel[79] ,   fuel[80] ,   fuel[81] ,   fuel[82] ,   fuel[83] ,   fuel[84] ,   fuel[85] ,   fuel[86] ,   fuel[87] ,   fuel[88] ,   fuel[89] ,   fuel[90] ,   
                             fuel[91] ,   fuel[92] ,   fuel[93] ,   fuel[94] ,   fuel[95] ,   fuel[96] ,   fuel[97] ,   fuel[98] ,   fuel[99] ,   fuel[100] ,   fuel[101] ,   fuel[102] ,   fuel[103] ,  
                             fuel[104] ,   fuel[105] ,   fuel[106] ,   fuel[107] ,   fuel[108] ,   fuel[109] ,   fuel[110] ,   fuel[111] ,   fuel[112] ,   fuel[113] ,   fuel[114] ,   fuel[115] ,   fuel[116] ,   
                             fuel[117] ,   fuel[118] ,   fuel[119] ,   fuel[120] ,   fuel[121] ,   fuel[122] ,   fuel[123] ,   fuel[124] ,   fuel[125] ,   fuel[126] ,   fuel[127] ,   fuel[128] ,   fuel[129] ,   
                             fuel[130] ,   fuel[131] ,   fuel[132] ,   fuel[133] ,   fuel[134] ,   fuel[135] ,   fuel[136] ,   fuel[137] ,   fuel[138] ,   fuel[139] ,   fuel[140] ,   fuel[141] ,   fuel[142] ,   
                             fuel[143] ,   fuel[144] ,   fuel[145] ,   fuel[146] ,   fuel[147] ,   fuel[148] ,   fuel[149] ,   fuel[150] ,   
                             fuel[151] ,   fuel[152] ,   fuel[153] ,   fuel[154] ,   fuel[155] ,   fuel[156] ,   fuel[157] ,   fuel[158] ,   fuel[159] ])
mat_file.export_to_xml()


# In[6]:


up = openmc.ZPlane(z0=220)
low = openmc.ZPlane(z0=-220)
up2 = openmc.ZPlane(z0=240, boundary_type = 'vacuum')
low2 = openmc.ZPlane(z0=-240, boundary_type = 'vacuum')
inner = openmc.ZCylinder(r=200) #, boundary_type = 'vacuum'
outer = openmc.ZCylinder(r=220, boundary_type = 'vacuum')


# In[7]:


#universe
root = openmc.Universe(0,name = 'root_universe')

univ = []
univ_id = []
for i in range (1,401):
    univ.append('univ'+str(i))
    univ_id.append(i)
    
for i in range (0,400):
    univ[i] = openmc.Universe(universe_id =univ_id[i])


# In[8]:


univ401 = openmc.Universe(universe_id = 401)
univ402 = openmc.Universe(universe_id = 402)
univ403 = openmc.Universe(universe_id = 403)

rfuel = 0.525
rgap = 0.528
rpin = 0.578
# pin fuel 1
geom_fuel1 = openmc.ZCylinder (x0=0, y0=0,  r=rfuel)
geom_gap1 = openmc.ZCylinder (x0=0, y0=0,  r=rgap)
geom_clad1 = openmc.ZCylinder (x0=0, y0=0,  r=rpin )

# pin reflector
geom_ref1 = openmc.ZCylinder (x0=0, y0=0,  r=rgap)
geom_cladref1 = openmc.ZCylinder (x0=0, y0=0,  r=rpin)


# In[9]:


pinfuel = []
pingap = []
pinclad = []
pincool = []
hexa =[]
hexac = []
for i in range (1,401):
    pinfuel_index = 'pinfuel'+str(i)
    pinfuel.append(pinfuel_index)
    pingap_index = 'pingap'+str(i)
    pingap.append(pingap_index)
    pinhexa_index = 'pinhexa'+str(i)
    hexa.append(pinhexa_index)
    pinhexac_index = 'pinhexac'+str(i)
    hexac.append(pinhexac_index)
    pinclad.append('pinclad'+str(i))
    pincool.append('pincool'+str(i))


# In[10]:


fuel0=fuel[0]
fuel1=fuel[1]
fuel2=fuel[2]
fuel3=fuel[3]
fuel4=fuel[4]
fuel5=fuel[5]
fuel6=fuel[6]
fuel7=fuel[7]
fuel8=fuel[8]
fuel9=fuel[9]
fuel10=fuel[10]
fuel11=fuel[11]
fuel12=fuel[12]
fuel13=fuel[13]
fuel14=fuel[14]
fuel15=fuel[15]
fuel16=fuel[16]
fuel17=fuel[17]
fuel18=fuel[18]
fuel19=fuel[19]
fuel20=fuel[20]
fuel21=fuel[21]
fuel22=fuel[22]
fuel23=fuel[23]
fuel24=fuel[24]
fuel25=fuel[25]
fuel26=fuel[26]
fuel27=fuel[27]
fuel28=fuel[28]
fuel29=fuel[29]
fuel30=fuel[30]
fuel31=fuel[31]
fuel32=fuel[32]
fuel33=fuel[33]
fuel34=fuel[34]
fuel35=fuel[35]
fuel36=fuel[36]
fuel37=fuel[37]
fuel38=fuel[38]
fuel39=fuel[39]
fuel40=fuel[40]
fuel41=fuel[41]
fuel42=fuel[42]
fuel43=fuel[43]
fuel44=fuel[44]
fuel45=fuel[45]
fuel46=fuel[46]
fuel47=fuel[47]
fuel48=fuel[48]
fuel49=fuel[49]
fuel50=fuel[50]
fuel51=fuel[51]
fuel52=fuel[52]
fuel53=fuel[53]
fuel54=fuel[54]
fuel55=fuel[55]
fuel56=fuel[56]
fuel57=fuel[57]
fuel58=fuel[58]
fuel59=fuel[59]
fuel60=fuel[60]
fuel61=fuel[61]
fuel62=fuel[62]
fuel63=fuel[63]
fuel64=fuel[64]
fuel65=fuel[65]
fuel66=fuel[66]
fuel67=fuel[67]
fuel68=fuel[68]
fuel69=fuel[69]
fuel70=fuel[70]
fuel71=fuel[71]
fuel72=fuel[72]
fuel73=fuel[73]
fuel74=fuel[74]
fuel75=fuel[75]
fuel76=fuel[76]
fuel77=fuel[77]
fuel78=fuel[78]
fuel79=fuel[79]
fuel80=fuel[80]
fuel81=fuel[81]
fuel82=fuel[82]
fuel83=fuel[83]
fuel84=fuel[84]
fuel85=fuel[85]
fuel86=fuel[86]
fuel87=fuel[87]
fuel88=fuel[88]
fuel89=fuel[89]
fuel90=fuel[90]
fuel91=fuel[91]
fuel92=fuel[92]
fuel93=fuel[93]
fuel94=fuel[94]
fuel95=fuel[95]
fuel96=fuel[96]
fuel97=fuel[97]
fuel98=fuel[98]
fuel99=fuel[99]
fuel100=fuel[100]
fuel101=fuel[101]
fuel102=fuel[102]
fuel103=fuel[103]
fuel104=fuel[104]
fuel105=fuel[105]
fuel106=fuel[106]
fuel107=fuel[107]
fuel108=fuel[108]
fuel109=fuel[109]
fuel110=fuel[110]
fuel111=fuel[111]
fuel112=fuel[112]
fuel113=fuel[113]
fuel114=fuel[114]
fuel115=fuel[115]
fuel116=fuel[116]
fuel117=fuel[117]
fuel118=fuel[118]
fuel119=fuel[119]
fuel120=fuel[120]
fuel121=fuel[121]
fuel122=fuel[122]
fuel123=fuel[123]
fuel124=fuel[124]
fuel125=fuel[125]
fuel126=fuel[126]
fuel127=fuel[127]

fuel128=fuel[128]
fuel129=fuel[129]
fuel130=fuel[130]
fuel131=fuel[131]
fuel132=fuel[132]
fuel133=fuel[133]
fuel134=fuel[134]
fuel135=fuel[135]
fuel136=fuel[136]
fuel137=fuel[137]
fuel138=fuel[138]
fuel139=fuel[139]
fuel140=fuel[140]
fuel141=fuel[141]
fuel142=fuel[142]
fuel143=fuel[143]

fuel144=fuel[144]
fuel145=fuel[145]
fuel146=fuel[146]
fuel147=fuel[147]
fuel148=fuel[148]
fuel149=fuel[149]
fuel150=fuel[150]
fuel151=fuel[151]
fuel152=fuel[152]
fuel153=fuel[153]
fuel154=fuel[154]
fuel155=fuel[155]
fuel156=fuel[156]
fuel157=fuel[157]
fuel158=fuel[158]
fuel159=fuel[159]


# In[11]:


fuel160=depU[0]
fuel161=depU[1]
fuel162=depU[2]
fuel163=depU[3]
fuel164=depU[4]
fuel165=depU[5]
fuel166=depU[6]
fuel167=depU[7]
fuel168=depU[8]
fuel169=depU[9]
fuel170=depU[10]
fuel171=depU[11]
fuel172=depU[12]
fuel173=depU[13]
fuel174=depU[14]
fuel175=depU[15]
fuel176=depU[16]
fuel177=depU[17]
fuel178=depU[18]
fuel179=depU[19]
fuel180=depU[20]
fuel181=depU[21]
fuel182=depU[22]
fuel183=depU[23]
fuel184=depU[24]
fuel185=depU[25]
fuel186=depU[26]
fuel187=depU[27]
fuel188=depU[28]
fuel189=depU[29]
fuel190=depU[30]
fuel191=depU[31]
fuel192=depU[32]
fuel193=depU[33]
fuel194=depU[34]
fuel195=depU[35]
fuel196=depU[36]
fuel197=depU[37]
fuel198=depU[38]
fuel199=depU[39]
fuel200=depU[40]
fuel201=depU[41]
fuel202=depU[42]
fuel203=depU[43]
fuel204=depU[44]
fuel205=depU[45]
fuel206=depU[46]
fuel207=depU[47]
fuel208=depU[48]
fuel209=depU[49]
fuel210=depU[50]
fuel211=depU[51]
fuel212=depU[52]
fuel213=depU[53]
fuel214=depU[54]
fuel215=depU[55]
fuel216=depU[56]
fuel217=depU[57]
fuel218=depU[58]
fuel219=depU[59]
fuel220=depU[60]
fuel221=depU[61]
fuel222=depU[62]
fuel223=depU[63]
fuel224=depU[64]
fuel225=depU[65]
fuel226=depU[66]
fuel227=depU[67]
fuel228=depU[68]
fuel229=depU[69]
fuel230=depU[70]
fuel231=depU[71]
fuel232=depU[72]
fuel233=depU[73]
fuel234=depU[74]
fuel235=depU[75]
fuel236=depU[76]
fuel237=depU[77]
fuel238=depU[78]
fuel239=depU[79]
fuel240=depU[80]
fuel241=depU[81]
fuel242=depU[82]
fuel243=depU[83]
fuel244=depU[84]
fuel245=depU[85]
fuel246=depU[86]
fuel247=depU[87]
fuel248=depU[88]
fuel249=depU[89]
fuel250=depU[90]
fuel251=depU[91]
fuel252=depU[92]
fuel253=depU[93]
fuel254=depU[94]
fuel255=depU[95]
fuel256=depU[96]
fuel257=depU[97]
fuel258=depU[98]
fuel259=depU[99]
fuel260=depU[100]
fuel261=depU[101]
fuel262=depU[102]
fuel263=depU[103]
fuel264=depU[104]
fuel265=depU[105]
fuel266=depU[106]
fuel267=depU[107]
fuel268=depU[108]
fuel269=depU[109]
fuel270=depU[110]
fuel271=depU[111]
fuel272=depU[112]
fuel273=depU[113]
fuel274=depU[114]
fuel275=depU[115]
fuel276=depU[116]
fuel277=depU[117]
fuel278=depU[118]
fuel279=depU[119]
fuel280=depU[120]
fuel281=depU[121]
fuel282=depU[122]
fuel283=depU[123]
fuel284=depU[124]
fuel285=depU[125]
fuel286=depU[126]
fuel287=depU[127]
fuel288=depU[128]
fuel289=depU[129]
fuel290=depU[130]
fuel291=depU[131]
fuel292=depU[132]
fuel293=depU[133]
fuel294=depU[134]
fuel295=depU[135]
fuel296=depU[136]
fuel297=depU[137]
fuel298=depU[138]
fuel299=depU[139]
fuel300=depU[140]
fuel301=depU[141]
fuel302=depU[142]
fuel303=depU[143]
fuel304=depU[144]
fuel305=depU[145]
fuel306=depU[146]
fuel307=depU[147]
fuel308=depU[148]
fuel309=depU[149]
fuel310=depU[150]
fuel311=depU[151]
fuel312=depU[152]
fuel313=depU[153]
fuel314=depU[154]
fuel315=depU[155]
fuel316=depU[156]
fuel317=depU[157]
fuel318=depU[158]
fuel319=depU[159]
fuel320=depU[160]
fuel321=depU[161]
fuel322=depU[162]
fuel323=depU[163]
fuel324=depU[164]
fuel325=depU[165]
fuel326=depU[166]
fuel327=depU[167]
fuel328=depU[168]
fuel329=depU[169]
fuel330=depU[170]
fuel331=depU[171]
fuel332=depU[172]
fuel333=depU[173]
fuel334=depU[174]
fuel335=depU[175]
fuel336=depU[176]
fuel337=depU[177]
fuel338=depU[178]
fuel339=depU[179]
fuel340=depU[180]
fuel341=depU[181]
fuel342=depU[182]
fuel343=depU[183]
fuel344=depU[184]
fuel345=depU[185]
fuel346=depU[186]
fuel347=depU[187]
fuel348=depU[188]
fuel349=depU[189]
fuel350=depU[190]
fuel351=depU[191]
fuel352=depU[192]
fuel353=depU[193]
fuel354=depU[194]
fuel355=depU[195]
fuel356=depU[196]
fuel357=depU[197]
fuel358=depU[198]
fuel359=depU[199]
fuel360=depU[200]
fuel361=depU[201]
fuel362=depU[202]
fuel363=depU[203]
fuel364=depU[204]
fuel365=depU[205]
fuel366=depU[206]
fuel367=depU[207]
fuel368=depU[208]
fuel369=depU[209]
fuel370=depU[210]
fuel371=depU[211]
fuel372=depU[212]
fuel373=depU[213]
fuel374=depU[214]
fuel375=depU[215]
fuel376=depU[216]
fuel377=depU[217]
fuel378=depU[218]
fuel379=depU[219]
fuel380=depU[220]
fuel381=depU[221]
fuel382=depU[222]
fuel383=depU[223]
fuel384=depU[224]
fuel385=depU[225]
fuel386=depU[226]
fuel387=depU[227]
fuel388=depU[228]
fuel389=depU[229]
fuel390=depU[230]
fuel391=depU[231]
fuel392=depU[232]
fuel393=depU[233]
fuel394=depU[234]
fuel395=depU[235]
fuel396=depU[236]
fuel397=depU[237]
fuel398=depU[238]
fuel399=depU[239]


# In[12]:


fuel=[fuel0,fuel1,fuel2,fuel3,fuel4,fuel5,fuel6,fuel7,fuel8,fuel9,fuel10,fuel11,fuel12,fuel13,fuel14,fuel15,fuel16,fuel17,fuel18,fuel19,fuel20,
fuel21,fuel22,fuel23,fuel24,fuel25,fuel26,fuel27,fuel28,fuel29,fuel30,fuel31,fuel32,fuel33,fuel34,fuel35,fuel36,fuel37,fuel38,fuel39,fuel40,
fuel41,fuel42,fuel43,fuel44,fuel45,fuel46,fuel47,fuel48,fuel49,fuel50,fuel51,fuel52,fuel53,fuel54,fuel55,fuel56,fuel57,fuel58,fuel59,fuel60,
fuel61,fuel62,fuel63,fuel64,fuel65,fuel66,fuel67,fuel68,fuel69,fuel70,fuel71,fuel72,fuel73,fuel74,fuel75,fuel76,fuel77,fuel78,fuel79,fuel80,
fuel81,fuel82,fuel83,fuel84,fuel85,fuel86,fuel87,fuel88,fuel89,fuel90,fuel91,fuel92,fuel93,fuel94,fuel95,fuel96,fuel97,fuel98,fuel99,fuel100,
fuel101,fuel102,fuel103,fuel104,fuel105,fuel106,fuel107,fuel108,fuel109,fuel110,fuel111,fuel112,fuel113,fuel114,fuel115,fuel116,fuel117,fuel118,fuel119,fuel120,
fuel121,fuel122,fuel123,fuel124,fuel125,fuel126,fuel127,fuel128,fuel129,fuel130,fuel131,fuel132,fuel133,fuel134,fuel135,fuel136,fuel137,fuel138,fuel139,fuel140,
fuel141,fuel142,fuel143,fuel144,fuel145,fuel146,fuel147,fuel148,fuel149,fuel150,fuel151,fuel152,fuel153,fuel154,fuel155,fuel156,fuel157,fuel158,fuel159,fuel160,
fuel161,fuel162,fuel163,fuel164,fuel165,fuel166,fuel167,fuel168,fuel169,fuel170,fuel171,fuel172,fuel173,fuel174,fuel175,fuel176,fuel177,fuel178,fuel179,fuel180,
fuel181,fuel182,fuel183,fuel184,fuel185,fuel186,fuel187,fuel188,fuel189,fuel190,fuel191,fuel192,fuel193,fuel194,fuel195,fuel196,fuel197,fuel198,fuel199,fuel200,
fuel201,fuel202,fuel203,fuel204,fuel205,fuel206,fuel207,fuel208,fuel209,fuel210,fuel211,fuel212,fuel213,fuel214,fuel215,fuel216,fuel217,fuel218,fuel219,fuel220,
fuel221,fuel222,fuel223,fuel224,fuel225,fuel226,fuel227,fuel228,fuel229,fuel230,fuel231,fuel232,fuel233,fuel234,fuel235,fuel236,fuel237,fuel238,fuel239,fuel240,
fuel241,fuel242,fuel243,fuel244,fuel245,fuel246,fuel247,fuel248,fuel249,fuel250,fuel251,fuel252,fuel253,fuel254,fuel255,fuel256,fuel257,fuel258,fuel259,fuel260,
fuel261,fuel262,fuel263,fuel264,fuel265,fuel266,fuel267,fuel268,fuel269,fuel270,fuel271,fuel272,fuel273,fuel274,fuel275,fuel276,fuel277,fuel278,fuel279,fuel280,
fuel281,fuel282,fuel283,fuel284,fuel285,fuel286,fuel287,fuel288,fuel289,fuel290,fuel291,fuel292,fuel293,fuel294,fuel295,fuel296,fuel297,fuel298,fuel299,fuel300,
fuel301,fuel302,fuel303,fuel304,fuel305,fuel306,fuel307,fuel308,fuel309,fuel310,fuel311,fuel312,fuel313,fuel314,fuel315,fuel316,fuel317,fuel318,fuel319,fuel320,
fuel321,fuel322,fuel323,fuel324,fuel325,fuel326,fuel327,fuel328,fuel329,fuel330,fuel331,fuel332,fuel333,fuel334,fuel335,fuel336,fuel337,fuel338,fuel339,fuel340,
fuel341,fuel342,fuel343,fuel344,fuel345,fuel346,fuel347,fuel348,fuel349,fuel350,fuel351,fuel352,fuel353,fuel354,fuel355,fuel356,fuel357,fuel358,fuel359,fuel360,
fuel361,fuel362,fuel363,fuel364,fuel365,fuel366,fuel367,fuel368,fuel369,fuel370,fuel371,fuel372,fuel373,fuel374,fuel375,fuel376,fuel377,fuel378,fuel379,fuel380,
fuel381,fuel382,fuel383,fuel384,fuel385,fuel386,fuel387,fuel388,fuel389,fuel390,fuel391,fuel392,fuel393,fuel394,fuel395,fuel396,fuel397,fuel398,fuel399]


# In[13]:


for i in range (0,400):
    pinfuel[i] = openmc.Cell(fill = fuel[i], region = -geom_fuel1 & -up & +low)
    pingap[i] = openmc.Cell(fill = gap, region = +geom_fuel1 & -geom_gap1 & -up & +low)
    pinclad[i] = openmc.Cell(fill = clad, region = +geom_gap1 & -geom_clad1 & -up & +low)
    pincool[i] = openmc.Cell(fill = coolant, region = +geom_clad1& -up & +low)
    univ[i].add_cells([pinfuel[i], pingap[i], pinclad[i],pincool[i]])
    hexa[i] = openmc.Cell(region = openmc.model.hexagonal_prism(edge_length = 9.596 , orientation = 'x') & -up & +low)
    hexac[i] = openmc.Cell(fill = clad, region =~ openmc.model.hexagonal_prism(edge_length = 9.596 , orientation = 'x') & -up & +low) #aware


# In[14]:


#buat pin reflektor dan core
# reflector pin 
pinref1 = openmc.Cell (fill=Reflector, region=-geom_ref1  & -up  & +low)
pincladref1 =  openmc.Cell (fill=Reflector, region=+geom_ref1  & -geom_cladref1  & -up  & +low)
pincoolref1 =  openmc.Cell (fill=coolant, region=+geom_cladref1  & -up  & +low)
univ401.add_cells([pinref1, pincladref1, pincoolref1])
hexa401 = openmc.Cell(region =openmc.model.hexagonal_prism(edge_length=9.596, orientation='x', origin=(0.0,0.0)) & -up &+low)
hexac401 = openmc.Cell(fill = clad, region=~openmc.model.hexagonal_prism(edge_length=9.596, orientation='x', origin=(0.0,0.0)) & -up &+low)

#core
core1 = openmc.Cell  (fill=coolant, region=-inner &-up &+low)
boundary = openmc.Cell(fill=coolant, region=-outer &+inner &-up &+low)
boundaryup = openmc.Cell(fill=coolant, region=-outer  &-up2 &+up)
boundarylow =  openmc.Cell(fill=coolant, region=-outer  &-low &+low2)
assemc = openmc.Cell (fill=coolant)
univ403.add_cells([assemc])


# In[15]:


lat = []
rotUniverse = []
assem = []
rotate = []
for i in range (1,401):
    lat.append('lat'+str(i))
    rotUniverse.append('rotUniverse'+str(i))
    assem.append('assem'+str(i))
    rotate.append('rotate'+str(i))


# In[16]:


for i in range (0,400):
    lat[i] = openmc.HexLattice()
    lat[i].center = [0.,0.]
    lat[i].pitch = [1.28]
    lat[i].orientation = 'x'
    lat[i].universes = [[univ[i]]*42,[univ[i]]*36,[univ[i]]*30,[univ[i]]*24,[univ[i]]*18,[univ[i]]*12,[univ[i]]*6,[univ[i]]*1]
    lat[i].outer = univ403
    rotate[i] = openmc.Cell(fill=lat[i])
    rotUniverse[i] = openmc.Universe(cells=(rotate[i],))
    hexa[i].fill =  rotUniverse[i]
    assem[i] = openmc.Universe(cells=(hexa[i], hexac[i]))
    


# In[17]:


lat401 = openmc.HexLattice()
lat401.center = [0.,0.]
lat401.pitch = [1] #1
lat401.universes = [[univ401]*54, [univ401]*48, [univ401]*42,[univ401]*36,[univ401]*30,[univ401]*24,[univ401]*18,[univ401]*12,[univ401]*6,[univ401]*1]
lat401.outer = univ403
lat401.orientation = 'x'
rotate401 = openmc.Cell(fill=lat401)
rotUniverse401 = openmc.Universe(cells=(rotate401,))
hexa401.fill =  rotUniverse401
assem401 = openmc.Universe(cells=(hexa401, hexac401))


# In[18]:


assem0=assem[0]
assem1=assem[1]
assem2=assem[2]
assem3=assem[3]
assem4=assem[4]
assem5=assem[5]
assem6=assem[6]
assem7=assem[7]
assem8=assem[8]
assem9=assem[9]
assem10=assem[10]
assem11=assem[11]
assem12=assem[12]
assem13=assem[13]
assem14=assem[14]
assem15=assem[15]
assem16=assem[16]
assem17=assem[17]
assem18=assem[18]
assem19=assem[19]
assem20=assem[20]
assem21=assem[21]
assem22=assem[22]
assem23=assem[23]
assem24=assem[24]
assem25=assem[25]
assem26=assem[26]
assem27=assem[27]
assem28=assem[28]
assem29=assem[29]
assem30=assem[30]
assem31=assem[31]
assem32=assem[32]
assem33=assem[33]
assem34=assem[34]
assem35=assem[35]
assem36=assem[36]
assem37=assem[37]
assem38=assem[38]
assem39=assem[39]
assem40=assem[40]
assem41=assem[41]
assem42=assem[42]
assem43=assem[43]
assem44=assem[44]
assem45=assem[45]
assem46=assem[46]
assem47=assem[47]
assem48=assem[48]
assem49=assem[49]
assem50=assem[50]
assem51=assem[51]
assem52=assem[52]
assem53=assem[53]
assem54=assem[54]
assem55=assem[55]
assem56=assem[56]
assem57=assem[57]
assem58=assem[58]
assem59=assem[59]
assem60=assem[60]
assem61=assem[61]
assem62=assem[62]
assem63=assem[63]
assem64=assem[64]
assem65=assem[65]
assem66=assem[66]
assem67=assem[67]
assem68=assem[68]
assem69=assem[69]
assem70=assem[70]
assem71=assem[71]
assem72=assem[72]
assem73=assem[73]
assem74=assem[74]
assem75=assem[75]
assem76=assem[76]
assem77=assem[77]
assem78=assem[78]
assem79=assem[79]
assem80=assem[80]
assem81=assem[81]
assem82=assem[82]
assem83=assem[83]
assem84=assem[84]
assem85=assem[85]
assem86=assem[86]
assem87=assem[87]
assem88=assem[88]
assem89=assem[89]
assem90=assem[90]
assem91=assem[91]
assem92=assem[92]
assem93=assem[93]
assem94=assem[94]
assem95=assem[95]
assem96=assem[96]
assem97=assem[97]
assem98=assem[98]
assem99=assem[99]
assem100=assem[100]
assem101=assem[101]
assem102=assem[102]
assem103=assem[103]
assem104=assem[104]
assem105=assem[105]
assem106=assem[106]
assem107=assem[107]
assem108=assem[108]
assem109=assem[109]
assem110=assem[110]
assem111=assem[111]
assem112=assem[112]
assem113=assem[113]
assem114=assem[114]
assem115=assem[115]
assem116=assem[116]
assem117=assem[117]
assem118=assem[118]
assem119=assem[119]
assem120=assem[120]
assem121=assem[121]
assem122=assem[122]
assem123=assem[123]
assem124=assem[124]
assem125=assem[125]
assem126=assem[126]
assem127=assem[127]


assem128=assem[128]
assem129=assem[129]
assem130=assem[130]
assem131=assem[131]
assem132=assem[132]
assem133=assem[133]
assem134=assem[134]
assem135=assem[135]
assem136=assem[136]
assem137=assem[137]
assem138=assem[138]
assem139=assem[139]
assem140=assem[140]
assem141=assem[141]
assem142=assem[142]
assem143=assem[143]


assem144=assem[144]
assem145=assem[145]
assem146=assem[146]
assem147=assem[147]
assem148=assem[148]
assem149=assem[149]
assem150=assem[150]
assem151=assem[151]
assem152=assem[152]
assem153=assem[153]
assem154=assem[154]
assem155=assem[155]
assem156=assem[156]
assem157=assem[157]
assem158=assem[158]
assem159=assem[159]


assem160=assem[160]
assem161=assem[161]
assem162=assem[162]
assem163=assem[163]
assem164=assem[164]
assem165=assem[165]
assem166=assem[166]
assem167=assem[167]
assem168=assem[168]
assem169=assem[169]
assem170=assem[170]
assem171=assem[171]
assem172=assem[172]
assem173=assem[173]
assem174=assem[174]
assem175=assem[175]
assem176=assem[176]
assem177=assem[177]
assem178=assem[178]
assem179=assem[179]
assem180=assem[180]
assem181=assem[181]
assem182=assem[182]
assem183=assem[183]
assem184=assem[184]
assem185=assem[185]
assem186=assem[186]
assem187=assem[187]
assem188=assem[188]
assem189=assem[189]
assem190=assem[190]
assem191=assem[191]
assem192=assem[192]
assem193=assem[193]
assem194=assem[194]
assem195=assem[195]
assem196=assem[196]
assem197=assem[197]
assem198=assem[198]
assem199=assem[199]
assem200=assem[200]
assem201=assem[201]
assem202=assem[202]
assem203=assem[203]
assem204=assem[204]
assem205=assem[205]
assem206=assem[206]
assem207=assem[207]
assem208=assem[208]
assem209=assem[209]
assem210=assem[210]
assem211=assem[211]
assem212=assem[212]
assem213=assem[213]
assem214=assem[214]
assem215=assem[215]
assem216=assem[216]
assem217=assem[217]
assem218=assem[218]
assem219=assem[219]
assem220=assem[220]
assem221=assem[221]
assem222=assem[222]
assem223=assem[223]
assem224=assem[224]
assem225=assem[225]
assem226=assem[226]
assem227=assem[227]
assem228=assem[228]
assem229=assem[229]
assem230=assem[230]
assem231=assem[231]
assem232=assem[232]
assem233=assem[233]
assem234=assem[234]
assem235=assem[235]
assem236=assem[236]
assem237=assem[237]
assem238=assem[238]
assem239=assem[239]
assem240=assem[240]
assem241=assem[241]
assem242=assem[242]
assem243=assem[243]
assem244=assem[244]
assem245=assem[245]
assem246=assem[246]
assem247=assem[247]
assem248=assem[248]
assem249=assem[249]
assem250=assem[250]
assem251=assem[251]
assem252=assem[252]
assem253=assem[253]
assem254=assem[254]
assem255=assem[255]
assem256=assem[256]
assem257=assem[257]
assem258=assem[258]
assem259=assem[259]
assem260=assem[260]
assem261=assem[261]
assem262=assem[262]
assem263=assem[263]
assem264=assem[264]
assem265=assem[265]
assem266=assem[266]
assem267=assem[267]
assem268=assem[268]
assem269=assem[269]
assem270=assem[270]
assem271=assem[271]
assem272=assem[272]
assem273=assem[273]
assem274=assem[274]
assem275=assem[275]
assem276=assem[276]
assem277=assem[277]
assem278=assem[278]
assem279=assem[279]
assem280=assem[280]
assem281=assem[281]
assem282=assem[282]
assem283=assem[283]
assem284=assem[284]
assem285=assem[285]
assem286=assem[286]
assem287=assem[287]
assem288=assem[288]
assem289=assem[289]
assem290=assem[290]
assem291=assem[291]
assem292=assem[292]
assem293=assem[293]
assem294=assem[294]
assem295=assem[295]
assem296=assem[296]
assem297=assem[297]
assem298=assem[298]
assem299=assem[299]
assem300=assem[300]
assem301=assem[301]
assem302=assem[302]
assem303=assem[303]
assem304=assem[304]
assem305=assem[305]
assem306=assem[306]
assem307=assem[307]
assem308=assem[308]
assem309=assem[309]
assem310=assem[310]
assem311=assem[311]
assem312=assem[312]
assem313=assem[313]
assem314=assem[314]
assem315=assem[315]
assem316=assem[316]
assem317=assem[317]
assem318=assem[318]
assem319=assem[319]
assem320=assem[320]
assem321=assem[321]
assem322=assem[322]
assem323=assem[323]
assem324=assem[324]
assem325=assem[325]
assem326=assem[326]
assem327=assem[327]
assem328=assem[328]
assem329=assem[329]
assem330=assem[330]
assem331=assem[331]
assem332=assem[332]
assem333=assem[333]
assem334=assem[334]
assem335=assem[335]
assem336=assem[336]
assem337=assem[337]
assem338=assem[338]
assem339=assem[339]
assem340=assem[340]
assem341=assem[341]
assem342=assem[342]
assem343=assem[343]
assem344=assem[344]
assem345=assem[345]
assem346=assem[346]
assem347=assem[347]
assem348=assem[348]
assem349=assem[349]
assem350=assem[350]
assem351=assem[351]
assem352=assem[352]
assem353=assem[353]
assem354=assem[354]
assem355=assem[355]
assem356=assem[356]
assem357=assem[357]
assem358=assem[358]
assem359=assem[359]
assem360=assem[360]
assem361=assem[361]
assem362=assem[362]
assem363=assem[363]
assem364=assem[364]
assem365=assem[365]
assem366=assem[366]
assem367=assem[367]
assem368=assem[368]
assem369=assem[369]
assem370=assem[370]
assem371=assem[371]
assem372=assem[372]
assem373=assem[373]
assem374=assem[374]
assem375=assem[375]
assem376=assem[376]
assem377=assem[377]
assem378=assem[378]
assem379=assem[379]
assem380=assem[380]
assem381=assem[381]
assem382=assem[382]
assem383=assem[383]
assem384=assem[384]
assem385=assem[385]
assem386=assem[386]
assem387=assem[387]
assem388=assem[388]
assem389=assem[389]
assem390=assem[390]
assem391=assem[391]
assem392=assem[392]
assem393=assem[393]
assem394=assem[394]
assem395=assem[395]
assem396=assem[396]
assem397=assem[397]
assem398=assem[398]
assem399=assem[399]


# In[19]:


latcore = openmc.HexLattice()
latcore.center = [0., 0., 0.,]
p2 = 16.83
p3 = 5.0
latcore.pitch = [p2, p3]
#secara aksial 
latcore.universes = [[[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem399]*42, [assem369]*36 , [assem339]*30, [assem309]*24, [assem279]*18, [assem249]*12 , [assem219]*6 , [assem189]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem398]*42, [assem368]*36 , [assem338]*30, [assem308]*24, [assem278]*18, [assem248]*12 , [assem218]*6 , [assem188]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem397]*42, [assem367]*36 , [assem337]*30, [assem307]*24, [assem277]*18, [assem247]*12 , [assem217]*6 , [assem187]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem396]*42, [assem366]*36 , [assem336]*30, [assem306]*24, [assem276]*18, [assem246]*12 , [assem216]*6 , [assem186]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem395]*42, [assem365]*36 , [assem335]*30, [assem305]*24, [assem275]*18, [assem245]*12 , [assem215]*6 , [assem185]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem394]*42, [assem364]*36 , [assem334]*30, [assem304]*24, [assem274]*18, [assem244]*12 , [assem214]*6 , [assem184]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem393]*42, [assem363]*36 , [assem333]*30, [assem303]*24, [assem273]*18, [assem243]*12 , [assem213]*6 , [assem183]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem392]*42, [assem362]*36 , [assem332]*30, [assem302]*24, [assem272]*18, [assem242]*12 , [assem212]*6 , [assem182]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem391]*42, [assem361]*36 , [assem331]*30, [assem301]*24, [assem271]*18, [assem241]*12 , [assem211]*6 , [assem181]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem390]*42, [assem360]*36 , [assem330]*30, [assem300]*24, [assem270]*18, [assem240]*12 , [assem210]*6 , [assem180]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem389]*42, [assem359]*36 , [assem329]*30, [assem299]*24, [assem269]*18, [assem239]*12 , [assem209]*6 , [assem179]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem388]*42, [assem358]*36 , [assem328]*30, [assem298]*24, [assem268]*18, [assem238]*12 , [assem208]*6 , [assem178]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem387]*42, [assem357]*36 , [assem327]*30, [assem297]*24, [assem267]*18, [assem237]*12 , [assem207]*6 , [assem177]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem386]*42, [assem356]*36 , [assem326]*30, [assem296]*24, [assem266]*18, [assem236]*12 , [assem206]*6 , [assem176]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem385]*42, [assem355]*36 , [assem325]*30, [assem295]*24, [assem265]*18, [assem235]*12 , [assem205]*6 , [assem175]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem384]*42, [assem354]*36 , [assem324]*30, [assem294]*24, [assem264]*18, [assem234]*12 , [assem204]*6 , [assem174]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem383]*42, [assem353]*36 , [assem323]*30, [assem293]*24, [assem263]*18, [assem233]*12 , [assem203]*6 , [assem173]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem382]*42, [assem352]*36 , [assem322]*30, [assem292]*24, [assem262]*18, [assem232]*12 , [assem202]*6 , [assem172]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem381]*42, [assem351]*36 , [assem321]*30, [assem291]*24, [assem261]*18, [assem231]*12 , [assem201]*6 , [assem171]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem380]*42, [assem350]*36 , [assem320]*30, [assem290]*24, [assem260]*18, [assem230]*12 , [assem200]*6 , [assem170]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem379]*42, [assem349]*36 , [assem319]*30, [assem289]*24, [assem259]*18, [assem229]*12 , [assem199]*6 , [assem169]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem378]*42, [assem348]*36 , [assem318]*30, [assem288]*24, [assem258]*18, [assem228]*12 , [assem198]*6 , [assem168]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem377]*42, [assem347]*36 , [assem317]*30, [assem287]*24, [assem257]*18, [assem227]*12 , [assem197]*6 , [assem167]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem376]*42, [assem346]*36 , [assem316]*30, [assem286]*24, [assem256]*18, [assem226]*12 , [assem196]*6 , [assem166]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem375]*42, [assem345]*36 , [assem315]*30, [assem285]*24, [assem255]*18, [assem225]*12 , [assem195]*6 , [assem165]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem374]*42, [assem344]*36 , [assem314]*30, [assem284]*24, [assem254]*18, [assem224]*12 , [assem194]*6 , [assem164]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem373]*42, [assem343]*36 , [assem313]*30, [assem283]*24, [assem253]*18, [assem223]*12 , [assem193]*6 , [assem163]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem372]*42, [assem342]*36 , [assem312]*30, [assem282]*24, [assem252]*18, [assem222]*12 , [assem192]*6 , [assem162]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem371]*42, [assem341]*36 , [assem311]*30, [assem281]*24, [assem251]*18, [assem221]*12 , [assem191]*6 , [assem161]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem370]*42, [assem340]*36 , [assem310]*30, [assem280]*24, [assem250]*18, [assem220]*12 , [assem190]*6 , [assem160]*1],
                      
                                          
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem159]*42, [assem157]*36 , [assem155]*30, [assem153]*24, [assem151]*18, [assem149]*12 , [assem147]*6 , [assem145]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem158]*42, [assem156]*36 , [assem154]*30, [assem152]*24, [assem150]*18, [assem148]*12 , [assem146]*6 , [assem144]*1],
                    
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem143]*42, [assem141]*36 , [assem139]*30, [assem137]*24, [assem135]*18, [assem133]*12 , [assem131]*6 , [assem129]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem142]*42, [assem140]*36 , [assem138]*30, [assem136]*24, [assem134]*18, [assem132]*12 , [assem130]*6 , [assem128]*1],
                        
                     
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem127]*42, [assem126]*36 , [assem125]*30, [assem124]*24, [assem123]*18, [assem122]*12 , [assem121]*6 , [assem120]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem119]*42, [assem118]*36 , [assem117]*30, [assem116]*24, [assem115]*18, [assem114]*12 , [assem113]*6 , [assem112]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem111]*42, [assem110]*36 , [assem109]*30, [assem108]*24, [assem107]*18, [assem106]*12 , [assem105]*6 , [assem104]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem103]*42, [assem102]*36 , [assem101]*30, [assem100]*24, [assem99]*18, [assem98]*12 , [assem97]*6 , [assem96]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem95]*42, [assem94]*36 , [assem93]*30, [assem92]*24, [assem91]*18, [assem90]*12 , [assem89]*6 , [assem88]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem87]*42, [assem86]*36 , [assem85]*30, [assem84]*24, [assem83]*18, [assem82]*12 , [assem81]*6 , [assem80]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem79]*42, [assem78]*36 , [assem77]*30, [assem76]*24, [assem75]*18, [assem74]*12 , [assem73]*6 , [assem72]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem71]*42, [assem70]*36 , [assem69]*30, [assem68]*24, [assem67]*18, [assem66]*12 , [assem65]*6 , [assem64]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem63]*42, [assem62]*36 , [assem61]*30, [assem60]*24, [assem59]*18, [assem58]*12 , [assem57]*6 , [assem56]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem55]*42, [assem54]*36 , [assem53]*30, [assem52]*24, [assem51]*18, [assem50]*12 , [assem49]*6 , [assem48]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem47]*42, [assem46]*36 , [assem45]*30, [assem44]*24, [assem43]*18, [assem42]*12 , [assem41]*6 , [assem40]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem39]*42, [assem38]*36 , [assem37]*30, [assem36]*24, [assem35]*18, [assem34]*12 , [assem33]*6 , [assem32]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem31]*42, [assem30]*36 , [assem29]*30, [assem28]*24, [assem27]*18, [assem26]*12 , [assem25]*6 , [assem24]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem23]*42, [assem22]*36 , [assem21]*30, [assem20]*24, [assem19]*18, [assem18]*12 , [assem17]*6 , [assem16]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem15]*42, [assem14]*36 , [assem13]*30, [assem12]*24, [assem11]*18, [assem10]*12 , [assem9]*6 , [assem8]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48,    [assem7]*42, [assem6]*36 , [assem5]*30, [assem4]*24, [assem3]*18, [assem2]*12 , [assem1]*6 , [assem0]*1],
                      
                     
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1],
                     [[assem401]*66, [assem401]*60, [assem401]*54, [assem401]*48, [assem401]*42, [assem401]*36 , [assem401]*30, [assem401]*24, [assem401]*18, [assem401]*12 , [assem401]*6 , [assem401]*1]]


# In[20]:


latcore.outer = univ403
core1.fill = latcore
root.add_cells([core1, boundary, boundaryup, boundarylow])


# In[21]:


geometry = openmc.Geometry(root)
geometry.export_to_xml()


# In[22]:


H = 370
D =   252.41 + 2*67.31
bounds = [-D/2, -D/2, -H/2,D/2, D/2, H/2]
uniform_dist = openmc.stats.Box (bounds[:3], bounds[3:], only_fissionable = True)
'''
#D = 252.41 + 2*67.31
src = openmc.Source()
#src.energy = openmc.stats.Discrete([10.0e6], [1.0e6])
src.space = openmc.stats.Box ([-D/2, -D/2, -H/2],[D/2, D/2, H/2], only_fissionable = True)
'''
settings = openmc.Settings ()
#settings.source = src
settings.batches = 250
settings.inactive = 25
settings.particles = 10000

settings.export_to_xml()


# In[23]:


######################################################################################################################################################################################################
#############################################################################################TALLIES XML##############################################################################################
######################################################################################################################################################################################################


# In[24]:


'''
#Tahun ke-
zmin, zmax, radius = -H/2, H/2, D/2
flux_tally_legendre = openmc.Tally()
#Tahun ke-1

sp_1 = openmc.StatePoint('openmc_simulation_n1.h5')
fission_zr = sp_1.tallies[fis_tally_zernike_radial.id].get_pandas_dataframe()
heating = sp_1.tallies[heating_tally.id].get_pandas_dataframe()
heating_mean = np.array(heating['mean'])
normalize = ((power/(Q*heating_mean)))
mean_fission_zr = fission_zr['mean']
equ_fission_zr = openmc.ZernikeRadial(mean_fission_zr, radius = radius)

fission_leg = sp_1.tallies[fis_tally_legendre.id].get_pandas_dataframe()
mean_fission_leg = fission_leg['mean']
equ_fission_leg = openmc.legendre_from_expcoef(mean_fission_leg, domain = (zmin,zmax))

fission_1 = np.array([equ_fission_leg(z)]).T@np.array([equ_fission_zr(zeniths)])
plt.figure(figsize =(10,10))
plt.title('Fission Distribution')
plt.xlabel('Radial Position [cm]')
plt.ylabel('Axial Height [cm]')
plt.pcolor(zeniths, z, fission_1*normalize, cmap='jet')
plt.colorbar()
plt.savefig('Distribusi Fisi Aksial Radial Tahun ke-1.jpg', dpi = 1000)
'''


# In[25]:


plot_xy = openmc.Plot()
plot_xy.filename= 'plot_xy'
plot_xy.origin = (0,0,0)
plot_xy.width = (450, 450)
plot_xy.pixels = (5000, 5000)
plot_xy.colors = {gap: (135, 206, 250), Reflector:'coral', clad :'yellow', coolant :(135, 206, 250), 
                  fuel0: 'red',fuel1: 'red',fuel2: 'red',fuel3: 'red',fuel4: 'red',fuel5: 'red',fuel6: 'red',fuel7: 'red',fuel8: 'red',fuel9: 'red',fuel10: 'red',fuel11: 'red',fuel12: 'red',fuel13: 'red',fuel14: 'red',fuel15: 'red',fuel16: 'red',fuel17: 'red',fuel18: 'red',fuel19: 'red',fuel20: 'red',
fuel21: 'red',fuel22: 'red',fuel23: 'red',fuel24: 'red',fuel25: 'red',fuel26: 'red',fuel27: 'red',fuel28: 'red',fuel29: 'red',fuel30: 'red',fuel31: 'red',fuel32: 'red',fuel33: 'red',fuel34: 'red',fuel35: 'red',fuel36: 'red',fuel37: 'red',fuel38: 'red',fuel39: 'red',fuel40: 'red',
fuel41: 'red',fuel42: 'red',fuel43: 'red',fuel44: 'red',fuel45: 'red',fuel46: 'red',fuel47: 'red',fuel48: 'red',fuel49: 'red',fuel50: 'red',fuel51: 'red',fuel52: 'red',fuel53: 'red',fuel54: 'red',fuel55: 'red',fuel56: 'red',fuel57: 'red',fuel58: 'red',fuel59: 'red',fuel60: 'red',
fuel61: 'red',fuel62: 'red',fuel63: 'red',fuel64: 'red',fuel65: 'red',fuel66: 'red',fuel67: 'red',fuel68: 'red',fuel69: 'red',fuel70: 'red',fuel71: 'red',fuel72: 'red',fuel73: 'red',fuel74: 'red',fuel75: 'red',fuel76: 'red',fuel77: 'red',fuel78: 'red',fuel79: 'red',fuel80: 'red',
fuel81: 'red',fuel82: 'red',fuel83: 'red',fuel84: 'red',fuel85: 'red',fuel86: 'red',fuel87: 'red',fuel88: 'red',fuel89: 'red',fuel90: 'red',fuel91: 'red',fuel92: 'red',fuel93: 'red',fuel94: 'red',fuel95: 'red',fuel96: 'red',fuel97: 'red',fuel98: 'red',fuel99: 'red',fuel100: 'red',
fuel101: 'red',fuel102: 'red',fuel103: 'red',fuel104: 'red',fuel105: 'red',fuel106: 'red',fuel107: 'red',fuel108: 'red',fuel109: 'red',fuel110: 'red',fuel111: 'red',fuel112: 'red',fuel113: 'red',fuel114: 'red',fuel115: 'red',fuel116: 'red',fuel117: 'red',fuel118: 'red',fuel119: 'red',fuel120: 'red',
fuel121: 'red',fuel122: 'red',fuel123: 'red',fuel124: 'red',fuel125: 'red',fuel126: 'red',fuel127: 'red',fuel128: 'grey',fuel129: 'grey',fuel130: 'grey',fuel131: 'grey',fuel132: 'grey',fuel133: 'grey',fuel134: 'grey',fuel135: 'grey',fuel136: 'grey',fuel137: 'grey',fuel138: 'grey',fuel139: 'grey',fuel140: 'grey',
fuel141: 'grey',fuel142: 'grey',fuel143: 'grey',fuel144: 'orange',fuel145: 'orange',fuel146: 'orange',fuel147: 'orange',fuel148: 'orange',fuel149: 'orange',fuel150: 'orange',fuel151: 'orange',fuel152: 'orange',fuel153: 'orange',fuel154: 'orange',fuel155: 'orange',fuel156: 'orange',fuel157: 'orange',fuel158: 'orange',fuel159: 'orange',fuel160: 'purple',
fuel161: 'purple',fuel162: 'purple',fuel163: 'purple',fuel164: 'purple',fuel165: 'purple',fuel166: 'purple',fuel167: 'purple',fuel168: 'purple',fuel169: 'purple',fuel170: 'purple',fuel171: 'purple',fuel172: 'purple',fuel173: 'purple',fuel174: 'purple',fuel175: 'purple',fuel176: 'purple',fuel177: 'purple',fuel178: 'purple',fuel179: 'purple',fuel180: 'purple',
fuel181: 'purple',fuel182: 'purple',fuel183: 'purple',fuel184: 'purple',fuel185: 'purple',fuel186: 'purple',fuel187: 'purple',fuel188: 'purple',fuel189: 'purple',fuel190: 'purple',fuel191: 'purple',fuel192: 'purple',fuel193: 'purple',fuel194: 'purple',fuel195: 'purple',fuel196: 'purple',fuel197: 'purple',fuel198: 'purple',fuel199: 'purple',fuel200: 'purple',
fuel201: 'purple',fuel202: 'purple',fuel203: 'purple',fuel204: 'purple',fuel205: 'purple',fuel206: 'purple',fuel207: 'purple',fuel208: 'purple',fuel209: 'purple',fuel210: 'purple',fuel211: 'purple',fuel212: 'purple',fuel213: 'purple',fuel214: 'purple',fuel215: 'purple',fuel216: 'purple',fuel217: 'purple',fuel218: 'purple',fuel219: 'purple',fuel220: 'purple',
fuel221: 'purple',fuel222: 'purple',fuel223: 'purple',fuel224: 'purple',fuel225: 'purple',fuel226: 'purple',fuel227: 'purple',fuel228: 'purple',fuel229: 'purple',fuel230: 'purple',fuel231: 'purple',fuel232: 'purple',fuel233: 'purple',fuel234: 'purple',fuel235: 'purple',fuel236: 'purple',fuel237: 'purple',fuel238: 'purple',fuel239: 'purple',fuel240: 'purple',
fuel241: 'purple',fuel242: 'purple',fuel243: 'purple',fuel244: 'purple',fuel245: 'purple',fuel246: 'purple',fuel247: 'purple',fuel248: 'purple',fuel249: 'purple',fuel250: 'purple',fuel251: 'purple',fuel252: 'purple',fuel253: 'purple',fuel254: 'purple',fuel255: 'purple',fuel256: 'purple',fuel257: 'purple',fuel258: 'purple',fuel259: 'purple',fuel260: 'purple',
fuel261: 'purple',fuel262: 'purple',fuel263: 'purple',fuel264: 'purple',fuel265: 'purple',fuel266: 'purple',fuel267: 'purple',fuel268: 'purple',fuel269: 'purple',fuel270: 'purple',fuel271: 'purple',fuel272: 'purple',fuel273: 'purple',fuel274: 'purple',fuel275: 'purple',fuel276: 'purple',fuel277: 'purple',fuel278: 'purple',fuel279: 'purple',fuel280: 'purple',
fuel281: 'purple',fuel282: 'purple',fuel283: 'purple',fuel284: 'purple',fuel285: 'purple',fuel286: 'purple',fuel287: 'purple',fuel288: 'purple',fuel289: 'purple',fuel290: 'purple',fuel291: 'purple',fuel292: 'purple',fuel293: 'purple',fuel294: 'purple',fuel295: 'purple',fuel296: 'purple',fuel297: 'purple',fuel298: 'purple',fuel299: 'purple',fuel300: 'purple',
fuel301: 'purple',fuel302: 'purple',fuel303: 'purple',fuel304: 'purple',fuel305: 'purple',fuel306: 'purple',fuel307: 'purple',fuel308: 'purple',fuel309: 'purple',fuel310: 'purple',fuel311: 'purple',fuel312: 'purple',fuel313: 'purple',fuel314: 'purple',fuel315: 'purple',fuel316: 'purple',fuel317: 'purple',fuel318: 'purple',fuel319: 'purple',fuel320: 'purple',
fuel321: 'purple',fuel322: 'purple',fuel323: 'purple',fuel324: 'purple',fuel325: 'purple',fuel326: 'purple',fuel327: 'purple',fuel328: 'purple',fuel329: 'purple',fuel330: 'purple',fuel331: 'purple',fuel332: 'purple',fuel333: 'purple',fuel334: 'purple',fuel335: 'purple',fuel336: 'purple',fuel337: 'purple',fuel338: 'purple',fuel339: 'purple',fuel340: 'purple',
fuel341: 'purple',fuel342: 'purple',fuel343: 'purple',fuel344: 'purple',fuel345: 'purple',fuel346: 'purple',fuel347: 'purple',fuel348: 'purple',fuel349: 'purple',fuel350: 'purple',fuel351: 'purple',fuel352: 'purple',fuel353: 'purple',fuel354: 'purple',fuel355: 'purple',fuel356: 'purple',fuel357: 'purple',fuel358: 'purple',fuel359: 'purple',fuel360: 'purple',
fuel361: 'purple',fuel362: 'purple',fuel363: 'purple',fuel364: 'purple',fuel365: 'purple',fuel366: 'purple',fuel367: 'purple',fuel368: 'purple',fuel369: 'purple',fuel370: 'purple',fuel371: 'purple',fuel372: 'purple',fuel373: 'purple',fuel374: 'purple',fuel375: 'purple',fuel376: 'purple',fuel377: 'purple',fuel378: 'purple',fuel379: 'purple',fuel380: 'purple',
fuel381: 'purple',fuel382: 'purple',fuel383: 'purple',fuel384: 'purple',fuel385: 'purple',fuel386: 'purple',fuel387: 'purple',fuel388: 'purple',fuel389: 'purple',fuel390: 'purple',fuel391: 'purple',fuel392: 'purple',fuel393: 'purple',fuel394: 'purple',fuel395: 'purple',fuel396: 'purple',fuel397: 'purple',fuel398: 'purple',fuel399:'purple'}

plot_xy.color_by = 'material'

plot_yz = openmc.Plot()
plot_yz.filename= 'plot_yz'
plot_yz.origin = (0,0,0)
plot_yz.width = (500,500)
plot_yz.pixels = (5000, 5000)
plot_yz.colors = {gap: (135, 206, 250), Reflector:'coral',clad :'yellow', coolant :(135, 206, 250), 
                  fuel0: 'red',fuel1: 'red',fuel2: 'red',fuel3: 'red',fuel4: 'red',fuel5: 'red',fuel6: 'red',fuel7: 'red',fuel8: 'red',fuel9: 'red',fuel10: 'red',fuel11: 'red',fuel12: 'red',fuel13: 'red',fuel14: 'red',fuel15: 'red',fuel16: 'red',fuel17: 'red',fuel18: 'red',fuel19: 'red',fuel20: 'red',
fuel21: 'red',fuel22: 'red',fuel23: 'red',fuel24: 'red',fuel25: 'red',fuel26: 'red',fuel27: 'red',fuel28: 'red',fuel29: 'red',fuel30: 'red',fuel31: 'red',fuel32: 'red',fuel33: 'red',fuel34: 'red',fuel35: 'red',fuel36: 'red',fuel37: 'red',fuel38: 'red',fuel39: 'red',fuel40: 'red',
fuel41: 'red',fuel42: 'red',fuel43: 'red',fuel44: 'red',fuel45: 'red',fuel46: 'red',fuel47: 'red',fuel48: 'red',fuel49: 'red',fuel50: 'red',fuel51: 'red',fuel52: 'red',fuel53: 'red',fuel54: 'red',fuel55: 'red',fuel56: 'red',fuel57: 'red',fuel58: 'red',fuel59: 'red',fuel60: 'red',
fuel61: 'red',fuel62: 'red',fuel63: 'red',fuel64: 'red',fuel65: 'red',fuel66: 'red',fuel67: 'red',fuel68: 'red',fuel69: 'red',fuel70: 'red',fuel71: 'red',fuel72: 'red',fuel73: 'red',fuel74: 'red',fuel75: 'red',fuel76: 'red',fuel77: 'red',fuel78: 'red',fuel79: 'red',fuel80: 'red',
fuel81: 'red',fuel82: 'red',fuel83: 'red',fuel84: 'red',fuel85: 'red',fuel86: 'red',fuel87: 'red',fuel88: 'red',fuel89: 'red',fuel90: 'red',fuel91: 'red',fuel92: 'red',fuel93: 'red',fuel94: 'red',fuel95: 'red',fuel96: 'red',fuel97: 'red',fuel98: 'red',fuel99: 'red',fuel100: 'red',
fuel101: 'red',fuel102: 'red',fuel103: 'red',fuel104: 'red',fuel105: 'red',fuel106: 'red',fuel107: 'red',fuel108: 'red',fuel109: 'red',fuel110: 'red',fuel111: 'red',fuel112: 'red',fuel113: 'red',fuel114: 'red',fuel115: 'red',fuel116: 'red',fuel117: 'red',fuel118: 'red',fuel119: 'red',fuel120: 'red',
fuel121: 'red',fuel122: 'red',fuel123: 'red',fuel124: 'red',fuel125: 'red',fuel126: 'red',fuel127: 'red',fuel128: 'grey',fuel129: 'grey',fuel130: 'grey',fuel131: 'grey',fuel132: 'grey',fuel133: 'grey',fuel134: 'grey',fuel135: 'grey',fuel136: 'grey',fuel137: 'grey',fuel138: 'grey',fuel139: 'grey',fuel140: 'grey',
fuel141: 'grey',fuel142: 'grey',fuel143: 'grey',fuel144: 'orange',fuel145: 'orange',fuel146: 'orange',fuel147: 'orange',fuel148: 'orange',fuel149: 'orange',fuel150: 'orange',fuel151: 'orange',fuel152: 'orange',fuel153: 'orange',fuel154: 'orange',fuel155: 'orange',fuel156: 'orange',fuel157: 'orange',fuel158: 'orange',fuel159: 'orange',fuel160: 'purple',
fuel161: 'purple',fuel162: 'purple',fuel163: 'purple',fuel164: 'purple',fuel165: 'purple',fuel166: 'purple',fuel167: 'purple',fuel168: 'purple',fuel169: 'purple',fuel170: 'purple',fuel171: 'purple',fuel172: 'purple',fuel173: 'purple',fuel174: 'purple',fuel175: 'purple',fuel176: 'purple',fuel177: 'purple',fuel178: 'purple',fuel179: 'purple',fuel180: 'purple',
fuel181: 'purple',fuel182: 'purple',fuel183: 'purple',fuel184: 'purple',fuel185: 'purple',fuel186: 'purple',fuel187: 'purple',fuel188: 'purple',fuel189: 'purple',fuel190: 'purple',fuel191: 'purple',fuel192: 'purple',fuel193: 'purple',fuel194: 'purple',fuel195: 'purple',fuel196: 'purple',fuel197: 'purple',fuel198: 'purple',fuel199: 'purple',fuel200: 'purple',
fuel201: 'purple',fuel202: 'purple',fuel203: 'purple',fuel204: 'purple',fuel205: 'purple',fuel206: 'purple',fuel207: 'purple',fuel208: 'purple',fuel209: 'purple',fuel210: 'purple',fuel211: 'purple',fuel212: 'purple',fuel213: 'purple',fuel214: 'purple',fuel215: 'purple',fuel216: 'purple',fuel217: 'purple',fuel218: 'purple',fuel219: 'purple',fuel220: 'purple',
fuel221: 'purple',fuel222: 'purple',fuel223: 'purple',fuel224: 'purple',fuel225: 'purple',fuel226: 'purple',fuel227: 'purple',fuel228: 'purple',fuel229: 'purple',fuel230: 'purple',fuel231: 'purple',fuel232: 'purple',fuel233: 'purple',fuel234: 'purple',fuel235: 'purple',fuel236: 'purple',fuel237: 'purple',fuel238: 'purple',fuel239: 'purple',fuel240: 'purple',
fuel241: 'purple',fuel242: 'purple',fuel243: 'purple',fuel244: 'purple',fuel245: 'purple',fuel246: 'purple',fuel247: 'purple',fuel248: 'purple',fuel249: 'purple',fuel250: 'purple',fuel251: 'purple',fuel252: 'purple',fuel253: 'purple',fuel254: 'purple',fuel255: 'purple',fuel256: 'purple',fuel257: 'purple',fuel258: 'purple',fuel259: 'purple',fuel260: 'purple',
fuel261: 'purple',fuel262: 'purple',fuel263: 'purple',fuel264: 'purple',fuel265: 'purple',fuel266: 'purple',fuel267: 'purple',fuel268: 'purple',fuel269: 'purple',fuel270: 'purple',fuel271: 'purple',fuel272: 'purple',fuel273: 'purple',fuel274: 'purple',fuel275: 'purple',fuel276: 'purple',fuel277: 'purple',fuel278: 'purple',fuel279: 'purple',fuel280: 'purple',
fuel281: 'purple',fuel282: 'purple',fuel283: 'purple',fuel284: 'purple',fuel285: 'purple',fuel286: 'purple',fuel287: 'purple',fuel288: 'purple',fuel289: 'purple',fuel290: 'purple',fuel291: 'purple',fuel292: 'purple',fuel293: 'purple',fuel294: 'purple',fuel295: 'purple',fuel296: 'purple',fuel297: 'purple',fuel298: 'purple',fuel299: 'purple',fuel300: 'purple',
fuel301: 'purple',fuel302: 'purple',fuel303: 'purple',fuel304: 'purple',fuel305: 'purple',fuel306: 'purple',fuel307: 'purple',fuel308: 'purple',fuel309: 'purple',fuel310: 'purple',fuel311: 'purple',fuel312: 'purple',fuel313: 'purple',fuel314: 'purple',fuel315: 'purple',fuel316: 'purple',fuel317: 'purple',fuel318: 'purple',fuel319: 'purple',fuel320: 'purple',
fuel321: 'purple',fuel322: 'purple',fuel323: 'purple',fuel324: 'purple',fuel325: 'purple',fuel326: 'purple',fuel327: 'purple',fuel328: 'purple',fuel329: 'purple',fuel330: 'purple',fuel331: 'purple',fuel332: 'purple',fuel333: 'purple',fuel334: 'purple',fuel335: 'purple',fuel336: 'purple',fuel337: 'purple',fuel338: 'purple',fuel339: 'purple',fuel340: 'purple',
fuel341: 'purple',fuel342: 'purple',fuel343: 'purple',fuel344: 'purple',fuel345: 'purple',fuel346: 'purple',fuel347: 'purple',fuel348: 'purple',fuel349: 'purple',fuel350: 'purple',fuel351: 'purple',fuel352: 'purple',fuel353: 'purple',fuel354: 'purple',fuel355: 'purple',fuel356: 'purple',fuel357: 'purple',fuel358: 'purple',fuel359: 'purple',fuel360: 'purple',
fuel361: 'purple',fuel362: 'purple',fuel363: 'purple',fuel364: 'purple',fuel365: 'purple',fuel366: 'purple',fuel367: 'purple',fuel368: 'purple',fuel369: 'purple',fuel370: 'purple',fuel371: 'purple',fuel372: 'purple',fuel373: 'purple',fuel374: 'purple',fuel375: 'purple',fuel376: 'purple',fuel377: 'purple',fuel378: 'purple',fuel379: 'purple',fuel380: 'purple',
fuel381: 'purple',fuel382: 'purple',fuel383: 'purple',fuel384: 'purple',fuel385: 'purple',fuel386: 'purple',fuel387: 'purple',fuel388: 'purple',fuel389: 'purple',fuel390: 'purple',fuel391: 'purple',fuel392: 'purple',fuel393: 'purple',fuel394: 'purple',fuel395: 'purple',fuel396: 'purple',fuel397: 'purple',fuel398: 'purple',fuel399:'purple'}

plot_yz.color_by = 'material'
plot_yz.basis = 'yz'

plots = openmc.Plots ([plot_yz,plot_xy])
plots.export_to_xml()
openmc.plot_geometry()


# In[26]:


openmc.plot_geometry()


# In[27]:


###########SET VOLUME##############
n_assem = 1 + 6 + 12 + 18 + 24 + 30 + 36 + 42
n_assem1 = 1
n_assem2 = 6
n_assem3 = 12
n_assem4 = 18
n_assem5 = 24
n_assem6 = 30
n_assem7 = 36
n_assem8 = 42

volume1 = {}
volume2 = {}
volume3 = {}
volume4 = {}
volume5 = {}
volume6 = {}
volume7 = {}
volume8 = {}

volume1[fuel1] = n_assem1 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume2[fuel2] = n_assem2 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume3[fuel3] = n_assem3 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume4[fuel4] = n_assem4 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume5[fuel5] = n_assem5 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume6[fuel6] = n_assem6 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume7[fuel7] = n_assem7 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2
volume8[fuel8] = n_assem8 * 1*169 * p3 * np.pi * geom_fuel1.coefficients['r'] ** 2

fuel[0].volume = volume1[fuel1] 
fuel[1].volume = volume1[fuel1] 
fuel[2].volume = volume1[fuel1] 
fuel[3].volume = volume1[fuel1] 
fuel[4].volume = volume1[fuel1] 
fuel[5].volume = volume1[fuel1] 
fuel[6].volume = volume1[fuel1] 
fuel[7].volume = volume1[fuel1] 
fuel[8].volume = volume1[fuel1] 
fuel[9].volume = volume1[fuel1] 
fuel[10].volume = volume1[fuel1] 
fuel[11].volume = volume1[fuel1] 
fuel[12].volume = volume1[fuel1] 
fuel[13].volume = volume1[fuel1] 
fuel[14].volume = volume1[fuel1] 
fuel[15].volume = volume1[fuel1] 
fuel[16].volume = volume1[fuel1] 
fuel[17].volume = volume1[fuel1] 
fuel[18].volume = volume1[fuel1] 
fuel[19].volume = volume1[fuel1] 

fuel[20].volume = volume2[fuel2] 
fuel[21].volume = volume2[fuel2] 
fuel[22].volume = volume2[fuel2] 
fuel[23].volume = volume2[fuel2] 
fuel[24].volume = volume2[fuel2] 
fuel[25].volume = volume2[fuel2] 
fuel[26].volume = volume2[fuel2] 
fuel[27].volume = volume2[fuel2] 
fuel[28].volume = volume2[fuel2] 
fuel[29].volume = volume2[fuel2] 
fuel[30].volume = volume2[fuel2] 
fuel[31].volume = volume2[fuel2] 
fuel[32].volume = volume2[fuel2] 
fuel[33].volume = volume2[fuel2] 
fuel[34].volume = volume2[fuel2] 
fuel[35].volume = volume2[fuel2] 
fuel[36].volume = volume2[fuel2] 
fuel[37].volume = volume2[fuel2] 
fuel[38].volume = volume2[fuel2] 
fuel[39].volume = volume2[fuel2] 

fuel[40].volume = volume3[fuel3] 
fuel[41].volume = volume3[fuel3] 
fuel[42].volume = volume3[fuel3] 
fuel[43].volume = volume3[fuel3] 
fuel[44].volume = volume3[fuel3] 
fuel[45].volume = volume3[fuel3] 
fuel[46].volume = volume3[fuel3] 
fuel[47].volume = volume3[fuel3] 
fuel[48].volume = volume3[fuel3] 
fuel[49].volume = volume3[fuel3] 
fuel[50].volume = volume3[fuel3] 
fuel[51].volume = volume3[fuel3] 
fuel[52].volume = volume3[fuel3] 
fuel[53].volume = volume3[fuel3] 
fuel[54].volume = volume3[fuel3] 
fuel[55].volume = volume3[fuel3] 
fuel[56].volume = volume3[fuel3] 
fuel[57].volume = volume3[fuel3] 
fuel[58].volume = volume3[fuel3] 
fuel[59].volume = volume3[fuel3] 

fuel[60].volume = volume4[fuel4] 
fuel[61].volume = volume4[fuel4] 
fuel[62].volume = volume4[fuel4] 
fuel[63].volume = volume4[fuel4] 
fuel[64].volume = volume4[fuel4] 
fuel[65].volume = volume4[fuel4] 
fuel[66].volume = volume4[fuel4] 
fuel[67].volume = volume4[fuel4] 
fuel[68].volume = volume4[fuel4] 
fuel[69].volume = volume4[fuel4] 
fuel[70].volume = volume4[fuel4] 
fuel[71].volume = volume4[fuel4] 
fuel[72].volume = volume4[fuel4] 
fuel[73].volume = volume4[fuel4] 
fuel[74].volume = volume4[fuel4] 
fuel[75].volume = volume4[fuel4] 
fuel[76].volume = volume4[fuel4] 
fuel[77].volume = volume4[fuel4] 
fuel[78].volume = volume4[fuel4] 
fuel[79].volume = volume4[fuel4] 

fuel[80].volume = volume5[fuel5] 
fuel[81].volume = volume5[fuel5] 
fuel[82].volume = volume5[fuel5] 
fuel[83].volume = volume5[fuel5] 
fuel[84].volume = volume5[fuel5] 
fuel[85].volume = volume5[fuel5] 
fuel[86].volume = volume5[fuel5] 
fuel[87].volume = volume5[fuel5] 
fuel[88].volume = volume5[fuel5] 
fuel[89].volume = volume5[fuel5] 
fuel[90].volume = volume5[fuel5] 
fuel[91].volume = volume5[fuel5] 
fuel[92].volume = volume5[fuel5] 
fuel[93].volume = volume5[fuel5] 
fuel[94].volume = volume5[fuel5] 
fuel[95].volume = volume5[fuel5] 
fuel[96].volume = volume5[fuel5] 
fuel[97].volume = volume5[fuel5] 
fuel[98].volume = volume5[fuel5] 
fuel[99].volume = volume5[fuel5] 

fuel[100].volume = volume6[fuel6] 
fuel[101].volume = volume6[fuel6] 
fuel[102].volume = volume6[fuel6] 
fuel[103].volume = volume6[fuel6] 
fuel[104].volume = volume6[fuel6] 
fuel[105].volume = volume6[fuel6] 
fuel[106].volume = volume6[fuel6] 
fuel[107].volume = volume6[fuel6] 
fuel[108].volume = volume6[fuel6] 
fuel[109].volume = volume6[fuel6] 
fuel[110].volume = volume6[fuel6] 
fuel[111].volume = volume6[fuel6] 
fuel[112].volume = volume6[fuel6] 
fuel[113].volume = volume6[fuel6] 
fuel[114].volume = volume6[fuel6] 
fuel[115].volume = volume6[fuel6] 
fuel[116].volume = volume6[fuel6] 
fuel[117].volume = volume6[fuel6] 
fuel[118].volume = volume6[fuel6] 
fuel[119].volume = volume6[fuel6] 

fuel[120].volume = volume7[fuel7] 
fuel[121].volume = volume7[fuel7] 
fuel[122].volume = volume7[fuel7] 
fuel[123].volume = volume7[fuel7] 
fuel[124].volume = volume7[fuel7] 
fuel[125].volume = volume7[fuel7] 
fuel[126].volume = volume7[fuel7] 
fuel[127].volume = volume7[fuel7] 
fuel[128].volume = volume7[fuel7] 
fuel[129].volume = volume7[fuel7] 
fuel[130].volume = volume7[fuel7] 
fuel[131].volume = volume7[fuel7] 
fuel[132].volume = volume7[fuel7] 
fuel[133].volume = volume7[fuel7] 
fuel[134].volume = volume7[fuel7] 
fuel[135].volume = volume7[fuel7] 
fuel[136].volume = volume7[fuel7] 
fuel[137].volume = volume7[fuel7] 
fuel[138].volume = volume7[fuel7] 
fuel[139].volume = volume7[fuel7] 

fuel[140].volume = volume8[fuel8] 
fuel[141].volume = volume8[fuel8] 
fuel[142].volume = volume8[fuel8] 
fuel[143].volume = volume8[fuel8] 
fuel[144].volume = volume8[fuel8] 
fuel[145].volume = volume8[fuel8] 
fuel[146].volume = volume8[fuel8] 
fuel[147].volume = volume8[fuel8] 
fuel[148].volume = volume8[fuel8] 
fuel[149].volume = volume8[fuel8] 
fuel[150].volume = volume8[fuel8] 
fuel[151].volume = volume8[fuel8] 
fuel[152].volume = volume8[fuel8] 
fuel[153].volume = volume8[fuel8] 
fuel[154].volume = volume8[fuel8] 
fuel[155].volume = volume8[fuel8] 
fuel[156].volume = volume8[fuel8] 
fuel[157].volume = volume8[fuel8] 
fuel[158].volume = volume8[fuel8] 
fuel[159].volume = volume8[fuel8] 

fuel[160].volume = volume1[fuel1]
fuel[161].volume = volume1[fuel1]
fuel[162].volume = volume1[fuel1]
fuel[163].volume = volume1[fuel1]
fuel[164].volume = volume1[fuel1]
fuel[165].volume = volume1[fuel1]
fuel[166].volume = volume1[fuel1]
fuel[167].volume = volume1[fuel1]
fuel[168].volume = volume1[fuel1]
fuel[169].volume = volume1[fuel1]
fuel[170].volume = volume1[fuel1]
fuel[171].volume = volume1[fuel1]
fuel[172].volume = volume1[fuel1]
fuel[173].volume = volume1[fuel1]
fuel[174].volume = volume1[fuel1]
fuel[175].volume = volume1[fuel1]
fuel[176].volume = volume1[fuel1]
fuel[177].volume = volume1[fuel1]
fuel[178].volume = volume1[fuel1]
fuel[179].volume = volume1[fuel1]
fuel[180].volume = volume1[fuel1]
fuel[181].volume = volume1[fuel1]
fuel[182].volume = volume1[fuel1]
fuel[183].volume = volume1[fuel1]
fuel[184].volume = volume1[fuel1]
fuel[185].volume = volume1[fuel1]
fuel[186].volume = volume1[fuel1]
fuel[187].volume = volume1[fuel1]
fuel[188].volume = volume1[fuel1]
fuel[189].volume = volume1[fuel1]

fuel[190].volume = volume2[fuel2]
fuel[191].volume = volume2[fuel2]
fuel[192].volume = volume2[fuel2]
fuel[193].volume = volume2[fuel2]
fuel[194].volume = volume2[fuel2]
fuel[195].volume = volume2[fuel2]
fuel[196].volume = volume2[fuel2]
fuel[197].volume = volume2[fuel2]
fuel[198].volume = volume2[fuel2]
fuel[199].volume = volume2[fuel2]
fuel[200].volume = volume2[fuel2]
fuel[201].volume = volume2[fuel2]
fuel[202].volume = volume2[fuel2]
fuel[203].volume = volume2[fuel2]
fuel[204].volume = volume2[fuel2]
fuel[205].volume = volume2[fuel2]
fuel[206].volume = volume2[fuel2]
fuel[207].volume = volume2[fuel2]
fuel[208].volume = volume2[fuel2]
fuel[209].volume = volume2[fuel2]
fuel[210].volume = volume2[fuel2]
fuel[211].volume = volume2[fuel2]
fuel[212].volume = volume2[fuel2]
fuel[213].volume = volume2[fuel2]
fuel[214].volume = volume2[fuel2]
fuel[215].volume = volume2[fuel2]
fuel[216].volume = volume2[fuel2]
fuel[217].volume = volume2[fuel2]
fuel[218].volume = volume2[fuel2]
fuel[219].volume = volume2[fuel2]

fuel[220].volume = volume3[fuel3]
fuel[221].volume = volume3[fuel3]
fuel[222].volume = volume3[fuel3]
fuel[223].volume = volume3[fuel3]
fuel[224].volume = volume3[fuel3]
fuel[225].volume = volume3[fuel3]
fuel[226].volume = volume3[fuel3]
fuel[227].volume = volume3[fuel3]
fuel[228].volume = volume3[fuel3]
fuel[229].volume = volume3[fuel3]
fuel[230].volume = volume3[fuel3]
fuel[231].volume = volume3[fuel3]
fuel[232].volume = volume3[fuel3]
fuel[233].volume = volume3[fuel3]
fuel[234].volume = volume3[fuel3]
fuel[235].volume = volume3[fuel3]
fuel[236].volume = volume3[fuel3]
fuel[237].volume = volume3[fuel3]
fuel[238].volume = volume3[fuel3]
fuel[239].volume = volume3[fuel3]
fuel[240].volume = volume3[fuel3]
fuel[241].volume = volume3[fuel3]
fuel[242].volume = volume3[fuel3]
fuel[243].volume = volume3[fuel3]
fuel[244].volume = volume3[fuel3]
fuel[245].volume = volume3[fuel3]
fuel[246].volume = volume3[fuel3]
fuel[247].volume = volume3[fuel3]
fuel[248].volume = volume3[fuel3]
fuel[249].volume = volume3[fuel3]

fuel[250].volume = volume4[fuel4]
fuel[251].volume = volume4[fuel4]
fuel[252].volume = volume4[fuel4]
fuel[253].volume = volume4[fuel4]
fuel[254].volume = volume4[fuel4]
fuel[255].volume = volume4[fuel4]
fuel[256].volume = volume4[fuel4]
fuel[257].volume = volume4[fuel4]
fuel[258].volume = volume4[fuel4]
fuel[259].volume = volume4[fuel4]
fuel[260].volume = volume4[fuel4]
fuel[261].volume = volume4[fuel4]
fuel[262].volume = volume4[fuel4]
fuel[263].volume = volume4[fuel4]
fuel[264].volume = volume4[fuel4]
fuel[265].volume = volume4[fuel4]
fuel[266].volume = volume4[fuel4]
fuel[267].volume = volume4[fuel4]
fuel[268].volume = volume4[fuel4]
fuel[269].volume = volume4[fuel4]
fuel[270].volume = volume4[fuel4]
fuel[271].volume = volume4[fuel4]
fuel[272].volume = volume4[fuel4]
fuel[273].volume = volume4[fuel4]
fuel[274].volume = volume4[fuel4]
fuel[275].volume = volume4[fuel4]
fuel[276].volume = volume4[fuel4]
fuel[277].volume = volume4[fuel4]
fuel[278].volume = volume4[fuel4]
fuel[279].volume = volume4[fuel4]

fuel[280].volume = volume5[fuel5]
fuel[281].volume = volume5[fuel5]
fuel[282].volume = volume5[fuel5]
fuel[283].volume = volume5[fuel5]
fuel[284].volume = volume5[fuel5]
fuel[285].volume = volume5[fuel5]
fuel[286].volume = volume5[fuel5]
fuel[287].volume = volume5[fuel5]
fuel[288].volume = volume5[fuel5]
fuel[289].volume = volume5[fuel5]
fuel[290].volume = volume5[fuel5]
fuel[291].volume = volume5[fuel5]
fuel[292].volume = volume5[fuel5]
fuel[293].volume = volume5[fuel5]
fuel[294].volume = volume5[fuel5]
fuel[295].volume = volume5[fuel5]
fuel[296].volume = volume5[fuel5]
fuel[297].volume = volume5[fuel5]
fuel[298].volume = volume5[fuel5]
fuel[299].volume = volume5[fuel5]
fuel[300].volume = volume5[fuel5]
fuel[301].volume = volume5[fuel5]
fuel[302].volume = volume5[fuel5]
fuel[303].volume = volume5[fuel5]
fuel[304].volume = volume5[fuel5]
fuel[305].volume = volume5[fuel5]
fuel[306].volume = volume5[fuel5]
fuel[307].volume = volume5[fuel5]
fuel[308].volume = volume5[fuel5]
fuel[309].volume = volume5[fuel5]

fuel[310].volume = volume6[fuel6]
fuel[311].volume = volume6[fuel6]
fuel[312].volume = volume6[fuel6]
fuel[313].volume = volume6[fuel6]
fuel[314].volume = volume6[fuel6]
fuel[315].volume = volume6[fuel6]
fuel[316].volume = volume6[fuel6]
fuel[317].volume = volume6[fuel6]
fuel[318].volume = volume6[fuel6]
fuel[319].volume = volume6[fuel6]
fuel[320].volume = volume6[fuel6]
fuel[321].volume = volume6[fuel6]
fuel[322].volume = volume6[fuel6]
fuel[323].volume = volume6[fuel6]
fuel[324].volume = volume6[fuel6]
fuel[325].volume = volume6[fuel6]
fuel[326].volume = volume6[fuel6]
fuel[327].volume = volume6[fuel6]
fuel[328].volume = volume6[fuel6]
fuel[329].volume = volume6[fuel6]
fuel[330].volume = volume6[fuel6]
fuel[331].volume = volume6[fuel6]
fuel[332].volume = volume6[fuel6]
fuel[333].volume = volume6[fuel6]
fuel[334].volume = volume6[fuel6]
fuel[335].volume = volume6[fuel6]
fuel[336].volume = volume6[fuel6]
fuel[337].volume = volume6[fuel6]
fuel[338].volume = volume6[fuel6]
fuel[339].volume = volume6[fuel6]

fuel[340].volume = volume7[fuel7]
fuel[341].volume = volume7[fuel7]
fuel[342].volume = volume7[fuel7]
fuel[343].volume = volume7[fuel7]
fuel[344].volume = volume7[fuel7]
fuel[345].volume = volume7[fuel7]
fuel[346].volume = volume7[fuel7]
fuel[347].volume = volume7[fuel7]
fuel[348].volume = volume7[fuel7]
fuel[349].volume = volume7[fuel7]
fuel[350].volume = volume7[fuel7]
fuel[351].volume = volume7[fuel7]
fuel[352].volume = volume7[fuel7]
fuel[353].volume = volume7[fuel7]
fuel[354].volume = volume7[fuel7]
fuel[355].volume = volume7[fuel7]
fuel[356].volume = volume7[fuel7]
fuel[357].volume = volume7[fuel7]
fuel[358].volume = volume7[fuel7]
fuel[359].volume = volume7[fuel7]
fuel[360].volume = volume7[fuel7]
fuel[361].volume = volume7[fuel7]
fuel[362].volume = volume7[fuel7]
fuel[363].volume = volume7[fuel7]
fuel[364].volume = volume7[fuel7]
fuel[365].volume = volume7[fuel7]
fuel[366].volume = volume7[fuel7]
fuel[367].volume = volume7[fuel7]
fuel[368].volume = volume7[fuel7]
fuel[369].volume = volume7[fuel7]

fuel[370].volume = volume8[fuel8]
fuel[371].volume = volume8[fuel8]
fuel[372].volume = volume8[fuel8]
fuel[373].volume = volume8[fuel8]
fuel[374].volume = volume8[fuel8]
fuel[375].volume = volume8[fuel8]
fuel[376].volume = volume8[fuel8]
fuel[377].volume = volume8[fuel8]
fuel[378].volume = volume8[fuel8]
fuel[379].volume = volume8[fuel8]
fuel[380].volume = volume8[fuel8]
fuel[381].volume = volume8[fuel8]
fuel[382].volume = volume8[fuel8]
fuel[383].volume = volume8[fuel8]
fuel[384].volume = volume8[fuel8]
fuel[385].volume = volume8[fuel8]
fuel[386].volume = volume8[fuel8]
fuel[387].volume = volume8[fuel8]
fuel[388].volume = volume8[fuel8]
fuel[389].volume = volume8[fuel8]
fuel[390].volume = volume8[fuel8]
fuel[391].volume = volume8[fuel8]
fuel[392].volume = volume8[fuel8]
fuel[393].volume = volume8[fuel8]
fuel[394].volume = volume8[fuel8]
fuel[395].volume = volume8[fuel8]
fuel[396].volume = volume8[fuel8]
fuel[397].volume = volume8[fuel8]
fuel[398].volume = volume8[fuel8]
fuel[399].volume = volume8[fuel8]


# In[28]:


model = openmc.model.Model(geometry= geometry, settings=settings)
#model.run()


import openmc.deplete
operator = openmc.deplete.Operator(geometry,settings ,"./chain_casl_sfr.xml")

#time_steps = [60*60*24*30]*12
power = 6.0e8


'''
step1_1 = 7*24*60*60
step1_2 = 30*24*60*60
step1_3 = 182.5*24*60*60

step_1 = 365*24*60*60
step_2 = 365.25*24*60*60
step_3 = 365.25*24*60*60
step_4 = 365.25*24*60*60
step_5 = 365.25*24*60*60


time_steps = [step1_1, step1_2, step1_3, step_1]
#,step_2,step_3,step_4,step_5

'''
###########################################################################################################################################################################
######################################################################STEP TAHUN UNTUK DEPLESI#############################################################################
###########################################################################################################################################################################
'''
step1_1 = 7*24*60*60
step1_2 = 30*24*60*60
step1_3 = 60*24*60*60
step1_4 = 90*24*60*60
step1_5 =180*24*60*60
'''

step_1 = 365*24*60*60
step_2 = 365*24*60*60
step_3 = 365*24*60*60
step_4 = 365*24*60*60
step_5 = 365*24*60*60
step_6 = 365*24*60*60
step_7 = 365*24*60*60
step_8 = 365*24*60*60
step_9 = 365*24*60*60
step_10 = 365*24*60*60
step_11 = 365*24*60*60
step_12 = 365*24*60*60
step_13 = 365*24*60*60
step_14 = 365*24*60*60
step_15 = 365*24*60*60
step_16 = 365*24*60*60
step_17 = 365*24*60*60
step_18 = 365*24*60*60
step_19 = 365*24*60*60
step_20 = 365*24*60*60
step_21 = 365*24*60*60
step_22 = 365*24*60*60
step_23 = 365*24*60*60
step_24 = 365*24*60*60
step_25 = 365*24*60*60
step_26 = 365*24*60*60
step_27 = 365*24*60*60
step_28 = 365*24*60*60
step_29 = 365*24*60*60
step_30 = 365*24*60*60
step_31 = 365*24*60*60
step_32 = 365*24*60*60
step_33 = 365*24*60*60
step_34 = 365*24*60*60
step_35 = 365*24*60*60
step_36 = 365*24*60*60
step_37 = 365*24*60*60
step_38 = 365*24*60*60
step_39 = 365*24*60*60
step_40 = 365*24*60*60
step_41 = 365*24*60*60
step_42 = 365*24*60*60
step_43 = 365*24*60*60
step_44 = 365*24*60*60
step_45 = 365*24*60*60
step_46 = 365*24*60*60
step_47 = 365*24*60*60
step_48 = 365*24*60*60
step_49 = 365*24*60*60
step_50 = 365*24*60*60

step_51 = 365*24*60*60
step_52 = 365*24*60*60
step_53 = 365*24*60*60
step_54 = 365*24*60*60
step_55 = 365*24*60*60
step_56 = 365*24*60*60
step_57 = 365*24*60*60
step_58 = 365*24*60*60
step_59 = 365*24*60*60
step_60 = 365*24*60*60
time_steps = [step_1,step_2,step_3,step_4,step_5,step_6,step_7,step_8,step_9,step_10,
step_11,step_12,step_13,step_14,step_15,step_16,step_17,step_18,step_19,step_20,     
step_21,step_22,step_23,step_24,step_25,step_26,step_27,step_28,step_29,step_30,
step_31,step_32,step_33,step_34,step_35,step_36,step_37,step_38,step_39,step_40,
step_41,step_42,step_43,step_44,step_45,step_46,step_47,step_48,step_49,step_50,
step_51,step_52,step_53,step_54,step_55,step_56,step_57,step_58,step_59,step_60]



zmin, zmax, radius = -H/2, H/2, D/2

energy_filter = openmc.EnergyFilter([1,10e6])
u_filter = openmc.UniverseFilter(root)

mesh = openmc.RegularMesh()
mesh.dimension = [1, 200, 200]
mesh.lower_left = [-250,-250,-250]
mesh.lower_right = [250,250,250]
mesh.width = [200,200,200]
mesh_filter = openmc.MeshFilter(mesh)

tally_mesh = openmc.Tally()
tally_mesh.filters = [mesh_filter]
tally_mesh.scores = ['fission']

legendre_filter = openmc.SpatialLegendreFilter(10,'z', zmin, zmax)

zernike_filter = openmc.ZernikeFilter(order=10,x=0,y=0,r=radius)
zer_radial_filter = openmc.ZernikeRadialFilter(order=10,x=0,y=0,r=radius) #disini tinggal tambah radial

fis_tally_legendre = openmc.Tally(name = 'fission tally legendre')
fis_tally_legendre.scores = ['fission']
fis_tally_legendre.filters = [u_filter, legendre_filter, energy_filter]

fis_tally_zernike_radial = openmc.Tally(name = 'fission tally zernike radial')
fis_tally_zernike_radial.scores = ['fission']
fis_tally_zernike_radial.filters = [u_filter, zer_radial_filter, energy_filter]


flux_leg = openmc.Tally(name = 'flux tally legendre')
flux_leg.scores = ['flux']
flux_leg.filters = [u_filter, legendre_filter, energy_filter]

flux_zr = openmc.Tally(name = 'flux tally zernike radial')
flux_zr.scores = ['flux']
flux_zr.filters = [u_filter, zer_radial_filter, energy_filter]

heating_tally = openmc.Tally(name = 'heating tally')
heating_tally.scores = ['heating']
heating_tally.filters = [u_filter, energy_filter]

tallies = openmc.Tallies([tally_mesh, fis_tally_legendre, fis_tally_zernike_radial, flux_leg, flux_zr, heating_tally])
tallies.export_to_xml()




integrator = openmc.deplete.PredictorIntegrator(operator, time_steps, power)
integrator.integrate()
