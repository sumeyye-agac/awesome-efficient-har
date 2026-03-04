from scripts.validate_entries import validate_payload


def test_validate_payload_reports_schema_and_normalization_errors():
    payload = {
        "entries": [
            {
                "category": "Datasets",
                "title": " Bad title ",
                "year": "2020",
                "tags": ["Dataset", "dataset"],
                "links": {"Dataset": "ftp://example.com"},
                "description": " One. Two. Three.",
            },
            {
                "category": "datasets",
                "title": "Another",
                "year": 2020,
                "tags": ["dataset"],
                "links": {"dataset": "https://example.com/a"},
                "description": "ok",
            },
            {
                "category": "datasets",
                "title": "Third",
                "year": 2019,
                "tags": ["dataset"],
                "links": {"dataset": "https://example.com/a"},
                "description": "ok",
            },
        ]
    }

    errors = validate_payload(payload, enforce_min_counts=False, enforce_order=False)

    assert any("category must be normalized" in e for e in errors)
    assert any("title must not include leading/trailing whitespace" in e for e in errors)
    assert any("year must be an integer" in e for e in errors)
    assert any("tag 'Dataset' must be normalized" in e for e in errors)
    assert any("duplicate link" in e for e in errors)


def test_validate_payload_reports_ordering_mismatch():
    payload = {
        "entries": [
            {
                "category": "datasets",
                "title": "Older",
                "year": 2019,
                "tags": ["dataset"],
                "links": {"dataset": "https://example.com/older"},
                "description": "ok",
            },
            {
                "category": "datasets",
                "title": "Newer",
                "year": 2020,
                "tags": ["dataset"],
                "links": {"dataset": "https://example.com/newer"},
                "description": "ok",
            },
        ]
    }

    errors = validate_payload(payload, enforce_min_counts=False, enforce_order=True)
    assert any("Entries must be ordered by category, then year (desc), then title" in e for e in errors)
