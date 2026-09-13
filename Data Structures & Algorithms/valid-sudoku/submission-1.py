class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = dict()
        cols = dict()
        rows = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                value = board[i][j]
                if value == '.':
                    continue
                k = (i // 3) * 3 + (j // 3)
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if k not in boxes:
                    boxes[k] = set()
                if (value in rows[i] or
                    value in cols[j] or
                    value in boxes[k]):
                    return False
                rows[i].add(value)
                cols[j].add(value)
                boxes[k].add(value)
        return True