import pytest

from normalizer.viewer import view_variants

from .commons import patch_retriever


@pytest.mark.parametrize(
    "description, output",
    [
        (
            "NM_003002.2:r.274g>u",
            {
                "views": [
                    {
                        "start": 0,
                        "end": 334,
                        "type": "outside",
                        "left": "gugggaauug",
                        "right": "cucugcgaug",
                    },
                    {
                        "description": "274g>u",
                        "start": 334,
                        "end": 335,
                        "type": "variant",
                        "deleted": {"sequence": "g"},
                        "inserted": {"sequence": "u", "length": 1},
                    },
                    {
                        "start": 335,
                        "end": 1382,
                        "type": "outside",
                        "left": "acuauucccu",
                        "right": "aaaaaaaaaa",
                    },
                ],
                "seq_length": 1382,
            },
        )
    ],
)
def test_view_variants(description, output):
    assert view_variants(description) == output
