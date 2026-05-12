import pytest

from ytshow.utils import extract_video_id, format_timestamp, slugify_title


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/live/a3-OJxxW810?si=ZWBh4IHquiCi9DOJ", "a3-OJxxW810"),
        ("https://www.youtube.com/shorts/abcdefghijk", "abcdefghijk"),
        ("https://www.youtube.com/embed/abcdefghijk", "abcdefghijk"),
        ("dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ],
)
def test_extract_video_id(url, expected):
    assert extract_video_id(url) == expected


def test_extract_video_id_invalid():
    with pytest.raises(ValueError):
        extract_video_id("https://example.com/foo")


def test_format_timestamp():
    assert format_timestamp(0) == "00:00"
    assert format_timestamp(59) == "00:59"
    assert format_timestamp(60) == "01:00"
    assert format_timestamp(3600) == "01:00:00"
    assert format_timestamp(3661) == "01:01:01"


@pytest.mark.parametrize(
    "title,expected",
    [
        (
            "\U0001f3ac Watch The Android Show | I/O Edition 2026",
            "android-show-io-edition-2026",
        ),
        ("How to Use Python for Data Science", "how-use-python-data-science"),
        ("Live: Apple Keynote September 2025", "apple-keynote-september-2025"),
        ("the official trailer", "official-trailer"),
        ("Q&A with the team", "qa-team"),
        ("2026 keynote", "keynote-2026"),
        ("", "video"),
        ("!!! ???", "video"),
    ],
)
def test_slugify_title(title, expected):
    assert slugify_title(title) == expected


def test_slugify_title_long_capped():
    title = "Big Long Keynote Announcement Conference About Things 2026"
    slug = slugify_title(title)
    assert slug.startswith("big-long-keynote-announcement-")
    assert slug.endswith("-2026")
    assert slug.count("-") == 4  # 4 separators -> 5 tokens
