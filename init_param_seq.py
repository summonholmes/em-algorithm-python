def init_param_seq(fasta_file_seq, len_list):
	len_seq = []
	for i in range(len_list):
		len_seq.append(len(fasta_file_seq[i]))
	# print("Length of all sequences: ", len_seq)
	return len_seq
