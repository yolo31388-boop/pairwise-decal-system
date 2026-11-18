# pairwise-decal-system

贴花在斜面和金属上发灰、边缘硬切、重叠闪烁：法线混合用加法没重归一；贴花投影矩阵没考虑非均匀缩放；stencil 只写不测；透明贴花排序按中心距离；贴花和地形 splat 的 UV 不同源；HDR 颜色没做 tonemap 前置；多张贴花重叠时深度偏移相同；贴花贴到蒙皮物体不跟随骨骼；正交投影在远距离穿透；贴花图集边缘 bleeding。render/decal_system.py 是核心，tests/test_decal_system.py 15个红。要修的是：法线重归一；逆投影矩阵；stencil 测试；逐像素排序；UV 同源；tonemap 顺序；按层深度偏移；蒙皮贴花；投影钳制；图集边缘 clamp。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
