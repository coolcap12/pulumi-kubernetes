# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import importlib

# Make subpackages available:
_submodules = [
    'v1alpha1',
    'v1beta1',
]
for pkg in _submodules:
    if pkg != 'config':
        importlib.import_module(f'{__name__}.{pkg}')
