#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        if start_idx > len(data):
            return []
        return data[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs:"""
        page_data = self.get_page(page, page_size)
        start_idx, end_idx = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end_idx < len(self.__dataset) else None,
            'prev_page': page - 1 if start_idx > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
