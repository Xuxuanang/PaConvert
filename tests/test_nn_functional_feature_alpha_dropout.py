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

obj = APIBase("torch.nn.functional.feature_alpha_dropout")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, -2, 3], [0, -1, 2], [1, 0, 1]], dtype=torch.float32)
        result = torch.nn.functional.feature_alpha_dropout(input=x, p=0.5, training=True, inplace=False)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch
        x = torch.tensor([[1, -2, 3], [0, -1, 2], [1, 0, 1]], dtype=torch.float32)
        result = torch.nn.functional.feature_alpha_dropout(x, 0.5, False, True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch
        x = torch.tensor([[1, -2, 3], [0, -1, 2], [1, 0, 1]], dtype=torch.float32)
        result = torch.nn.functional.feature_alpha_dropout(x)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch
        x = torch.tensor([[1, -2, 3], [0, -1, 2], [1, 0, 1]], dtype=torch.float32)
        result = torch.nn.functional.feature_alpha_dropout(training=True, input=x, p=0.5, inplace=False)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch
        x = torch.tensor([[1, -2, 3], [0, -1, 2], [1, 0, 1]], dtype=torch.float32)
        result = torch.nn.functional.feature_alpha_dropout(input=x, p=0.4, inplace=False)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
    )