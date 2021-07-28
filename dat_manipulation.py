"""
Slice the data at a certain index.
    original_data_loc: path to data to be sliced
    slice_index: the index to slice to or to slice from
    start: if true, read the first slice_index samples, otherwise read all samples after slice_index
    new_name: new filename for sliced data
    num_channels: the number of channels in the dataset provided
"""
def slice_data(original_data_loc, slice_index, start, new_name, num_channels):
    slice_index *= num_channels
    new_name += ".dat"
    if start:
        original_data = open(original_data_loc, mode='rb').read(slice_index * 2)
        new_file = original_data_loc[:original_data_loc.rindex("/") + 1] + new_name
        new_file = open(new_file, 'wb')
        new_file.write(original_data)
        new_file.close()
    else:
        original_data = open(original_data_loc, mode='rb').read()
        original_data = original_data[slice_index * 2:]
        new_file = original_data_loc[:original_data_loc.rindex("/") + 1] + new_name
        new_file = open(new_file, 'wb')
        new_file.write(original_data)
        new_file.close()


"""
Remove a certain portion of the data.
    original_data_loc: path to data to be sliced
    slice_index: the index to start removing data from
    end_slice_index: index to stop removing data (non-inclusive)
    new_name: new filename for data
    num_channels: the number of channels in the dataset provided
"""
def remove_data(original_data_loc, slice_index, end_slice_index, new_name, num_channels):
    slice_index *= int(num_channels * 2)
    end_slice_index *= int(num_channels * 2)
    new_name += ".dat"
    original_data = open(original_data_loc, mode='rb').read()
    original_data = original_data[0:slice_index] + original_data[end_slice_index:]
    new_file = original_data_loc[:original_data_loc.rindex("/") + 1] + new_name
    new_file = open(new_file, 'wb')
    new_file.write(original_data)
    new_file.close()


"""
Append two datasets together.
    original_data_loc: first dataset location
    append_data_loc: second dataset location
    new_name: new filename for combined data
"""
def combine_data(original_data_loc, append_data_loc, new_name):
    new_name += ".dat"
    old_file = open(original_data_loc, mode='rb')
    append_file = open(append_data_loc, mode='rb')
    old_data = old_file.read()
    append_data_loc = append_file.read()
    append_file.close()
    old_file.close()
    new_file = original_data_loc[:original_data_loc.rindex("/") + 1] + new_name
    new_file = open(new_file, 'wb')
    new_file.write(old_data)
    new_file.write(append_data_loc)
    new_file.close()


"""
Add two probe datasets together. (double channel count with same timestamps)
    file_name_1: first dataset location
    file_name_2: second dataset location
    new_name: new filename for weaved together data
    num_channels: number of channels to 
"""
def weave_data(file_name_1, file_name_2, new_name, num_channels):
    new_name += ".dat"
    old_file = open(file_name_1, mode='rb')
    append_file = open(file_name_2, mode='rb')
    old_data = old_file.read()
    added_data = append_file.read()
    append_file.close()
    old_file.close()
    if len(old_data) != len(added_data):
        print("Error: files not same size.")
        return
    new_file = file_name_1[:file_name_1.rindex("/") + 1] + new_name
    new_file = open(new_file, 'wb')
    num_entries = int(len(old_data) / (2 * num_channels))
    for i in range(num_entries):
        first_data = old_data[i * (2 * num_channels):i * (2 * num_channels) + 2 * num_channels]
        second_data = added_data[i * (2 * num_channels):i * (2 * num_channels) + 2 * num_channels]
        new_file.write(first_data)
        new_file.write(second_data)
    new_file.close()


if __name__ == "__main__":
    # sample 10-second dataset
    file_loc = "/home/wufan/Downloads/10sec.dat"
    # first 200000 samples of dataset
    slice_data(file_loc, 100000, True, "10secFirst200k", 32)
    # weave two datasets together, although in this case it's just two of the same dataset
    weave_data(file_loc, file_loc, "10secWeaved", 32)
    # combine two datasets together, in this case have the same data twice in one file
    combine_data(file_loc, file_loc, "10secAppended")
    # remove values 100000-120000
    remove_data(file_loc, 100000, 120000, "10secRemoved", 32)
