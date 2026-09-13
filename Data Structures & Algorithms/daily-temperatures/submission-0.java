class Solution {
    public int[] dailyTemperatures(int[] temps) {
        int[] result = new int[temps.length];
        Stack<Point> stack = new Stack<>();
        for (int i = 0; i < temps.length; i++) {
            if (!stack.empty() &&  temps[i] > stack.peek().value) {
                while (!stack.empty() && temps[i] > stack.peek().value) {
                    Point p = stack.pop();
                    result[p.index] = i - p.index;
                }
            }
            stack.push(new Point(i, temps[i]));
        }
        return result;
    }
    
    private class Point {
		int index;
        int value;
        public Point(int index, int value) {
        	this.index = index;
            this.value = value;
        }
    }
}
