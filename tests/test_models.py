# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

from polyaxon_schemas.losses import SoftmaxCrossEntropyConfig, MeanSquaredErrorConfig
from polyaxon_schemas.metrics import StreamingAccuracyConfig, StreamingPrecisionConfig
from polyaxon_schemas.models import (
    BaseModelConfig,
    ClassifierConfig,
    RegressorConfig,
)
from polyaxon_schemas.optimizers import AdamConfig
from tests.utils import assert_equal_graphs, assert_equal_dict


class TestModelConfigs(TestCase):
    @staticmethod
    def assert_equal_models(result_model, expected_model):
        assert_equal_graphs(expected_model.pop('graph'), result_model.pop('graph'))
        assert_equal_dict(result_model, expected_model)

    def test_base_model_config(self):
        config_dict = {
            'graph': {
                'input_layers': ['image'],
                'output_layers': ['dense_0'],
                'layers': [
                    {
                        'Conv2D': {
                            'filters': 64,
                            'strides': [1, 1],
                            'kernel_size': [2, 2],
                            'activation': 'relu',
                            'name': 'convolution_1',
                        }
                    },
                    {'Dense': {'units': 17, 'name': 'dense_0'}}
                ]
            },
            'loss': SoftmaxCrossEntropyConfig(input_layer=['image', 0, 0],
                                              output_layer=['dense_0', 0, 0]).to_schema(),
            'optimizer': AdamConfig(learning_rate=0.01).to_schema(),
            'eval_metrics': [
                StreamingAccuracyConfig(input_layer=['image', 0, 0],
                                        output_layer=['dense_0', 0, 0]).to_schema(),
                StreamingPrecisionConfig(input_layer=['image', 0, 0],
                                         output_layer=['dense_0', 0, 0]).to_schema(),
            ],
            'summaries': ['loss', 'gradients'],
            'clip_gradients': 0.5,
            'clip_embed_gradients': 0.,
            'name': 'model'}
        config = BaseModelConfig.from_dict(config_dict)
        config_to_dict = config.to_dict()
        self.assert_equal_models(config_to_dict, config_dict)

    def test_classifier_model_config(self):
        config_dict = {
            'graph': {
                'input_layers': ['image'],
                'output_layers': ['dense_0'],
                'layers': [
                    {
                        'Conv2D': {
                            'filters': 64,
                            'strides': [1, 1],
                            'kernel_size': [2, 2],
                            'activation': 'relu',
                            'name': 'convolution_1',
                        }
                    },
                    {'Dense': {'units': 17, 'name': 'dense_0'}}
                ]
            },
            'one_hot_encode': True,
            'n_classes': 10,
            'loss': SoftmaxCrossEntropyConfig(['image', 0, 0],
                                              output_layer=['dense_0', 0, 0]).to_schema(),
            'optimizer': AdamConfig(learning_rate=0.01).to_schema(),
            'eval_metrics': [
                StreamingAccuracyConfig(input_layer=['image', 0, 0],
                                        output_layer=['dense_0', 0, 0]).to_schema(),
                StreamingPrecisionConfig(input_layer=['image', 0, 0],
                                         output_layer=['dense_0', 0, 0]).to_schema(),
            ],
            'summaries': ['loss', 'gradients'],
            'clip_gradients': 0.5,
            'clip_embed_gradients': 0.,
            'name': 'model'}
        config = ClassifierConfig.from_dict(config_dict)
        config_to_dict = config.to_dict()
        self.assert_equal_models(config_to_dict, config_dict)

    def test_regressor_model_config(self):
        config_dict = {
            'graph': {
                'input_layers': ['image'],
                'output_layers': ['dense_0'],
                'layers': [
                    {'LSTM': {'units': 5}},
                    {'Dense': {'units': 1, 'name': 'dense_0'}}
                ]
            },
            'loss': MeanSquaredErrorConfig(input_layer=['image', 0, 0],
                                           output_layer=['dense_0', 0, 0]).to_schema(),
            'optimizer': AdamConfig(learning_rate=0.01).to_schema(),
            'eval_metrics': [],
            'summaries': ['loss', 'gradients'],
            'clip_gradients': 0.5,
            'clip_embed_gradients': 0.,
            'name': 'model'}
        config = RegressorConfig.from_dict(config_dict)
        config_to_dict = config.to_dict()
        self.assert_equal_models(config_to_dict, config_dict)
