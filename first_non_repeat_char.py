# WORK SOLUATION
# Python 3
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
# First non-repeating letter
# 找到第一个非重复的单个字符 (大小写不敏感)
# input  'stress'
# output 't'
# 如果全是重复的就返回  ""


# 思路1：用一个字典来计数，循环整个字符串一次，然后字符和出现次数就都在字典里了
# 然后从前往后看字典，第一个碰到 value 为 1 的就是了.
def first_non_repeating_letter(string):
  order = []
  counts = {}
  for x in string:
    x = x.lower()
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
    order.append(x) # this make sure order is same as string

  for idx, val in enumerate(order):
    if counts[val] == 1:
      return string[idx]
  # get right index, this make case insensetive work

  return ""

# 这里用了字典和列表我想是因为 order [] 是为了跟踪顺序
# 而字典是没有顺序的。

## Reference
# https://www.quora.com/How-do-I-find-the-first-non-repeated-character-of-a-given-string
# http://stackoverflow.com/questions/15495731/best-way-to-find-first-non-repeating-character-in-a-string
# http://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/


## Codewar 里最高票的简洁答案：
# 管用，先转小写，然后循环小写，用了 string 的 count 方法来做统计，最后返回原字符里相同 index 的字符，解决了大小写不敏感的问题。
# clever
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""
