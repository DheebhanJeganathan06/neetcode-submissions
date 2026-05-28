class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rowMap = new HashMap<>();
        Map<Integer, Set<Character>> colMap = new HashMap<>();
        Map<String, Set<Character>> squareMap = new HashMap<>();

        for(int i = 0; i < board.length; i++) {
            rowMap.put(i, new HashSet<>());
            colMap.put(i, new HashSet<>());
        }

        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                char currChar = board[i][j];
                if(currChar != '.') {
                    String squareKey = (i / 3) + ", "  + (j / 3);
                    squareMap.putIfAbsent(squareKey, new HashSet<>());

                    if(rowMap.get(i).contains(currChar) || colMap.get(j).contains(currChar) || squareMap.get(squareKey).contains(currChar)) {
                        return false;
                    }
                    rowMap.get(i).add(currChar);
                    colMap.get(j).add(currChar);
                    squareMap.get(squareKey).add(currChar);
                }
            }
        }

        return true;

    }
}
