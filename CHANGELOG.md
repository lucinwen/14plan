# 版本记录与旧版保留

> 2026-10-19 课程质量复核。原版仍可通过 GitHub **不可变历史提交**查看，不会丢失。

- **v1 原始提交**：[查看最初 14天计划（25 文件）](https://github.com/venividici/14plan/tree/6d83f52571913a5f8cdb9c6984e9599b4330882c)
- **v2 当前主分支**：[查看当前 README](README.md)

## v1 → v2 的实质变化

| 项目 | v1 | v2 |
|---|---|---|
| 理论学习 | Modern Robotics + ROS2 + Z3 + PDDL | 保留上述主课，增加 MIT Robotic Manipulation / TAMP |
| 机器人仿真 | Isaac Sim 概念 | 增加 Isaac Lab 训练环境契约（obs/action/reward/reset/success） |
| 具身学习 | RL + robomimic 及短视频 | 增加吉林大学 AVCLab、LeRobot、π0/Diffusion Policy 原始研究入口 |
| 场景评测 | 成功率等指标 | 加入 BEHAVIOR-1K 任务表示与公平基线、失败分类 |
| XR | WebRTC 传输 | 加 OpenXR 参考空间：**空间配准与传输不能混为一谈** |
| 视频策略 | 每天固定2h视频 | 仅看匹配当天问题的精选选集；以官方课/文档兜底；Day14不看新课 |
| 面试训练 | 第14天为主 | Day3/7/10/12/14 五次里程碑，D+1/D+3/D+7 间隔复习 |
| 题库 | 45问 | 57问，新增训练接口、任务评测、科研方法追问 |
| 证据边界 | 实操+真实贡献 | 严格区分学习理解、AI辅助代码、实际跑通与既往工作经历 |

## 重要质量说明

- 复核覆盖**本次候选资源和公开检索**，不是对 B站/YouTube 全网逐帧试看或终极排名。
- 个别 B站链接返回 412，不声称已播放验证；用公开可检索的标题与目录作索引，原始论文、大学与工具官方链接作为主证据。
- 仓库为 **Public**；不要上传个人电话、邮箱、企业内部源代码、私密简历证据、真实传感/人脸/健康数据。
## v3｜2026-10-20 · 面试选拔定向实施（保留 v1/v2）
- 旧的不可变版本：**v1** [6d83f525](https://github.com/venividici/14plan/tree/6d83f52571913a5f8cdb9c6984e9599b4330882c) / **v2** [1604d723](https://github.com/venividici/14plan/tree/1604d723d83cfa21b734aaf6b942822a6af30b80)。
- 新增 [RELATED_WORK.md](RELATED_WORK.md)：MANSION(CVPR2026)、另一个同名 SceneWeaver(NeurIPS2025)、Holodeck(CVPR2024)及个人研究的证据对照。
- 新增 [ADMISSION_PREP.md](ADMISSION_PREP.md)：10/27材料冻结、建议10/28提交、10/29核验、10/30用户确认截止日；提前模拟面试。
- 所有14天的学习页面保留，Day1–13改成**主题差异化10小时表**；Day8新增论文比较，Day9首轮完整模拟。
- 新增 [minilab/](minilab/)（受限二维几何+图+任务状态检查、可选Z3例子）与17项单元测试；它是**新学习练习，不是腾讯或科研原项目成果**。
- 新增 [scripts/check_plan.py](scripts/check_plan.py) 和 GitHub Actions；检查内部链接、14天文件、截止节点与minilab单元测试。
- 更新课程/论文/题库（57→73问）/阶段考核/进度表。原有资源没有整体替换，保密与贡献边界继续生效。
- 本版采用 PR [#1](https://github.com/venividici/14plan/pull/1) 进行审阅、CI和合并，保留 Git 历史与差异记录。


## v4｜2026-10-20 · 逐资源实操教程
- 为全部 **22份课程/工具资源 R01–R22、9份论文/研究 P01–P09** 新增独立[学习指南](STUDY_GUIDES/README.md)；不删除旧版课程及项目。
- 所有14份DAILY页面都改为有子教程链接，每份详细说明所学章节、要跳过的部分、练习和验收。
- 用真实B站目录核对R01、R02、R09、R13、R15、MIT R16，并修正R11、R14、R22错误入口。
- README、RESOURCES、PLAN_14_DAYS均指向一键可进入的教程目录；自动测试验证教程完整性和链接。


## v5｜2026-10-20 · 完整14天任务操作教学
- 新增 [TASK_GUIDES/README.md](TASK_GUIDES/README.md)，14份逐时间段任务操作手册和14份独立参考答案/排错，与原计划预算对应（Day01–13每一天7段、Day14 8段）。
- 新增 [TASK_GUIDES/WORKLOG_TEMPLATE.md](TASK_GUIDES/WORKLOG_TEMPLATE.md) 用于本地分阶段记录预测、本人操作、实测或未运行、反例与复盘。
- 所有DAILY、主README、宏观计划、学习协议、进度与Codex教练均已接入新操作层；旧资源教程和全部Git历史保留。
- CI自动验证阶段数、时间预算、答案配对、Markdown链接与原MiniLab/Z3测试。
