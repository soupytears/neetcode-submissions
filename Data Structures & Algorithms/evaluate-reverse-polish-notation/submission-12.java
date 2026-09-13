class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if ("+-*/".contains(tokens[i])) {
                evaluateStack(stack, tokens[i]);
            } else {
                stack.push(tokens[i] + "");
            }
        }
        return Integer.parseInt(stack.pop());
    }
    
    private void evaluateStack(Stack<String> stack, String op) {
        int num2 = Integer.parseInt(stack.pop());
        int num1 = Integer.parseInt(stack.pop());
        int result = 0;
        stack.push(evaluate(num1, num2, op) + "");
    }

    private int evaluate(int num1, int num2, String op) {
        switch(op) {
            case "+":
                return num1 + num2;
            case "-":
                return num1 - num2;
            case "*":
                return num1 * num2;
            case "/":
                if (num2 == 0) {
                    return 0;
                }
                return num1 / num2;
        }
        return 0;
    }
}
