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

from apibase import APIBase

obj = APIBase("torch.nn.functional.softmin")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = torch.nn.functional.softmin(input, dim=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = F.softmin(input=input, dim=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = F.softmin(input=input, dim=-1, dtype=torch.float64)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = F.softmin(input=input, dim=-1, _stacklevel=3, dtype=torch.float64)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = F.softmin(input, -1, 3, torch.float64)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = F.softmin(_stacklevel=3, dtype=torch.float64, input=input, dim=-1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        input = torch.tensor([[-1.2837, -0.0297,  0.0355],
            [ 0.9112, -1.7526, -0.4061]])
        result = torch.nn.functional.softmin(input)
        """
    )
    obj.run(pytorch_code, ["result"])
