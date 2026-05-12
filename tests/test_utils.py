import pytest

from ytshow.utils import extract_video_id, format_timestamp


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
