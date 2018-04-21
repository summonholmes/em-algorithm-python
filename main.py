from em_check_exception import check_if_int
from em_input_start import input_start_align, input_start_fasta, input_start_iter
from em_start import start_the_em_prep
from pprint import pprint


def print_start_em():
    print("\nNow preparing for E-M...")
    print(
        "M = Max Motif\nS = Max Score\nP = Max Position\n# = Max Sequence #"\
        "\nSS = Max Sum Scores\n\nPlease be patient..."
    )


def print_results_em(final_motif):
    print("\nDONE!  First horizontal array: max information.")
    print("Vertical arrays: positions, scores, and motifs. ")
    print("\nMAX: Motif\tScore\t Pos\tSeq\tSumScore")
    pprint(final_motif)


def main():
    print("Welcome to my Python implementation of Expectation-Maximization")
    max_bit_score_arr = []
    final_record = []
    motif_width = check_if_int(
        input("Please specify the width of the motif: "))
    user_align = input_start_align()
    user_iter = input_start_iter()
    fasta_file_seq = input_start_fasta()
    print_start_em()
    em_results = start_the_em_prep(max_bit_score_arr, final_record,
                                   motif_width, user_align, user_iter,
                                   fasta_file_seq)
    final_motif = max(em_results, key=lambda item: item[0][4])
    print_results_em(final_motif)


main()