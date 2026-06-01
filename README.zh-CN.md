# 研究生科研 Skills

[English](README.md) | [简体中文](README.zh-CN.md)

这个仓库是一套 GitHub-ready 的模块化科研 skills，专门为计算机相关专业，包括计算机应用类专业的华人研究生和科研助手准备，覆盖计算机、人工智能、工程类研究中最常见的毕业科研工作流。

当前由于内卷特色，中国大陆地区很多计算机相关专业毕业往往需要两个小论文加一篇大论文。这套 skill 从论文选题、开题报告、文献调研、文献精读、文献矩阵、方法归纳、创新点挖掘、实验设计、实验对比到论文组织，都已经覆盖，目标是为你的毕业保驾护航。

这个 skill 不是一键出文章的 skill。它是交互式的，会不断提问、引导、检查、整理，带你做计算机相关的研究，陪你从开题走到毕业。这个项目会不断完善，欢迎大家使用、关注，也欢迎提出建议。

每个 skill 都是 `skills/` 下一个独立的 `SKILL.md` 目录。共享模板、rubrics 和科研诚信规则放在 `shared/` 下，让每个 skill 保持紧凑，同时能输出结构化科研材料。

## Skill 索引

| Skill | 用途 |
| --- | --- |
| `research-topic-selection` | 选择、收敛和评估科研选题。 |
| `research-proposal` | 起草开题报告、论文开题、课题申请或研究计划。 |
| `research-literature-search` | 检索和收集近期文献，并检查期刊会议层次、代码和元数据。 |
| `research-paper-reading` | 精读单篇论文，整理代码、图解、数学原理和实验。 |
| `research-literature-matrix` | 把多篇论文整理成文献矩阵和对比表。 |
| `research-method-synthesis` | 对调研文献中的方法进行归类，并解释方法族。 |
| `research-idea-mining` | 挖掘研究空白、创新点和可行贡献方向。 |
| `research-experiment-design` | 设计数据集、指标、baseline、消融实验和实验协议。 |
| `research-experiment-comparison` | 对比实验、baseline、消融结果和论文中的结果声明。 |
| `research-paper-organization` | 组织论文、学位论文章节、相关工作和贡献叙事。 |

## 安装

把 `skills/` 中一个或多个 skill 目录复制到你的 Codex skills 目录中；如果你的 Codex 环境支持从仓库安装 skill，也可以把这个仓库作为可复用 skill 源。

典型本地复制结构：

```text
~/.codex/skills/research-literature-search/SKILL.md
~/.codex/skills/research-paper-reading/SKILL.md
```

开发或使用时，请让 `shared/` 目录与仓库保持在一起。单独复制某个 skill 到别处时，也要复制它引用的共享文件，或者调整其中的相对路径。

## 验证

发布前运行结构检查：

```bash
python3 -m unittest tests/test_validate_research_skills.py
python3 scripts/validate_research_skills.py
```

验证器会检查必需文件、skill frontmatter、必需章节和未解决的草稿标记。

## 科研诚信规则

这些 skills 是科研助手，不是引用生成器。它们必须：

- 不编造论文、会议期刊、代码链接、指标或实验结果。
- 对未知元数据明确标注。
- 区分已验证证据和推断。
- 对近期文献、会议期刊层次、影响因子、CCF 分类和开源状态，优先使用当前来源核验。
