class Solution(object):
    def prefixCount(self, words, pref):
      return len([word for word in words if word.statswith(pref)]}
