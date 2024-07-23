#!/usr/bin/env python3
"""Simple pagination"""
from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the range of indexes to return in
    a list for given pagination parameters"""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize this class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []
