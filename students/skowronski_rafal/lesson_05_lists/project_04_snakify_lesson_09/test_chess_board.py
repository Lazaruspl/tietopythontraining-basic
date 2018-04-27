import pytest
from chess_board import get_chess_board


class TestChessBoard:
    test_data = [
        (3, 4, [
            ['.', '*', '.', '*'],
            ['*', '.', '*', '.'],
            ['.', '*', '.', '*']
        ]),
        (6, 8, [
            ['.', '*', '.', '*', '.', '*', '.', '*'],
            ['*', '.', '*', '.', '*', '.', '*', '.'],
            ['.', '*', '.', '*', '.', '*', '.', '*'],
            ['*', '.', '*', '.', '*', '.', '*', '.'],
            ['.', '*', '.', '*', '.', '*', '.', '*'],
            ['*', '.', '*', '.', '*', '.', '*', '.']
        ]),
        (8, 3, [
            ['.', '*', '.'],
            ['*', '.', '*'],
            ['.', '*', '.'],
            ['*', '.', '*'],
            ['.', '*', '.'],
            ['*', '.', '*'],
            ['.', '*', '.'],
            ['*', '.', '*'],
        ]),
        (7, 5, [
            ['.', '*', '.', '*', '.'],
            ['*', '.', '*', '.', '*'],
            ['.', '*', '.', '*', '.'],
            ['*', '.', '*', '.', '*'],
            ['.', '*', '.', '*', '.'],
            ['*', '.', '*', '.', '*'],
            ['.', '*', '.', '*', '.']
        ]),
        (1, 6, [
            ['.', '*', '.', '*', '.', '*']
        ]),
        (8, 1, [
            ['.'],
            ['*'],
            ['.'],
            ['*'],
            ['.'],
            ['*'],
            ['.'],
            ['*']
        ]),
        (1, 1, [
            ['.']
        ]),
    ]

    @pytest.mark.parametrize('rows_count, cols_count, expected', test_data)
    def test_get_chess_board_on_test_data(
            self,
            rows_count,
            cols_count,
            expected):
        assert get_chess_board(rows_count, cols_count) == expected
