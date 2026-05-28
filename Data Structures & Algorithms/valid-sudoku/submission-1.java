class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for(int i = 0; i < board.length; i++) {
            rows.put(i, new HashSet<>());
            cols.put(i, new HashSet<>());
        }

        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                Character curr = board[i][j];
                if(curr != '.') {
                    String squareKey = i/3 + ", " + j/3;
                    squares.putIfAbsent(squareKey, new HashSet<>());

                    if(rows.get(i).contains(curr) || cols.get(j).contains(curr) || squares.get(squareKey).contains(curr)) {
                        return false;
                    }
                    rows.get(i).add(curr);
                    cols.get(j).add(curr);
                    squares.get(squareKey).add(curr);
                }
            }
        }

        return true;
    }
}
