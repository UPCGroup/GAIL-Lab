# GAIL-Lab

基于[DI-engine](https://github.com/opendilab/DI-engine)库的生成式对抗模仿学习（[GAIL](https://arxiv.org/pdf/1606.03476.pdf)）算法实验。

## 结果展示
### [Cartpole-v0](https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html#id5)训练图像

<img src="Images\Cartpole-v0.png" width = "400" height = "300" alt="Cartpole-v0 Results" align=center />

***

这里有基于DI-engine的[Cartpole-v0训练指标说明以及胜利条件](https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html#id5)的全部介绍。

## 文件说明

| 文件名     | 说明 |
|----------|------|
| [GAIL-LAB.ipynb](GAIL-LAB.ipynb) |   Python Notebook，用于调整数据、生成图表    |
| [Cartpole](Cartpole)     |   Cartpole环境的所有训练模型及生成内容   |

### Cartpole文件夹

| 文件名     | 说明 |
|----------|------|
| [cartpole_dqn_main.py](Cartpole\cartpole_dqn_main.py) | DQN算法的训练入口文件 |
| [cartpole_dqn_config.py](Cartpole\cartpole_dqn_config.py)     | DQN算法的模型配置文件 |
| [cartpole_dqn_gail_main.py](Cartpole\cartpole_dqn_gail_main.py) | GAIL算法的训练入口文件 |
| [cartpole_dqn_gail_config.py](Cartpole\cartpole_dqn_gail_config.py) | GAIL算法的模型配置文件 |
| [cartpole_dqn_seed0\video](Cartpole\cartpole_dqn_seed0\video) | DQN算法的训练迭代视频文件夹 |
| [cartpole_dqn_gail_seed0\video](Cartpole\cartpole_dqn_gail_seed0\video) | GAIL算法的训练迭代视频文件夹 |