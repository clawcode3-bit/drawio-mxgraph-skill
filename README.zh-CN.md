# Draw.io mxGraph Skill

[English](README.md) | 简体中文

一个面向 Codex 的 Draw.io（diagrams.net / mxGraph）绘图 Skill。它可以把自然语言描述转换成可继续拖拽、修改和导出的 `.drawio` 文件，而不是生成不可编辑的截图。

## 主要能力

- 根据自然语言生成架构图、业务流程图和系统集成图
- 输出合法、可编辑的 mxGraph XML
- 支持增加、删除、移动、重命名和连接节点
- 支持分组、取消分组以及 LR、RL、TB、BT 布局切换
- 自动选择 Draw.io、Iconify、AWS 和 Microsoft Fluent 风格图标
- 将 SVG 图标嵌入 `.drawio`，避免离线打开时丢失图标
- 支持方形图标卡片，图标和文字保持在节点内部
- 使用正交折线、显式路径点和高对比度标签，减少连线穿越与文字重叠
- 在交付前验证 XML 结构、节点引用和图标编码

## 项目结构

```text
.
├── drawio-mxgraph/               # 可直接安装的 Codex Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── scripts/drawio_tool.py
│   ├── references/
│   └── assets/
├── examples/                     # AgentBuilder 智能客服示例
│   ├── *.json                    # 图形规格
│   └── *.drawio                  # 可编辑成品
└── README.md
```

## 安装

```bash
git clone https://github.com/clawcode3-bit/drawio-mxgraph-skill.git
cp -R drawio-mxgraph-skill/drawio-mxgraph ~/.codex/skills/
```

重新启动 Codex 后，可以显式调用：

```text
使用 $drawio-mxgraph 生成一个 Agent 平台架构图，
包含用户、API Gateway、AgentBuilder、LLM、知识库、CRM、ERP 和工单系统。
使用方形图标卡片，采用左右布局。
```

也可以直接用 Python 工具构建：

```bash
python3 ~/.codex/skills/drawio-mxgraph/scripts/drawio_tool.py \
  build \
  --spec architecture.json \
  --output architecture.drawio
```

验证文件：

```bash
python3 ~/.codex/skills/drawio-mxgraph/scripts/drawio_tool.py \
  validate architecture.drawio
```

## 图形规格示例

```json
{
  "title": "Agent Platform",
  "direction": "LR",
  "auto_icons": true,
  "icon_layout": "tile",
  "icon_tile_size": 96,
  "nodes": [
    {
      "id": "user",
      "label": "用户",
      "icon": "fluent:person-24-filled"
    },
    {
      "id": "gateway",
      "label": "API Gateway",
      "icon": "logos:aws-api-gateway"
    },
    {
      "id": "agent",
      "label": "AgentBuilder",
      "icon": "logos:aws-step-functions"
    }
  ],
  "edges": [
    {
      "id": "user-gateway",
      "source": "user",
      "target": "gateway",
      "label": "HTTPS"
    },
    {
      "id": "gateway-agent",
      "source": "gateway",
      "target": "agent"
    }
  ]
}
```

## 增量修改

Skill 支持以下操作：

- `add_node`
- `update_node`
- `remove_node`
- `move_node`
- `add_edge`
- `remove_edge`
- `group`
- `ungroup`
- `set_layout`

示例：

```json
{
  "operations": [
    {
      "op": "move_node",
      "id": "agent",
      "x": 720,
      "y": 240
    },
    {
      "op": "update_node",
      "id": "agent",
      "label": "Customer Service Agent"
    }
  ]
}
```

## 示例项目

`examples/` 提供了一套完整的 AgentBuilder 智能客服案例，包括：

- 全渠道客户接入
- AgentBuilder 对话与任务编排
- 意图识别、知识问答、业务办理和投诉服务 Agent
- CRM、ERP、工单系统对接
- LLM、知识与数据平台、安全护栏和可观测能力
- 人工客服协同及运营智能驾驶舱

可以直接在 [diagrams.net](https://app.diagrams.net/) 中打开示例 `.drawio` 文件继续编辑。

## 图标说明

生成器可使用 Draw.io 原生图形以及 Iconify 图标。外部图标会在构建时下载并以 SVG Data URI 形式嵌入 `.drawio` 文件。

首次使用某个 Iconify 图标时需要网络连接；之后可以使用本地缓存。不同图标集可能采用不同许可证，发布或商用前请检查对应图标集的许可与商标要求。

## 设计原则

- `.drawio` 文件必须保持可编辑
- 节点 ID 在增量修改中保持稳定
- 抽象流程优先使用标准流程图符号
- 产品、云服务和角色优先使用可识别图标
- 复杂分支必须提供明确的正交折线路径
- 连线标签使用不透明背景，避免与线条和网格混淆
- XML 验证通过后仍要在 diagrams.net 中进行视觉检查

## 运行环境

- Python 3.10 或更高版本
- Codex Skills
- diagrams.net / Draw.io（用于查看与继续编辑）
- 网络连接（仅在首次下载未缓存的 Iconify 图标时需要）

## 许可证

本项目代码使用 MIT License。通过 Iconify 获取的图标及第三方商标仍受各自许可证和品牌规范约束。
