import paddle

print("#########################case1#########################")
g_cpu = paddle.framework.core.default_cpu_generator()
print("#########################case2#########################")
g_cpu = paddle.framework.core.default_cpu_generator()
print("#########################case3#########################")
g_cpu = paddle.framework.core.default_cpu_generator()
print("#########################case4#########################")
device = paddle.device.get_device()
g_cuda = paddle.framework.core.default_cuda_generator(int(device[-1]))
print("#########################case5#########################")
device = paddle.device.get_device()
g_cuda = paddle.framework.core.default_cuda_generator(int(device[-1]))
