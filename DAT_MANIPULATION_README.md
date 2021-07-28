# Dat Manipulation Code Documentation
The .dat manipulation code (found [here](https://github.com/theCudster/random-projects/blob/python/dat_manipulation.py)) is code to splice .dat files, remove data from .dat files, combine .dat files, and weave .dat files (combine two datasets taken at the same time to make one new dataset with double the channels). 
There are four functions in the dat_manipulation.py file:
### slice_data
This function can be used to slice data from a certain index. It takes 5 parameters:
* original_data_loc: the path to the original data
* slice_index: the index to slice to or to slice from
* start: if true, read all samples until slice_index, otherwise read all samples after slice_index
* new_name: new filename for sliced data (created in the same directory as original_data_loc)
* num_channels: the number of channels in the data provided
### remove_data
This function can be used to remove a certain portion of the data in the dataset. It takes 5 parameters:
* original_data_loc: path to data to be sliced
* slice_index: the index to start removing data from
* end_slice_index: index to stop removing data (non-inclusive)
* new_name: new filename for data w/o removed data (created in the same directory as original_data_loc)
* num_channels: the number of channels in the dataset provided
### combine_data
This function can be used to combine two datasets. The datasets do not necessarily have to have the same amount of channels to function, but the output makes little to no sense if they do not have the same amount of channels. It takes 3 parameters:
* original_data_loc: first dataset location (in a filesystem)
* append_data_loc: second dataset location (in a filesystem)
* new_name: new filename for combined data (created in the same directory as original_data_loc)
### weave_data
This function can be used to combine two datasets as if they were taken at the same time, effectively "weaving" them together. The datasets  have to have the same amount of channels for the code to function, but this could be easily modified with a fifth parameter. They have to have the same amount of samples. It takes 4 parameters:
* file_name_1: first dataset location (in a filesystem)
* file_name_2: second dataset location (in a filesystem)
* new_name: new filename for weaved together data (created in the same directory as file_name_1)
* num_channels: number of channels in the first dataset
***
All code assumes 16-bit integers.
