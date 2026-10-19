# 精选课程与官方资料 v2 · 2026-10-19 复核

> **核心原则**：**B 站负责解释直觉和展示案例，官方课程/原始论文负责核对原理，自己的实验和闭卷答辩负责证明理解。** Python、UE5、PCG 已有基础，不安排入门课。课程不能因为标题标注“2026最新”“天花板”就自动获得优先级。
>
> **链接核验说明**：`官网`=官方文档/课程入口已核对；`索引`=搜索结果能够确认 B站标题/课程目录或视频存在，**并不代表每条视频都已实际播放、字幕完整或永久可用**；`备用`=原有资源保留，但本次没有获得足够可靠的选集证据，不能当成唯一学习来源。复核日期：2026-10-19。

## 核心主课：真正值得优先投入

| 编号 | 内容 / 链接 | 适配 Day | 必看范围（**总时长受当天预算约束**） | 评价与核验 |
|---|---|---|---|---|
| **R01** | [西北大学 Modern Robotics（B站中英字幕）](https://www.bilibili.com/video/BV1KV411Z7sC/) / [官方教学站](https://modernrobotics.northwestern.edu/) | 01 / 04 / 13 | 自由度、位形空间、旋转/齐次变换、FK/IK、Jacobian；按相关小节选看，不全刷 | **S·运动学主课**｜索引+官网；课程理论强，但**不是**任务环境/世界模型全套教程 |
| **R02** | [古月居：ROS2 入门 21 讲](https://www.bilibili.com/video/BV16B4y1Q7jQ/) / [ROS2 Concepts](https://docs.ros.org/en/rolling/Concepts.html) | 05 | 第 1、8、11、16、17 节优先；第 7、9、10、18、19 节只选需补部分 | **S·ROS架构**｜原作者 B站选集+官网；略去安装/语法 |
| **R03** | [微软 Z3 Guide](https://microsoft.github.io/z3guide/) / [Z3Py 完整教程源码](https://github.com/microsoft/z3guide/blob/main/website/docs-programming/02%20-%20Z3%20Python/01%20-%20Introduction.md) / [Programming Z3](https://z3prover.github.io/papers/programmingz3.html) | 02 / 03 | Solver、model、And/Or、push/pop、unsat core / assumptions（手动构造测试） | **S·空间约束必修**｜官网；**以文档为主，不凑满两小时视频** |
| **R04** | [Planning.wiki PDDL Domain](https://planning.wiki/ref/pddl/domain) / [Problem](https://planning.wiki/ref/pddl/problem) | 03 | predicates、precondition、effect、initial state、goal | **S·状态与规划**｜原始术语直达；不是完整 TAMP 课程 |
| **R16** | [MIT 6.4210 Robotic Manipulation（官方讲义/课程）](https://manipulation.mit.edu/) / [2022 课程目录](https://manipulation.csail.mit.edu/Fall2022/schedule.html) / [B站系列](https://www.bilibili.com/video/BV1dB4y1R7bS/) | 01/03/04/06/08 | 优先第 21 讲 **Task-and-Motion Planning**；第 5 讲点云与配准、第 13–14 讲运动规划、第 1 讲系统整体按需选读 | **S·补足最大漏洞**｜MIT官网+B站索引；英文主讲/B站搬运，**不建议连续刷全集** |
| **R05** | [Nav2 官方 Navigation Servers](https://github.com/ros-navigation/docs.nav2.org/blob/rolling/docs/getting_started/navigation_concepts/navigation_servers.md) | 05 | Planner、Controller、Recovery、Costmap，对应 Topic/Action/TF | **A·架构补强**｜官网；避免只会背 ROS2 名词 |
| **R06** | [Isaac Sim Core API 官方教程](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/index.html) | 06 | Hello World、Hello Robot、机器人、碰撞、传感、坐标与物理参数 | **S·仿真基础**｜官网；实际运行需匹配设备、版本与驱动 |
| **R19** | [NVIDIA Isaac Lab：机器人学习任务系统](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-lab/latest/isaac-lab-basics/01-the-isaac-platform.html) | 06/07/08 | observation、action、reward、termination、reset、随机化、批量环境；Sim vs Lab vs Arena 角色 | **S·具身环境接口**｜官网；这部分**上一版缺失** |
| **R07** | [李宏毅强化学习概述（B站转载）](https://www.bilibili.com/video/BV1SJvAzfEL2/) | 07 | 先看概述第 1 讲（约45分钟），Policy Gradient / Actor Critic 按需 | **A·强化学习直觉**｜索引；标题里的“2025版”**不证明是2025新授课** |
| **R18** | [吉林大学 AVCLab 机器人学习入门：State/Observation/Action Chunking](https://www.bilibili.com/video/BV1TAbS6xELE) / [π0 论文解读（B站）](https://www.bilibili.com/video/BV1SEdWBXEqj/) | 07 | 前者约 61 分钟；后者约 39 分钟（按时间二选一或截取片段） | **S·具身学习针对性**｜B站索引；讲者观点须用原论文核验 |
| **R08** | [robomimic 原始算法文档](https://robomimic.github.io/docs/introduction/implemented_algorithms.html) | 07 | BC、Transformer、Diffusion Policy 的数据与策略接口 | **A·算法对照**｜官网，**不等于跑过这些策略** |
| **R17** | [LeRobot 官方文档](https://huggingface.co/docs/lerobot/index) / [Diffusion Policy 作者的 LeRobot 研究报告（B站中文字幕）](https://www.bilibili.com/video/BV1ZaeAe7EMu/) | 07/08 | Teleoperate→Record→Train→Deploy、dataset 记录、policy rollout、评测；视频用于理解 diffusion actions | **S·实际机器人学习流程**｜官网+B站索引；新版新增 |
| **R20** | [Stanford BEHAVIOR-1K 官方 benchmark](https://behavior.stanford.edu/) / [中文论文介绍（B站）](https://www.bilibili.com/video/BV1DJ4m187D9/) | 03/08 | 任务初始/目标条件、可交互实体、场景可复现与成功定义；**先看官方，视频选看** | **S·任务环境评测基准**｜官网+B站索引；新版新增 |

## 多模态、数字人、传感与 XR：按简历广度选学

| 编号 | 内容 / 链接 | Day | 该看什么 | 评价与核验 |
|---|---|---|---|---|
| R09 | [aha-voice 项目介绍（B站）](https://www.bilibili.com/video/BV1RudZBoEWx/) / [原开源项目](https://github.com/jhqxxx/aha-voice) | 09 | Mic→VAD→ASR→LLM→TTS→speaker 的状态/延迟链 | **A·管线示例**｜索引+源码；项目以 Rust 为主，无须学 Rust |
| R10 | [可打断语音助手演示（B站）](https://www.bilibili.com/video/BV1uQBCYrEYL/) | 09 | 打断、取消、并发、时延；先用已验证 R09 源码兜底 | **B·演示备选**｜本轮未复核完整选集，不作唯一依据 |
| R11 | [SY_007：讲人话 3DGS 4 集（B站）](https://www.bilibili.com/video/BV1rJ4m1g7Un/) | 10 | 高斯表示、投影、渲染、训练；不必读 CUDA | **S·3DGS入门**｜索引；建议搭配原论文而非只看示意 |
| R12 | [FLAME](https://flame.is.tue.mpg.de/) / [SMPL-X](https://smpl-x.is.tue.mpg.de/) / [VRM 1.0](https://vrm.dev/en/vrm1/) | 10 | 参数脸/身体、表情和动作驱动、骨架/标准格式差别 | **S·原理对照**｜官网 |
| R13 | [TI mmWave 基础培训（B站）](https://www.bilibili.com/video/BV1du4m1g7bv/) / [TI 官方 mmWave 视频教程](https://www.ti.com/video/series/mmwave-training-series.html) | 11 | FMCW chirp、beat frequency、range FFT、phase、Doppler；实践以真实型号为准 | **S·雷达基础**｜官方主证据；B站具体选集未逐段实播 |
| R22 | [哈基金博士 TI 雷达采数/呼吸演示（B站合集）](https://www.bilibili.com/video/BV1qE4NzfEfD/) | 11 | 选集 **“TI DEMO实现测量呼吸心跳”**（约20分钟）及距离分辨率选集（按需） | **A·中文动手参照**｜B站索引；不把视频演示变成自己的硬件测试 |
| R14 | [南航毛新华《雷达成像技术》（B站合集）](https://www.bilibili.com/video/BV1ku4y157Fu/) | 12 | **必看 L1（约47m）和 L3（约46m）**，L5/L8 改选读，六讲不再塞进2小时 | **S·SAR系统理解**｜B站索引；不是短视频速成“全掌握” |
| R15 | [WebRTC 从入门到实战（B站）](https://www.bilibili.com/video/BV1wfpbeiEEq/) / [WebRTC Peer Connection 官方](https://webrtc.org/getting-started/peer-connections) | 13 | SDP、ICE、STUN/TURN、signaling，差别于 WebSocket | **A·实时通信**｜官网主证据；B站前6节仅备选 |
| R21 | [Khronos OpenXR Reference Spaces 规范](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#spaces) | 13 | VIEW/LOCAL 空间、xrLocateSpace、跟踪有效位、时间戳 | **S·XR真实空间定义**｜官网；新版新增 |

## 论文与前沿项目（不能替代基础课）

- **P1 · [Diffusion Policy 原论文/项目](https://diffusion-policy.cs.columbia.edu/)**：从观察到连续 action sequence；对照 BC 的动作分布建模和多峰选择。
- **P2 · [π0 原始研究](https://www.pi.website/blog/pi0)**：预训练 VLM + 连续动作输出/flow matching；不要把一次论文解读当成掌握训练全链路。
- **P3 · [OpenVLA 原始代码](https://github.com/openvla/openvla)**：对照 π0 的行动表示与预训练数据；需要时看 Readme 和模型输入输出。
- **P4 · [BEHAVIOR-1K](https://behavior.stanford.edu/)**：看具身环境的任务定义、可交互物体、长时序评测，尤其与你简历“任务可执行”主线相关。
- **P5 · [MIT Robotic Manipulation 官方笔记](https://manipulation.mit.edu/)**：含感知、规划、状态机和任务+运动规划章节，完整本科+研究生级课程，选章节读。

## 为什么这样选，而不随意找“最热门课程”

1. **作者与原始来源可靠**优先于“2026最新”标题；官方课程为准，转载视频是入口。
2. **针对真实面试问题**优先于完整度；MIT TAMP、Isaac Lab、LeRobot、BEHAVIOR 直接覆盖“环境生成→机器人执行→评测”。
3. **每课都写学习目标与停止条件**；只看与当天问题相关的 1–3 节，不额外拓展超过 2 小时的视频。
4. **以原项目论文检查衍生解读**；视频作者自评/演示可能不等于论文真正做出的结论。
5. **不强求安装重型平台**：GPU/系统/设备不明时阅读官方系统和案例，比耗费一整天配置环境更适合面试冲刺。

详细替换理由请读 [COURSE_AUDIT.md](COURSE_AUDIT.md)；每日入口见 [DAILY/](DAILY/)。