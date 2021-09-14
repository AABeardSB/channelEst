# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:57:00 2020

@author: AB Intern Ashley
"""
import numpy as np



# sigmoidal fucntion
def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))    # Use sigmoid fn. as the activation fn.

# hyperbolic tangent function
def nonlin2(x,deriv=False):
    if(deriv==True):
        return 1 - np.tanh(x)**2
    
    return np.tanh(x)



#############################End Function####################
def getdata(file_num):
    #Now do this for all files
    set_array = []
    filename = "C:\\Users\\AB Intern Ashley\\OneDrive - SPECTRUMBULLPEN\\Shared Python\\Gen_files_w_noise\\Feature_List_" + str(file_num) + ".txt" #Change to your location of data files
    data = np.fromfile(filename, dtype="float32")   #Construct an array from data in a binary file
    data = data[0::2] + 1j*data[1::2]               #Construct interleaved I/Q data into complex array
    
    #Starting at 1st set of 1024, this averages five complex sets of 1024 for each input for a total of 10 input sets.
    # Each input set is multiplied by its complex conjugate to give real number aka norm of complex set.
    sample1 = (data[0:1024]+data[1025:2049]+data[2050:3074]+data[3075:4099]+data[4100:5124]) # average of complex set
    set1 = (1/100.0)*sample1 * (np.conj(data[0:1024])+np.conj(data[1025:2049])+np.conj(data[2050:3074])+np.conj(data[3075:4099])+np.conj(data[4100:5124]))   # norm
    set1 = set1.real # drop the zero imaginary component
    
    sample2 = (data[5125:6149]+data[6150:7174]+data[7175:8199]+data[8200:9224]+data[9225:10249])
    set2 = (1/100.0)*sample2 * (np.conj(data[5125:6149])+np.conj(data[6150:7174])+np.conj(data[7175:8199])+np.conj(data[8200:9224])+np.conj(data[9225:10249]))
    set2 = set2.real # drop the zero imaginary component
    
    sample3 = (data[10250:11274]+data[11275:12299]+data[12300:13324]+data[13325:14349]+data[14350:15374])
    set3 = (1/100.0)*sample3 * (np.conj(data[10250:11274])+np.conj(data[11275:12299])+np.conj(data[12300:13324])+np.conj(data[13325:14349])+np.conj(data[14350:15374]))
    set3 = set3.real # drop the zero imaginary component
    
    sample4 = (data[15375:16399]+data[16400:17424]+data[17425:18449]+data[18450:19474]+data[19475:20499])
    set4 = (1/100.0)*sample4 * (np.conj(data[15375:16399])+np.conj(data[16400:17424])+np.conj(data[17425:18449])+np.conj(data[18450:19474])+np.conj(data[19475:20499]))
    set4 = set4.real # drop the zero imaginary component
    
    sample5 = (data[20500:21524]+data[21525:22549]+data[22550:23574]+data[23575:24599]+data[24600:25624])
    set5 = (1/100.0)*sample5 * (np.conj(data[20500:21524])+np.conj(data[21525:22549])+np.conj(data[22550:23574])+np.conj(data[23575:24599])+np.conj(data[24600:25624]))
    set5 = set5.real # drop the zero imaginary component
    
    sample6 = (data[25625:26649]+data[26650:27674]+data[27675:28699]+data[28700:29724]+data[29725:30749])
    set6 = (1/100.0)*sample6 * (np.conj(data[25625:26649])+np.conj(data[26650:27674])+np.conj(data[27675:28699])+np.conj(data[28700:29724])+np.conj(data[29725:30749]))
    set6 = set6.real # drop the zero imaginary component
    
    sample7 = (data[30750:31774]+data[31775:32799]+data[32800:33824]+data[33825:34849]+data[34850:35874])
    set7 = (1/100.0)*sample7 * (np.conj(data[30750:31774])+np.conj(data[31775:32799])+np.conj(data[32800:33824])+np.conj(data[33825:34849])+np.conj(data[34850:35874]))
    set7 = set7.real # drop the zero imaginary component
    
    sample8 = (data[35875:36899]+data[36900:37924]+data[37925:38949]+data[38950:39974]+data[39975:40999])
    set8 = (1/100.0)*sample8 * (np.conj(data[35875:36899])+np.conj(data[36900:37924])+np.conj(data[37925:38949])+np.conj(data[38950:39974])+np.conj(data[39975:40999]))
    set8 = set8.real # drop the zero imaginary component
    
    sample9 = (data[41000:42024]+data[42025:43049]+data[43050:44074]+data[44075:45099]+data[45100:46124])
    set9 = (1/100.0)*sample9 * (np.conj(data[41000:42024])+np.conj(data[42025:43049])+np.conj(data[43050:44074])+np.conj(data[44075:45099])+np.conj(data[45100:46124]))
    set9 = set9.real # drop the zero imaginary component

    sample10 = (data[46125:47149]+data[47150:48174]+data[48175:49199]+data[49200:50224]+data[50225:51249])
    set10 = (1/100.0)*sample10 * (np.conj(data[46125:47149])+np.conj(data[47150:48174])+np.conj(data[48175:49199])+np.conj(data[49200:50224])+np.conj(data[50225:51249]))
    set10 = set10.real # drop the zero imaginary component
    
    #Concatenate the sample arrays Row-wise so we have a vertical array of file samples
    set_mean = [0 for x in range(1024)]
    set_std = [0 for x in range(1024)]
    set_var = [0 for x in range(1024)]
    set_max = [0 for x in range(1024)]
    for i in range(1024):
        set_mean[i] = np.mean([set1[i],set2[i],set3[i],set4[i],set5[i],set6[i],set7[i],set8[i],set9[i],set10[i]])
        set_var[i] = np.var([set1[i],set2[i],set3[i],set4[i],set5[i],set6[i],set7[i],set8[i],set9[i],set10[i]])
        set_std[i] = np.std([set1[i],set2[i],set3[i],set4[i],set5[i],set6[i],set7[i],set8[i],set9[i],set10[i]])
        set_max[i] = np.max([set1[i],set2[i],set3[i],set4[i],set5[i],set6[i],set7[i],set8[i],set9[i],set10[i]])
    # End for loop
    set_array = np.vstack((set1,set2,set3,set4,set5,set6,set7,set8,set9,set10,set_mean,set_var,set_std,set_max,np.ones((1,1024))))  

    # Concatenate to the end of input array: Used as extra data features
    #Mean is to help find the noise floor of the data & differentiate it from the signal peaks @ the correct frequency.
    # ones added for convention
    return set_array

#########################End function########################

def remove_cuft(s):
        #used to remove 0[..] from list
    return s[1:]

    
def getteach(file_num):

    filename = "C:\\Users\\AB Intern Ashley\\OneDrive - SPECTRUMBULLPEN\\Shared Python\\Gen_files_w_noise\\Teach_" + str(file_num) + ".txt" #Change to your location of teaching files

    teach=np.loadtxt(filename,delimiter=',', skiprows=1)
    
    new_teach = [0 for j in range(10)]
    freq_list = [2.412E9,2.417E9,2.422E9,2.427E9,2.432E9,2.437E9,2.442E9,2.447E9,2.452E9,2.462E9]                #list of all 2.4Ghz wifi center freqs # was kHz before?
    for i in range(5):
        for k in range(10):
            if teach[i] == freq_list[k]:
                new_teach[k] = 1            # designates a used channel for that frequency spot, else for open channel = 0
    # End for loop
    new_teach = np.append(new_teach,[0,0,0,0,0])
    new_teach = np.reshape(new_teach, (15,1))
    

    
    print("Teaching frequency list " + str(file_num) + ": " + str(new_teach))

    return new_teach

######################End function###########################

taining_runs=1000
inspection_views = taining_runs / taining_runs*10
data_set_size=140
learning_rate = .0001

# Sample data for debugging:
#
#X = np.array([[0+0j,0+0j,0-1j],
#            [0+0j,0-1j,1+0j],
#            [0+1j,0+0j,0+1j],
#            [1+0j,1+0j,1+0j]])
#                
#y = np.array([[0],
#			      [1],
#			      [1],
#			      [0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((1024,15))-1  #+ .1j   # Size of input: (1024,15), Orig: 3,4
syn1 = 2*np.random.random((15,1000))-1
syn2 = 2*np.random.random((1000,15))-1
syn3 = 2*np.random.random((15,1)) -1 #+ .1j  # Size of output: (15,1), Orig: 4,1



for data_index in range(data_set_size):
    
    # Build arrays from data
    X = getdata(data_index)  # Get a new set of 15,1024 from one I/Q data file for each iteration
    Y = getteach(data_index)# Get a new set of 1,15 from one teach file for each iteration of validation

    
    for j in range(taining_runs):

        #Feed forward through layers 0, 1, and 2
        l0 = X
        l1 = nonlin(np.dot(l0,syn0))
        l2 = nonlin(np.dot(l1,syn1))
        l3 = nonlin(np.dot(l2,syn2))
        l4 = nonlin(np.dot(l3,syn3))

        # how much did we miss the target value?
        l4_error = np.subtract(Y,l4)

        if (j% inspection_views) == 0:
            print ("Error:" + str(np.mean(np.square((l4_error)))))
        # End if
    
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        l4_delta = np.multiply(l4_error,nonlin(l4,deriv=True))

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        l3_error = l4_delta.dot(syn3.T)
        l3_delta = learning_rate*(l3_error * nonlin(l3,deriv=True))
        
        l2_error = l3_delta.dot(syn2.T)
        l2_delta = learning_rate*(l2_error * nonlin(l2,deriv=True))
        
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = learning_rate*(l1_error * nonlin(l1,deriv=True))
        
        syn3 += np.dot(l3.T,l4_delta)
        syn2 += np.dot(l2.T,l3_delta)
        syn1 += np.dot(l1.T,l2_delta)
        syn0 += np.dot(l0.T,l1_delta)
        
    # End for loop
# End for loop

print(syn0)
print(syn1)
print(syn2)
print(syn3)

