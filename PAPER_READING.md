# 机器人学习 + 空间生成研究/基准入口：建立可核验的科研判断

> 目的：把“知识图谱很广”转成“能判断什么是真需求，如何测试”。面试不要求背数值；涉及第三方报告的指标请主动说明实验条件、来源与限制。

| 方向 | 官方来源 | 要带走的三个问题 | 安排 |
|---|---|---|---|
| Task-and-motion planning | [MIT Robotics Manipulation 讲义](https://manipulation.mit.edu/) | 符号目标如何映射到可执行连续动作？碰撞规划如何反馈上层？为什么不能只做 BFS？ | Day 03，必看 |
| Robot learning | [LeRobot 官方文档](https://huggingface.co/docs/lerobot/index) | 观测、动作如何采集并对齐？如何学到策略？如何定义评测回合？ | Day 07，必看 |
| Diffusion policy | [Cheng Chi 等原始研究](https://diffusion-policy.cs.columbia.edu/) | 行动序列如何表示？多模态动作为什么麻烦？同样数据、计算和机器人下如何公平比较？ | Day 07，选看 |
| VLA / π0 | [Physical Intelligence π0 原文](https://www.pi.website/blog/pi0) | VLM 如何连接连续动作？训练数据来自哪些机器人？跨具身迁移的结论边界是什么？ | Day 07，必看概览 |
| Simulation and robotics learning | [NVIDIA Isaac Lab](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-lab/latest/isaac-lab-basics/01-the-isaac-platform.html) | 场景、任务、物理、学习器谁负责什么？obs/action/reward/termination/reset 怎样定义？ | Day 06，必看 |
| Interactive evaluation environments | [Stanford BEHAVIOR-1K](https://behavior.stanford.edu/) | 人需要机器人完成什么？谓词/任务状态的范围？任务成功率和仿真可用性如何验证？ | Day 08，必看 |
| 机器人学习对比 | [robomimic](https://robomimic.github.io/docs/introduction/implemented_algorithms.html) | BC 与 Diffusion 输出/数据依赖差异？训练集分布转移时如何失败？哪些评测是 rollout 而非离线指标？ | Day 07，选看 |

**论文现在也有单独的 [P01–P09 资源子教程](STUDY_GUIDES/README.md)**。Day08优先 [P06 MANSION](STUDY_GUIDES/P06.md)、[P07 同名SceneWeaver](STUDY_GUIDES/P07.md)、[P09个人项目](STUDY_GUIDES/P09.md)；不要求一天读完全部9份资料。

## 精读一篇只花 45–60 分钟，按这个顺序

1. **3 分钟**：这一研究到底想解决什么痛点？一句话讲清。
2. **10 分钟**：画输入、输出、关键模块、依赖数据。
3. **15 分钟**：找一张最重要的原始方法图/公式，口头解释其假设。
4. **10 分钟**：找实验任务、训练/测试划分、成功判据、基线和消融。
5. **10 分钟**：写一条“不等于”的警示（例如：模型输出动作≠已在不同机器人真实泛化）。
6. **2 分钟**：写进 [CHECKPOINTS.md](CHECKPOINTS.md) 的薄弱项。

### 需要牢记的两个“世界模型”

- **工程/符号世界模型**：房间、物体、几何、关系和动作状态的结构化表示。你的 SceneWeaver/Einstein 问题主要先在这个层级。
- **学习型动态世界模型**：从观测与动作预测未来状态/表征（可能在图像、潜变量或其它空间）。它们与上面可以结合，但不是同义词。**不应把“我有场景图”说成“已训练世界模型”。**

## v3 重点补课：场景生成与具身任务（Day08 先读这三篇）
| 工作 | 官方来源 | 研究问题与能力边界 | 对本人 SceneWeaver 的追问 |
|---|---|---|---|
| MANSION (CVPR 2026) | [正式论文](https://openaccess.thecvf.com/content/CVPR2026/html/Che_MANSION_Multi-floor_lANguage-to-3D_Scene_generatIOn_for_loNg-horizon_tasks_CVPR_2026_paper.html) / [代码](https://github.com/AgibotGeneral/MANSION) | 语言驱动多层建筑/跨层约束/定制和长时程任务基准；注意分别判断各项实验 | 自己是否产生了完整结构/实例/任务执行证据，还是仅组件？ |
| 同名 SceneWeaver (NeurIPS 2025) | [作者主页](https://scene-weaver.github.io/) / [代码](https://github.com/Scene-Weaver/SceneWeaver) | 可扩展工具、场景生成、反馈与评测；名字相同不是同一工作 | 个人方法的研究义务、表示/状态与独立验证是否真的不同？ |
| Holodeck (CVPR 2024) | [正式论文](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html) | 文本→物体空间关系约束→布局优化，展示了导航训练应用 | 为什么视觉/空间关系成功仍可能任务失败？ |

**实际任务**：逐篇各用 45–60 分钟找原图、评测指标、最强对照、限制。再按 [RELATED_WORK.md](RELATED_WORK.md) 填五维比较，明确标注自己项目中**现有证据**、**尚需实测**和**可能被更强基线覆盖**的假设。 
