
def seq_check(sequence):
    seq = ""
    seq_tem = ""
    seq_l = []

    for i in sequence:
        if i == seq_tem[-1:]:
            seq_tem += i
        else:
            seq_tem = i
        if len(seq_tem) > len(seq):
            seq = seq_tem
            seq_l = [seq]
        elif len(seq_tem) == len(seq):
            seq_l.append(seq_tem)

    return seq_l


