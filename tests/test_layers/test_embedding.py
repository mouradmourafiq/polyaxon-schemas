# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

from polyaxon_schemas.initializations import UniformInitializerConfig
from polyaxon_schemas.layers.embeddings import EmbeddingConfig

from tests.utils import assert_equal_layers


class TestEmbeddingConfigs(TestCase):
    def test_embedding_config(self):
        config_dict = {
            'input_dim': 100,
            'output_dim': 100,
            'embeddings_initializer': UniformInitializerConfig().to_schema(),
            'embeddings_regularizer': None,
            'activity_regularizer': None,
            'embeddings_constraint': None,
            'mask_zero': False,
            'input_length': None,
        }
        config = EmbeddingConfig.from_dict(config_dict)
        assert_equal_layers(config, config_dict)
