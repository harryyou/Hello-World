#!/usr/bin/env python3
#coding：utf-8

from collections import deque

#构建一个散列表
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#搜索条件
def what_we_find(name):
	return name[-1] == 'm'

#广度优先搜索
def bfs(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if what_we_find(person):
				print("we find it!,{}".format(person))
				return True
			else:
				search_queue += graph[person]
				searched.append(person)

	return False

if __name__ == "__main__":
	bfs('you')