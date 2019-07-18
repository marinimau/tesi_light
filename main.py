#
#   Author: Mauro Marini
#   Project: tesi
#   main.py
#
from data_testing.run_test_in_parallel import Run
from feature_vector.generate_feature_vector import FeatureVectorGenerator
from data_manager.data_prefab import DataPrefab

run_test = False
generate_feature_vector = True

dataset = DataPrefab.generate_data_from_entire_sample(DataPrefab())


if run_test:
    Run.run_in_parallel(Run(dataset))
if generate_feature_vector:
    FeatureVectorGenerator.generate(FeatureVectorGenerator(dataset))