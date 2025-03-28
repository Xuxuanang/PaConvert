# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

import paddle
from apibase import APIBase


class SpectralNormAPIBase(APIBase):
    def compare(
        self,
        name,
        pytorch_result,
        paddle_result,
        check_value=True,
        check_shape=True,
        check_dtype=True,
        check_stop_gradient=True,
        rtol=1.0e-6,
        atol=0.0,
    ):
        assert isinstance(paddle_result, paddle.nn.Linear)


obj = SpectralNormAPIBase("torch.nn.utils.parametrizations.spectral_norm")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(model)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(model, name="weight")
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(model, name="weight", n_power_iterations=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(model, name="weight", n_power_iterations=1, eps=1e-5, dim=0)
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_4
def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(model, "weight", 1, 1e-5, 0)
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_4
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(module=model, name="weight", n_power_iterations=1, eps=1e-5, dim=0)
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_4
def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.parametrizations.spectral_norm(dim=0, eps=1e-5, n_power_iterations=1, name="weight", module=model)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_alias_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.spectral_norm(dim=0, eps=1e-5, n_power_iterations=1, name="weight", module=model)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_alias_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        model = nn.Linear(10, 20)
        result = torch.nn.utils.spectral_norm(dim=0, eps=1e-5, n_power_iterations=1, name="weight", module=model)
        """
    )
    obj.run(pytorch_code, ["result"])
