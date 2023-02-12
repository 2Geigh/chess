class piece:
    def __init__(self)

class amino_acid:
    def __init__(self, dna_codon:str, name:str, has_polar_property:bool, has_acidity_propery:bool, is_polar = False, is_acidic = False):
        """
        Creates an amino acid object.
        is_it_polar == True if the amino acid is polar, False otherwise.
        acidity == True if the amino acid is acidic, False if basic.
        """
        self.dna_codon = dna_codon
        self.rna_codon = transcribe(dna_codon)
        self.name = name
        if has_polar_property:
            self.is_polar = is_polar
        elif has_acidity_propery:
            self.is_acidic = is_acidic 