# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from marshmallow import Schema, fields, post_load

from polyaxon_schemas.base import BaseConfig, BaseMultiSchema
from polyaxon_schemas.utils import ObjectOrListObject


class GlobalStepWaiterHookSchema(Schema):
    wait_until_step = fields.Int()

    class Meta:
        ordered = True

    @post_load
    def make_load(self, data):
        return GlobalStepWaiterHookConfig(**data)


class GlobalStepWaiterHookConfig(BaseConfig):
    IDENTIFIER = 'GlobalStepWaiterHook'
    SCHEMA = GlobalStepWaiterHookSchema

    def __init__(self, wait_until_step):
        self.wait_until_step = wait_until_step


class FinalOpsHookSchema(Schema):
    final_ops = ObjectOrListObject(fields.Str)

    class Meta:
        ordered = True

    @post_load
    def make_load(self, data):
        return FinalOpsHookConfig(**data)


class FinalOpsHookConfig(BaseConfig):
    IDENTIFIER = 'FinalOpsHook'
    SCHEMA = FinalOpsHookSchema

    def __init__(self, final_ops):
        self.final_ops = final_ops


class StepLoggingTensorHookSchema(Schema):
    tensors = ObjectOrListObject(fields.Str)
    every_n_iter = fields.Int(allow_none=True)
    every_n_secs = fields.Int(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make_load(self, data):
        return StepLoggingTensorHookConfig(**data)


class StepLoggingTensorHookConfig(BaseConfig):
    IDENTIFIER = 'StepLoggingTensorHook'
    SCHEMA = StepLoggingTensorHookSchema

    def __init__(self, tensors, every_n_iter=None, every_n_secs=None):
        self.tensors = tensors
        self.every_n_iter = every_n_iter
        self.every_n_secs = every_n_secs


class EpisodeLoggingTensorHookSchema(Schema):
    tensors = ObjectOrListObject(fields.Str)
    every_n_episodes = fields.Int()

    class Meta:
        ordered = True

    @post_load
    def make_load(self, data):
        return EpisodeLoggingTensorHookConfig(**data)


class EpisodeLoggingTensorHookConfig(BaseConfig):
    IDENTIFIER = 'EpisodeLoggingTensorHook'
    SCHEMA = EpisodeLoggingTensorHookSchema

    def __init__(self, tensors, every_n_episodes):
        self.tensors = tensors
        self.every_n_episodes = every_n_episodes


class HookSchema(BaseMultiSchema):
    __multi_schema_name__ = 'loss'
    __configs__ = {
        GlobalStepWaiterHookConfig.IDENTIFIER: GlobalStepWaiterHookConfig,
        FinalOpsHookConfig.IDENTIFIER: FinalOpsHookConfig,
        StepLoggingTensorHookConfig.IDENTIFIER: StepLoggingTensorHookConfig,
        EpisodeLoggingTensorHookConfig.IDENTIFIER: EpisodeLoggingTensorHookConfig,
    }
