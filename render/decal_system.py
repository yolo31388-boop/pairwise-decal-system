"""第 52 批：贴花在斜面和金属上发灰、边缘硬切、重叠闪烁：法线..."""

def normalize_normal(normal):
    """把混合后的贴花法线重新归一化。"""
    raise NotImplementedError("TODO: normalize_normal")

def inverse_scale(scale):
    """返回非均匀缩放的逆缩放。"""
    raise NotImplementedError("TODO: inverse_scale")

def stencil_pass(ref, mask):
    """判断 stencil 测试是否通过。"""
    raise NotImplementedError("TODO: stencil_pass")

def depth_bias(layer, unit=0.001):
    """按贴花层返回深度偏移。"""
    raise NotImplementedError("TODO: depth_bias")

def uv_source(decal_uv, terrain_uv):
    """返回与地形同源的贴花 UV。"""
    raise NotImplementedError("TODO: uv_source")

def atlas_clamp(uv, size):
    """把图集 UV 钳制在页内。"""
    raise NotImplementedError("TODO: atlas_clamp")

def tonemap_order(hdr, exposure):
    """按 tonemap 前置顺序返回 HDR 颜色。"""
    raise NotImplementedError("TODO: tonemap_order")

def skinned_decal(local, bone):
    """把贴花局部坐标变换到骨骼空间。"""
    raise NotImplementedError("TODO: skinned_decal")
