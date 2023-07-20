# GAIL-Lab

基于[`DI-engine`](https://github.com/opendilab/DI-engine)库的生成式对抗模仿学习（[`GAIL`](https://arxiv.org/pdf/1606.03476.pdf)）算法实验。

## 结果展示
### [`Cartpole-v0`](https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html#id5)训练图像

<img src="Images\Cartpole-v0.png" width = "400" height = "300" alt="Cartpole-v0 Results of DQN-GAIL" align=center />

***

这里有基于[`DI-engine`](https://github.com/opendilab/DI-engine)的[`Cartpole-v0`训练指标说明以及胜利条件](https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html#id5)的全部介绍。

## 文件说明

| 文件名     | 说明 |
|----------|------|
| [`Cartpole`](Cartpole)     |   [`Cartpole-v0`](https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html#id5)环境的所有训练模型及生成内容   |
| [`images`](images) |   训练过程图像    |

### [`Cartpole`](Cartpole)文件夹

| 文件名     | 说明 |
|----------|------|
| [`DQN-BC`](Cartpole\DQN-BC)     |   基于`DQN`的`BC`训练文件   |
| [`DQN-GAIL`](Cartpole\DQN-GAIL) |   基于`DQN`的`GAIL`训练文件    |
| [`PPO-BC`](Cartpole\PPO-BC) |   基于`off-policy PPO`的`BC`训练文件    |
| [`PPO-GAIL`](Cartpole\PPO-GAIL) |   基于`off-policy PPO`的`GAIL`训练文件    |

在上述的每个文件夹下，找到训练好的模型文件夹。其中包含`video`文件夹，这里面按顺序保存了训练时模型的测试视频。（有些模型并未生成测试视频）