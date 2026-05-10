import scanpy as sc

def preprocess(adata):

    # Filter cells
    sc.pp.filter_cells(adata, min_genes=200)

    # Filter genes
    sc.pp.filter_genes(adata, min_cells=3)

    # Normalize
    sc.pp.normalize_total(adata, target_sum=1e4)

    # Log transform
    sc.pp.log1p(adata)

    return adata