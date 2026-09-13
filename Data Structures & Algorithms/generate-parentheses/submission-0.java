class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> valids = new ArrayList<>();
        generateParenthesis(valids, "", n, 0, 0);
        return valids;
    }

    private void generateParenthesis(List<String> valids, String curr, int n, int open, int closed) {
        if (closed > open) {
            return;
        } if (curr.length() == 2*n) {
            if (closed != open) {
                return;
            }
            valids.add(curr);
            return;
        }
        generateParenthesis(valids, curr + "(", n, open + 1, closed);
        generateParenthesis(valids, curr + ")", n, open, closed + 1);
    }
}
