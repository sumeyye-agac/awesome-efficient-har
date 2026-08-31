from scripts.generate_readme import render_readme


def test_generated_readme_contains_mandatory_sections():
    entries = [
        {
            "category": "datasets",
            "title": "Tiny Dataset",
            "year": 2025,
            "tags": ["dataset"],
            "links": {"dataset": "https://example.com/dataset"},
            "description": "Minimal dataset.",
        }
    ]

    readme = render_readme(entries)

    assert "Legend:" in readme
    assert "## Datasets (wearable/IMU/multimodal)" in readme
    assert "## Self-supervised and foundation models for HAR" in readme
    assert "## Deployment patterns (windowing/streaming/personalization)" in readme
    assert "## Edge HAR starter packs" in readme
    assert "MIT license." in readme
