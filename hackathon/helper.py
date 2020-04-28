# Copyright 2020 Toyota Research Institute

from camd.analysis import AnalyzerBase
from matminer.datasets.convenience_loaders import load_elastic_tensor


class SimpleAnalyzer(AnalyzerBase):
    def __init__(self):
        pass

    def analyze(self, new_experiment_data, seed_data):
        pass


def load_tutorial_data():
    """
    Helper function to load tutorial data, loads
    the elastic tensor data from the MatMiner/MP API
    drops columns and renames the VRH K and G to
    bulk and shear modulus, rounds to 1 decimal
    point, and sets the index to the material id
    """
    data = load_elastic_tensor()
    data = data.drop(
        [
            'nsites',
            # 'space_group',
            'elastic_anisotropy',
            'structure',
            'volume',
            'G_Voigt',
            'G_Reuss',
            'K_Voigt',
            'K_Reuss',
            'compliance_tensor',
            'elastic_tensor',
            'elastic_tensor_original',
            'poisson_ratio'
        ],
        axis=1
    )
    data = data.rename(
        {
            "K_VRH": "bulk_modulus",
            "G_VRH": "shear_modulus"
        },
        axis='columns'
    )
    data = data.round(1)
    data = data.set_index('material_id')
    return data
