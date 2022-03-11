def fasta_read(file):
    """
    :param file: FASTA FILE
    :return: DICTIONARY WITH SEQUENCE TAGS AS KEYS AND SEQUENCES AS VALUES
    """
    with open(file) as f:
        file_raw = f.read().split()
        ros = [line for line in file_raw if '>' in line]
        file_edit = []
        for index, seq in enumerate(file_raw):
            if '>' in seq:
                file_edit.append('b')
            else:
                file_edit.append(seq)
        file_edit = ''.join(file_edit).split('b')[1:]
        file_edit = dict(zip(ros, file_edit))
        return file_edit


