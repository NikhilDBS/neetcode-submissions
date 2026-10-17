class Solution:

  def isValid(self, s: str) -> bool:
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Pop the top element from the stack if it's not empty, else use a dummy value
        top_element = stack.pop() if stack else "#"

        # If the extracted opening bracket doesn't match, it's invalid
        if mapping[char] != top_element:
          return False
      else:
        # If it's an opening bracket, push it to the stack
        stack.append(char)

    # If the stack is empty, all brackets matched successfully
    return not stack