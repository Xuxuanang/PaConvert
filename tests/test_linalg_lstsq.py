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

import numpy as np
from apibase import APIBase


class LstsqAPI(APIBase):
    def compare(self, name, pytorch_result, paddle_result, check_value=True):
        if isinstance(pytorch_result, (tuple, list)):
            for i in range(len(pytorch_result)):
                self.compare(self.pytorch_api, pytorch_result[i], paddle_result[i])
            return

        pytorch_numpy, paddle_numpy = pytorch_result.numpy(), paddle_result.numpy()
        assert (
            pytorch_result.requires_grad != paddle_result.stop_gradient
        ), "API ({}): requires grad mismatch, torch tensor's requires_grad is {}, paddle tensor's stop_gradient is {}".format(
            name, pytorch_result.requires_grad, paddle_result.stop_gradient
        )
        assert (
            pytorch_numpy.shape == paddle_numpy.shape
        ), "API ({}): shape mismatch, torch shape is {}, paddle shape is {}".format(
            name, pytorch_numpy.shape, paddle_numpy.shape
        )
        assert np.allclose(
            pytorch_numpy, paddle_numpy
        ), "API ({}): paddle result has diff with pytorch result".format(name)


obj = LstsqAPI("torch.linalg.lstsq")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 3], [3, 2], [5, 6.]])
        y = torch.tensor([[3, 4, 6], [5, 3, 4], [1, 2, 1.]])
        result = torch.linalg.lstsq(x, y, driver="gelsd")
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[10, 2, 3], [3, 10, 5], [5, 6, 12.]])
        y = torch.tensor([[4, 2, 9], [2, 0, 3], [2, 5, 3.]])
        result = torch.linalg.lstsq(x, y, driver="gels")
        """
    )
    obj.run(pytorch_code, ["result"])