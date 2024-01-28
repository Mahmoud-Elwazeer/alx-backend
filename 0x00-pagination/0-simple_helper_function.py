#!/usr/bin/env python3
"""import libraries"""


def index_range(page, page_size):
    """return tuple start index and an end index """
    start_idx = page_size * (page - 1)
    end_idx = page_size * page

    return (start_idx, end_idx)
