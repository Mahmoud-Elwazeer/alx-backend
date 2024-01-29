#!/usr/bin/env python3
"""import libraries"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """return tuple start index and an end index """
    start_idx = page_size * (page - 1)
    end_idx = page_size * page

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """find the correct indexes to paginate the dataset correctly and
        return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page != 0 or page_size != 0
        assert page >= 0
        assert page_size >= 0

        self.__dataset = self.dataset()

        if (page * page_size > len(self.__dataset)):
            return []

        start_idx, end_idx = index_range(page, page_size)
        return self.__dataset[start_idx:end_idx]
