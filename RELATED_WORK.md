# 具身环境生成相关工作｜Day 08 方法对照与真实证据

> 目的：面试中解释“个人 SceneWeaver 与 MANSION 很接近”**究竟接近在哪里**，而不把相似问题偷换成已拥有同等成果。论文已发表的事实与自己在研状态分开；材料是学习提纲，不代表已完成逐项复现。

## 阅读顺序与权威出处
1. **MANSION (CVPR 2026)**：[正式论文](https://openaccess.thecvf.com/content/CVPR2026/html/Che_MANSION_Multi-floor_lANguage-to-3D_Scene_generatIOn_for_loNg-horizon_tasks_CVPR_2026_paper.html) · [作者仓库](https://github.com/AgibotGeneral/MANSION)。语言驱动、建筑尺度多楼层空间、竖向结构约束、MansionWorld 和任务语义编辑；查作者对长时程任务的具体评测。
2. **SceneWeaver (NeurIPS 2025，别人的同名工作)**：[论文主页](https://scene-weaver.github.io/) · [作者仓库](https://github.com/Scene-Weaver/SceneWeaver)。通过可扩展工具及自我反思 agent 进行三维场景合成；特别注意工具调用、反馈方式、USD/IsaacSim 资产导出与验证范围。
3. **Holodeck (CVPR 2024)**：[正式论文](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html)。用 LLM 建议空间关系约束并优化物体摆放，包含导航研究使用场景。
4. **个人在研 SceneWeaver**：[研究目标](https://github.com/venividici/ue-scene-generation-research/blob/main/research/route1/RESEARCH_TARGET.md) · [有日期的研究状态](https://github.com/venividici/ue-scene-generation-research/blob/main/CURRENT_RESEARCH_STATUS.md)。这是本人项目，与 NeurIPS 同名工作**不是同一项目**；仓库可能为私有，请不要在对外材料里把其链接当作公共可访问的证据。

## 按“研究问题—输入—实现—验证”比较（先读原文再填更多细节）
| 维度 | MANSION | NeurIPS SceneWeaver（同名） | Holodeck | 个人 SceneWeaver（目标与证据分开） |
|---|---|---|---|---|
| 核心需求 | 语言驱动建筑尺度、多楼层环境及长时任务 | 可扩展工具驱动与反思式场景合成 | 文本驱动多样化室内环境与对象摆放 | 开放关卡构想→任务/玩法状态→可编辑可执行三维关卡 |
| 主要输入 | 建筑/布局文字条件 | 场景自然语言指令与可用工具 | 文本与资产集 | 目标：单段自然语言；已有语义编译受限证据 |
| 空间重点 | 多楼层、垂直结构约束及可导航结构 | 场景合成与工具执行 | 对象关系布局优化 | 目标：跨层拓扑/几何/对象交互共享语义 |
| 功能/交互 | 包含任务语义编辑与跨层长时程评测 | 提供工具化场景修改，检查具体评测合同 | 展示导航训练场景 | 核心假说：任务状态与空间几何应共同保持原要求 |
| 已有证据 | 作者公开论文、代码、数据/实验 | 作者公开项目、代码与论文 | 作者论文中的生成及导航评测 | 用户仓库状态文件：已有受限组件；完整复杂关卡与新算法优势**尚未证明** |
| 未完成的比较 | 不推断比其他所有方法强 | 同名不等于个人创新 | 不用“画面更好”代替任务成功 | 须补完整运行、强基线、共同信息/预算和失败证据 |

> 上表是“第一轮研究导航”，非经同等条件复现的实验结论。具体对照必须以论文的方法、协议与补充材料为准。

## 面试时先讲五件事
- **研究问题**：几何连通与任务可执行之间有落差（锁门、钥匙、动作能力、跨层往返等）。
- **结构化假设**：任务谓词、状态、几何、可交互实体通过共享ID/约束关联；这是拟验证的研究路线，非已获论文优势。
- **已有证明**：分清文本编译、有限状态重放、空间检查、局部物理样例和端到端三维任务是否各自验收。
- **强基线**：MANSION/Holodeck/NeurIPS SceneWeaver 均可能覆盖相似模块；比较时固定输入、资产池、机器人、预算和测试。
- **失败边界**：Z3 sat、图可达、UE场景导出和机器人任务成功是四种不同证据。

## Day08 一小时闭卷任务
1. 用自己的话各写 **1句贡献 + 1句限制**，不能复制摘要。
2. 选“跨层有路径但门被锁”设计至少两种方法均能/不能处理的反例。
3. 做一张二栏表：**目前亲自可核实** 与 **入营后拟验证**。
4. 回答 Q61–Q63，并接受“你这不就是 MANSION 吗？”连续追问。
