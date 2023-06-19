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
#

import textwrap

from apibase import APIBase

obj = APIBase("torch.randperm")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randperm(5)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        n = 5
        result = torch.randperm(n)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        n = 5
        result = torch.randperm(n, dtype=torch.float64, layout=torch.strided, requires_grad=True, pin_memory=False)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        out = torch.zeros(5, dtype=torch.float64)
        result = torch.randperm(5, dtype=torch.float64, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randperm(n=6, dtype=torch.float64, layout=torch.strided, requires_grad=True, pin_memory=False)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)