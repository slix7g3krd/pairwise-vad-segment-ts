import pytest
import media.vad_segment_ts as mod

CASES = [
    ("tail_hold", (1)),
    ("boundary_backoff", (1)),
    ("stream_offline", (1)),
    ("noise_adapt", (1)),
    ("ts_align", (1)),
    ("min_segment", (1)),
    ("onset_detect", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("hangover", (1)),
    ("metrics", (1)),
    ("false_wake", (1)),
    ("merge_segments", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
