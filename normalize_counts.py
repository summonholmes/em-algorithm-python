# from pprint import pprint


def normalize_counts(motif_width, len_list, count_all_motif_bases):
	for i in range(4):
		for j in range(len_list):
			for k in range(motif_width):
				count_all_motif_bases[i][j][k] += 1
	# print("\nAdjusted counts for motif base postitions: ")
	# pprint(count_all_motif_bases)
	return count_all_motif_bases