# channelEst
Authors: Ashley Beard
         Steven Sharp
         
Channel Estimator using ML and GNU Radio

This directory contains the GNU Radio and Python scripts used for our paper "Analysis of an Open Channel Identifier using Stochastic Gradient Descent and GNU Radio" submitted to the 11th annual GNU Radio Conferece technical proceedings. 

The 95 GB dataset created for this project is open-access and can be found at this link: https://spectrumbullpen-my.sharepoint.com/:f:/p/ashley_beard/EvJUG5CRVWNIrKl_prhtRIkBoL-HM8oQpVZf1E3Nb9vVVg?e=yywhKt

Below are descriptions of each file included in this directory:

power_estimation.grc: This flowgraph is the base of the script 'test_signal_detector_6.py'. It generates a signal with five randomized-frequency signals and a Gaussian noise source. It transforms the signal into the frequency domain, seperates frequencies into bins, and estimates the signal strength of each frequency section of bandwidth.

data_files_gen.grc: This flowgraph is the base of the script 'data_files_gen_w_noise.py'. It generates a binary data file (in the user's choice of directory) consisting of an approximately one-second stream of five randomized-frequency signals and a Gaussian noise source.

NN_5layer_2.py: This script performs the training phase of the feedforward neural network model in this project. It gives the option of two different cost functions to use: sigmoid or hyperbolic tangent functions. The 'getdata' function reads in the generated dataset and perfoms all the data preproccessing before it is fed into the neural network. The 'getteach' function reads in the teaching labels for each dataset which include the ground-truth 'yes/no' signal labels. The script then defines the hyperparameters, number of training runs, and initial weight values. It then runs the gradient descent and backpropagation functions, printing the training error with each iteration. It then prints the final weights of the neural network. The user must save these weights as numpy files to be fed into the script 'validation_5layer.py'.

data_files_gen_w_noise.py: This Python script is based on the GNU Radio flowgraph 'data_files_gen.grc' with some added code to the main function. It loops through the base flowgraph operations, creating a new numbered data file with a new randomized set of used frequencies each time. This script was used to generate the full dataset used for this project.

test_signal_detector_6.py: This Python script is based off of the GNU Radio flowgraph 'power_estimation.grc' with some added code to the main function. It loops the flowgraph code and uses the estimated signal strength to locate signals in their respective sections of bandwidth. At the end of the specified number of iterations, it compares its estimates to the ground-truth set to calculate a total percent error of its performance.

validation_5layer.py: This script performs the validation/testing phase of the feedforward neural network model in this project. The user feeds in the saved network weights from the training script 'NN_5layer_2.py'. Running the script prints the following arrays in this order: "l4", "Rounded", "Y", "error", "discrepency". "l4" is the raw output of the network, "Rounded" is "l4" rounded to the nearest '0 or 1' expected response, "Y" is the ground-truth labels for each data file, "error" is the difference between "Rounded"-l4 and "Y", "discrepency" is the difference between raw-"l4" and "Y". The last printed value of the script is the final testing percent error of the network.
