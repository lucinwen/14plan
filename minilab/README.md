# Minilab｜受限的“任务—环境”验证学习项目

> **这段新编写的练习代码不是腾讯 Einstein Layout、不是个人 SceneWeaver、也不是 MANSION 复现。** 没有机器人硬件/物理引擎/控制器/观测数据，也没有自然语言解析模型。

## 最短运行步骤
在仓库根目录执行：

```bash
python -m unittest discover -s minilab/tests -v
python -m minilab.validate
# 可选：已经安装 z3-solver 后
python -m pip install -r minilab/requirements.txt
python -m minilab.z3_demo
python -m minilab.z3_demo --width 3
```

`validate` 只依赖 Python 标准库，输出6个不同案例；`z3_demo` 用到可选的开源 z3-solver。模拟使用二维整数矩形布局（AABB）、房间邻接图、门净宽、门锁/钥匙和“能否在声明规则下抓取物品”的有限动作条件。

## 你必须区分的四种结论
- `geometry_valid`：受限 2D 检查，包括房间正面积、无内部重叠、门与共墙长度相容。
- `topology_connected`：忽略锁与净空，只检查房间图上的门边是否连通。
- `rule_task_feasible`：在简化机器人宽度、钥匙与动作能力规则下，是否有到达并执行`hold`目标的受限计划。
- **未曾验证**：机器人实际三维路径、避障、视觉观测、抓取姿态、动力学、传感、训练策略、真实/仿真 rollout。

## Day1–8 建议验收
| 天 | 练习 | 留下的学习证据 |
|---|---|---|
| D1 | 改2间房/门的位置，使共墙消失 | 同一个图，几何可以失败 |
| D2 | 运行Z3宽度4(sat)与3(unsat)；改宽度和约束 | 满足性/冲突集不自动等于物理可执行 |
| D3 | 锁门/钥匙/无开锁能力/不可抓取物分别变化 | 状态与动作前置区别 |
| D4 | 手绘机器人宽度、工作空间/机械臂的限制 | 本练习没有 IK 和碰撞路径检查 |
| D5–6 | 为`rule_task_feasible`接口写字段清单，标明ROS2/Isaac Lab仍缺什么 | 不把示意 JSON 称为真实控制接口 |
| D7 | 讨论策略/示教数据格式，不把本checker输出称训练数据 | 基准/策略需要独立验证 |
| D8 | 与人工/随机/约束方案建立共同任务规则、seed与预算 | 未跑实验则不要填成功率 |

至少修改一个条件并预测结果，再执行核验，记录预期/实际/原因。**不要只让 Codex 修改后复制“测试通过”。**

## 失败反例（最小）
- 门净宽 < 机器人宽：图连通但`blocked_geometry`；
- 门锁无钥匙：`blocked_state`；
- 机器人无`grasp`：`blocked_action`；
- 房间重叠 / 门无共墙：`invalid_geometry`；
- 目标物缺失：`invalid_input`；
- Z3 两个2×2矩形要放进3×3空间：`unsat`，但core不代表唯一需要修改的条件。

测试报告只证明**练习代码的受限逻辑符合当前测试**。不声称可以完成真实机器人物理任务，更不能写进历史实习成果。

## 版本与隐私
这里只有玩具/合成样例；禁止拷贝腾讯内部项目代码、真实人脸/健康数据、私有日志、账号密钥。源代码为新学习练习，不是论文方法原创性声明。
