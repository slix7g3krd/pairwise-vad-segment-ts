# pairwise-vad-segment-ts

## 领域

游戏、图形与多媒体

## 主题

语音活动分段

## 说明

尾音判定、边界回退与流式离线同参。

初始状态下 `media/vad_segment_ts.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
