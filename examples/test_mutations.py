import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from mutation_tracker import classify_mutations_cds
from orf_finder import translate_dna
from activity_score import compute_activity_scores


# WT CDS
wt_cds = "ATG" + "GCT"*5 + "TTC"*5

# Variant CDS
var_cds = "ATG" + "GCC" + "GCT"*4 + "TTC"*4 + "TAC"

print("WT protein:", translate_dna(wt_cds))
print("VAR protein:", translate_dna(var_cds))

generation = 1

# Mutation tracker
result = classify_mutations_cds(wt_cds, var_cds, generation)

print("\nSynonymous count:", result["syn_count"])
print("Non-synonymous count:", result["nonsyn_count"])
print("Mutation count:", result["mutation_count"])

print("\nMutation records:")
for m in result["mutation_records"]:
    print(m)

# Activity score
wt_dna_yield = 100.0
wt_protein_yield = 50.0

variant_dna_yield = 120.0
variant_protein_yield = 50.0

activity = compute_activity_scores(
    dna_yield=variant_dna_yield,
    protein_yield=variant_protein_yield,
    wt_dna_yield=wt_dna_yield,
    wt_protein_yield=wt_protein_yield
)

print("\nActivity score results:")
print(activity)