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

obj = APIBase("torch.autograd.function.FunctionCtx.mark_non_differentiable")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        from torch.autograd import Function

        # Inherit from Function
        class cus_func(Function):
            @staticmethod
            def forward(ctx, x):
                a = x + x
                b = x + x + x
                ctx.mark_non_differentiable(a)
                return a, b

            @staticmethod
            def backward(ctx, grad_a, grad_b):
                grad_x = 3*grad_b
                return grad_x

        data = torch.ones([2, 3], dtype=torch.float64, requires_grad=True)
        a, b = cus_func.apply(data)
        b.sum().backward()

        result = data.grad
        """
    )
    obj.run(pytorch_code, ["a", "b", "result"], check_stop_gradient=False)
