#Backtracking is a form of depth-first search (DFS). \
# For a certain search tree (which records the path and state judgment), \
# the main difference between backtracking and DFS is that backtracking does not \
# retain the complete tree structure in the solving process, while depth-based search \
# records the complete search tree.

# template from LeetCode
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
#/////////////////////////////////////////////////////////////////////////////
# Template from a different place
# General structure of backtracking
function dfs(current_status):
      if(condition):
        record or output
        return
      for i in range(something):       #traverse all the nodes of solution tree
            Generate child parameters
           if(condition):
              dfs(child condition)
           recover #(backtracking part)