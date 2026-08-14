class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # construct adjacency list of 1 letter transforms
        # do a bfs

        adj_list = dict()

        wordList.append(beginWord)
        for word in wordList:
            adj_list[word] = set()
        
        def is_one_char_away(word1, word2):
            i = 0
            diff = 0
            while i < len(word1):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff > 1:
                        return False
                i += 1
            return True

        for w1 in range(len(wordList)):
            for w2 in range(w1+1, len(wordList)):
                if is_one_char_away(wordList[w1], wordList[w2]):
                    adj_list[wordList[w1]].add(wordList[w2])
                    adj_list[wordList[w2]].add(wordList[w1])
        
        # bfs
        queue = [beginWord]
        visited = set()
        count = 0

        while queue:
            children = []
            for word in queue:
                if word == endWord:
                    return count+1 # need no. of nodes

                visited.add(word)
                
                for neighbor in adj_list[word]:
                    if neighbor not in visited:
                        children.append(neighbor)
            
            if children:
                count += 1
            queue = children
            # print(children)
            # print(count)
        
        return 0


        