class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            if token in '+-*/':
                self.evalStack(stack, token)
            else:
                stack.append(token)
        return int(stack.pop())

    def evalStack(self, stack, op):
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(str(self.evaluate(num1, num2, op)))

    def evaluate(self, num1, num2, operand) -> int:
        num1 = int(num1)
        num2 = int(num2)
        if operand == '+':
            return num1 + num2
        if operand == "-":
            return num1 - num2
        if operand == "*":
            return num1 * num2
        if num2 == 0:
            return 0
        return int(num1 / num2)
        