class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area

# The stack stores indices of bars whose maximum rectangle
# cannot yet be determined.
#
# The stack is maintained in increasing height order.
#
# When we encounter a shorter bar, we know that the taller bars
# on top of the stack can no longer extend further to the right.
# Therefore, this is the moment when we can calculate their
# largest possible rectangle.
#
# For a popped bar:
#   - the current index i is the first smaller bar on the right
#   - stack[-1] (after popping) is the first smaller bar on the left
#
# Therefore:
#   width = right_smaller - left_smaller - 1
#
# If the stack becomes empty after popping, there is no smaller
# bar on the left, so the rectangle extends all the way to index 0.
#
# A sentinel bar of height 0 is appended to force every remaining
# bar out of the stack so that all rectangles get processed.
#
# Each index is pushed once and popped once, giving O(n) time.
