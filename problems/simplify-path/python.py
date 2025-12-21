class Solution:
    def simplifyPath(self, path: str) -> str:
        sections = path.split("/")
        #print(sections)
        
        i = 0
        stack = []
        while i < len(sections):
            section = sections[i]
            i += 1
            if section == "" or section == ".":
                continue
            if section == "..":
                if len(stack) > 0:
                    stack.pop()
                continue

            stack.append(section)
        #print(stack)

        return "/" + "/".join(stack)
        