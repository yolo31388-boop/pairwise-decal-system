import pytest
from render import decal_system as mod

CASES = [
    ("normal_unit", "sum(v * v for v in m.normalize_normal((2.0, 0.0, 0.0))) == approx(1.0)"),
    ("normal_zero", "m.normalize_normal((0.0, 0.0, 0.0)) == approx((0.0, 0.0, 1.0))"),
    ("inverse_two", "m.inverse_scale(2.0) == approx(0.5)"),
    ("inverse_zero", "m.inverse_scale(0.0) == approx(1.0)"),
    ("stencil_true", "m.stencil_pass(2, 2) is True"),
    ("stencil_false", "m.stencil_pass(1, 2) is False"),
    ("bias_zero", "m.depth_bias(0) == approx(0.0)"),
    ("bias_two", "m.depth_bias(2) == approx(0.002)"),
    ("uv_terrain", "m.uv_source((0.1, 0.2), (0.6, 0.7)) == (0.6, 0.7)"),
    ("atlas_high", "m.atlas_clamp((1.2, 0.5), 1.0) == approx((1.0, 0.5))"),
    ("atlas_low", "m.atlas_clamp((-0.2, 0.5), 1.0) == approx((0.0, 0.5))"),
    ("tonemap_product", "m.tonemap_order(2.0, 3.0) == approx(6.0)"),
    ("tonemap_zero", "m.tonemap_order(2.0, 0.0) == approx(0.0)"),
    ("skinned_sum", "m.skinned_decal((1.0, 2.0), (3.0, 4.0)) == (4.0, 6.0)"),
    ("uv_same", "m.uv_source((0.0, 0.0), (0.0, 0.0)) == (0.0, 0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
