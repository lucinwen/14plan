# 课程与学习资料｜B 站优先，官方文档补原理

只看与**当天知识问题**对应的选集，避免刷完几十小时课程却没有实际输出。以下链接已按对应课程名称检索核对（2026-10-19）；部分是转载/搬运，版权归原作者，视频失效时优先使用原作者官方资料。

| ID | 类别 | 资源 | 指定观看 / 阅读部分 | 关联日 |
|---|---|---|---|---|
| R01 | B站 | [《现代机器人学》Modern Robotics（中英字幕）](https://www.bilibili.com/video/BV1KV411Z7sC/) | 自由度、位形空间、SE(3)、FK/IK、Jacobian | 01 / 04 / 13 |
| R02 | B站 | [古月居 ROS2 入门21讲](https://www.bilibili.com/video/BV16B4y1Q7jQ/) | 第 1、7–11、16–19 节（不看安装/基础语法） | 05 |
| R03 | 官方 | [微软 Z3 Guide 仓库](https://github.com/microsoft/z3guide) / [Z3Py教程](https://github.com/microsoft/z3guide/blob/main/website/docs-programming/02%20-%20Z3%20Python/01%20-%20Introduction.md) | SMT、模型、Unsat Core、增量求解，配合手头空间几何题 | 02 / 03 |
| R04 | 文档 | [Planning.wiki PDDL Domain](https://planning.wiki/ref/pddl/domain) | Predicate、Action、Precondition、Effect | 03 |
| R05 | 官方 | [Nav2 Navigation Servers 概念文档](https://github.com/ros-navigation/docs.nav2.org/blob/rolling/docs/getting_started/navigation_concepts/navigation_servers.md) | Planner、Controller、行为恢复、代价地图 | 05 |
| R06 | 官方 | [Isaac Sim 6.1 Core API Tutorial Series](https://docs.isaacsim.omniverse.nvidia.com/6.1.0/core_api_tutorials/index.html) | Hello World / Hello Robot / Manipulator 的前半部分 | 06 |
| R07 | B站 | [李宏毅强化学习课程（2025 版转载）](https://www.bilibili.com/video/BV1SJvAzfEL2/) | 前 3 节（RL、Policy Gradient、Actor-Critic） | 07 |
| R08 | 官方 | [robomimic 已实现算法](https://robomimic.github.io/docs/introduction/implemented_algorithms.html) | BC、BC-Transformer、Diffusion Policy、Offline RL | 07 |
| R09 | B站 | [aha-voice：从零搭建语音助手](https://www.bilibili.com/video/BV1RudZBoEWx/) | VAD、ASR、LLM、TTS 短视频选集（示例是 Rust，不需学 Rust） | 09 |
| R10 | B站 | [实时语音助手：VAD、任意打断、多模态](https://www.bilibili.com/video/BV1uQBCYrEYL/) | 打断与时延的架构思路，不要求重写全部模型 | 09 |
| R11 | B站 | [SY_007：讲人话 3D Gaussian Splatting 4 集](https://www.bilibili.com/video/BV1rJ4m1g7Un/) | 4 集讲原理、公式和渲染（系列页可以跳转） | 10 |
| R12 | 官方 | [FLAME](https://flame.is.tue.mpg.de/) / [SMPL-X](https://smpl-x.is.tue.mpg.de/) / [VRM](https://vrm.dev/en/vrm1/) | 分别看面部参数、全身动作和表情驱动规范 | 10 |
| R13 | B站 | [TI 毫米波雷达基础知识课程](https://www.bilibili.com/video/BV1du4m1g7bv/) | FMCW、相位、速度、系统设计、角度估计 | 11 |
| R14 | B站 | [南航《雷达成像技术》L6（33 集合集）](https://www.bilibili.com/video/BV1ku4y157Fu/) | L1、L3、L5、L6、L7、L8；不要全刷 | 12 |
| R15 | B站 | [WebRTC 从入门到实战](https://www.bilibili.com/video/BV1wfpbeiEEq/) | 前 6 节：架构、STUN、TURN、信令、点对点连接 | 13 |

## 补充资料

- [现代机器人学官方网站](https://modernrobotics.northwestern.edu/)：读刚体变换、运动学及运动规划章节，B站视频只用于建立直觉。
- [ROS2 官方 Concepts](https://docs.ros.org/en/rolling/Concepts.html)：可以查对概念，留意不同 ROS2 发行版 API 差异。
- [SMT-LIB 官方标准](https://smt-lib.org/)：当讨论逻辑理论、输入表达式或求解能力边界时查阅。
- [robomimic 文档总览](https://robomimic.github.io/docs/)：理解策略训练、数据集、rollout、评价环节。
- [TI 官方毫米波课程](https://www.ti.com/video/series/mmwave-training-series.html)：FMCW 官方视频系列，可用于复核 B站转载内容。
- [WebRTC 官方 Peer Connection 概述](https://webrtc.org/getting-started/peer-connections)：比较媒体连接与信令责任。

## 怎么判断视频值得看？

1. 看完 20–30 分钟后，能否自己画出输入输出与数据流？不能就停下，回去读资料。
2. 与当天目标无关的安装、框架语法和调参细节一律跳过。
3. 优先保留可证明的产物：约束样例、架构图、反例、对照表、面试口述记录。
4. 外部资料可能更新，具体 API/工具版本以使用时的官方文档为准。