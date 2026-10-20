# 14天任务操作手册 V6｜一日一套任务、一日一份独立答案

> 本目录是原有 [DAILY每日计划](../DAILY/) 的“操作教学层”，**没有重新设计时间表**。31份 [STUDY_GUIDES](../STUDY_GUIDES/README.md) 负责每个资源看哪一节；14份 TASK_GUIDES 负责每个时间块起手、主练习、核验、交付；14份答案手册提供参考答案和误区诊断。

## V6 我们具体补强了哪些问题
- **基础原理**：Day01坐标与门宽、Day02六种SAT/UNSAT、Day03开锁/开门/PDDL、Day04 FK/IK/Jacobian及手算答案。
- **机器人主线**：Day05 ROS2消息与导航失败、Day06 Isaac Lab Task Contract、Day07 BC/RL/VLA与公平对照、Day08 MANSION/SceneWeaver真实论文比较。
- **交互与感知**：Day09旧LLM/TTS打断状态、Day10 3DGS/FLAME与音画时延、Day11 FMCW具体数值、Day12 SAR多源证据、Day13 XR双端坐标。
- **录取答辩**：Day14两轮**真正各45分钟**的计时模拟，个人职责/团队成果/未来计划分开；并清除了答案里大量重复的泛泛追问。

**每天的完成标准**：先交一份不看资料的首次答案，至少手算/实践一例、构造一例失败，并能说清`输入→机制→输出→假设→局限`；不懂就标未知，运行失败要保存实际报错而非填PASS。

## 今天这样开始（先实践，后对答案）
1. 打开 [Day01每日计划](../DAILY/day-01.md)。
2. 点 [Day01任务操作手册](day-01.md)，按阶段1→阶段7执行；遇到知识需求再点对应R01/R16资源子教程。
3. 录入你**第一次闭卷回答**和真实运行的输出，区分“纸面/合成示例/本机实测/历史研发”。
4. 完成尝试后再查看 [Day01答案及排错](ANSWERS/day-01.md)，订正两处最大误区。
5. 按 [本地工作记录模板](WORKLOG_TEMPLATE.md)记下D+1/D+3/D+7复习，不提交企业信息和私人录音。

## 14天所有任务与答案
| 天数 | 学习主题 | 每日原计划 | 逐阶段操作手册 | 完成后核答案 |
|---|---|---|---|---|
| 01 | 空间表示、三维坐标与五层合法性 | [Day01](../DAILY/day-01.md) | [具体怎么做](day-01.md) | [参考答案/排错](ANSWERS/day-01.md) |
| 02 | Z3/SMT和SAT/UNSAT反例 | [Day02](../DAILY/day-02.md) | [具体怎么做](day-02.md) | [参考答案/排错](ANSWERS/day-02.md) |
| 03 | PDDL/TAMP任务状态与动作 | [Day03](../DAILY/day-03.md) | [具体怎么做](day-03.md) | [参考答案/排错](ANSWERS/day-03.md) |
| 04 | FK/IK/Jacobian运动学 | [Day04](../DAILY/day-04.md) | [具体怎么做](day-04.md) | [参考答案/排错](ANSWERS/day-04.md) |
| 05 | ROS2/TF/URDF/Nav2任务接口 | [Day05](../DAILY/day-05.md) | [具体怎么做](day-05.md) | [参考答案/排错](ANSWERS/day-05.md) |
| 06 | Isaac Sim/Lab和仿真任务合同 | [Day06](../DAILY/day-06.md) | [具体怎么做](day-06.md) | [参考答案/排错](ANSWERS/day-06.md) |
| 07 | BC/RL/Diffusion/VLA具身学习 | [Day07](../DAILY/day-07.md) | [具体怎么做](day-07.md) | [参考答案/排错](ANSWERS/day-07.md) |
| 08 | MANSION/SceneWeaver学术对照与材料冻结 | [Day08](../DAILY/day-08.md) | [具体怎么做](day-08.md) | [参考答案/排错](ANSWERS/day-08.md) |
| 09 | 实时语音、报名与首场完整模拟 | [Day09](../DAILY/day-09.md) | [具体怎么做](day-09.md) | [参考答案/排错](ANSWERS/day-09.md) |
| 10 | 3DGS/FLAME/SMPL-X数字人 | [Day10](../DAILY/day-10.md) | [具体怎么做](day-10.md) | [参考答案/排错](ANSWERS/day-10.md) |
| 11 | FMCW/陪伴机器人误报与安全 | [Day11](../DAILY/day-11.md) | [具体怎么做](day-11.md) | [参考答案/排错](ANSWERS/day-11.md) |
| 12 | SAR/天穹慧眼可信感知 | [Day12](../DAILY/day-12.md) | [具体怎么做](day-12.md) | [参考答案/排错](ANSWERS/day-12.md) |
| 13 | Rove XR/WebRTC/触觉安全及二轮模拟 | [Day13](../DAILY/day-13.md) | [具体怎么做](day-13.md) | [参考答案/排错](ANSWERS/day-13.md) |
| 14 | 全简历真实贡献与全真面试 | [Day14](../DAILY/day-14.md) | [具体怎么做](day-14.md) | [参考答案/排错](ANSWERS/day-14.md) |

## 每天“完成”必须满足
- **按原计划时间块提交**：Day01–13七段，Day14八段，10小时有效学习（休息另计）；可调整具体开始时刻，不能用没做的内容凑满时数。
- **自己先答、再看答案**：包含至少一条可行路径和一条失败反例；会讲输入、约束、模块输出和无法验证的条件。
- **不能倒填履历**：新MiniLab、AI辅助示例、公开课程案例绝不冒充过去的腾讯项目/个人科研实测。
- **尊重个人与企业隐私**：本仓库Public；面试录音、简历全文、报名回执、企业未公开代码和个人数据一律只保存在本地私人目录。

按 [LEARNING_PROTOCOL](../LEARNING_PROTOCOL.md) 五维（概念、因果、接口、验证、真实性）给闭卷答辩评分，低于要求时只复习关键错误，不强行赶新课程。

[返回仓库首页](../README.md) · [所有资源教程](../STUDY_GUIDES/README.md) · [进度表](../PROGRESS.md)


## 卡住时的最短自救流程
1. 看不懂视频：只回 [STUDY_GUIDES](../STUDY_GUIDES/README.md) 中指定的分P或官方章节，不随机刷全集。
2. 算法/数学卡住：先复写输入、单位和一个最小数值例；把失败点精确到公式或接口。
3. 环境安装超过90分钟：改纸面推导/公开示例，记录未运行；不因此跳过当天反例和闭卷答辩。
4. 面试卡住：先讲当前确知的个人贡献、模型前提和验证边界，不胡编没有完成的实机结果。

