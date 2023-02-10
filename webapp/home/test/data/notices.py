"""Data for test setup."""

from .subsites import TEST_SUBSITES

TEST_NOTICES = [
    {
        "data": {
            "notice_class": "info",
            "title": "Test Notice 1",
            "body": "# Test notice body\n\nThe notice body in markdown.",
            "enabled": True,
            "is_published": True,
        },
        "relations": {
            "subsites": [TEST_SUBSITES[0]],
        },
    },
    {
        "data": {
            "notice_class": "info",
            "title": "Test Notice 2",
            "body": (
                "# Test notice body 2\n\n"
                "Another arbitrary info notice."
                " This one will also be displayed on a second subsite."
            ),
            "enabled": True,
            "is_published": True,
        },
        "relations": {
            "subsites": [
                TEST_SUBSITES[0],
                TEST_SUBSITES[1]
            ],
        },
    },
    {
        "data": {
            "notice_class": "info",
            "title": "Test Notice 3",
            "body": (
                "# Test notice body 3\n\nThis notice is not yet published."
            ),
            "enabled": True,
        },
        "relations": {
            "subsites": [TEST_SUBSITES[0]],
        },
    },
    {
        "data": {
            "notice_class": "warning",
            "title": "Test Notice 4",
            "body": (
                "# A warning notice 3\n\nThis is a warning message."
            ),
            "enabled": True,
            "is_published": True,
        },
        "relations": {
            "subsites": [TEST_SUBSITES[0]],
        },
    },
]
