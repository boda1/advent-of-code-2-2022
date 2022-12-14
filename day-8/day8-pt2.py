column_index = 0
row_index = 0
tree_columns = []
tree_rows = []
all_tree_columns = []
list_of_scenic_scores = []


def get_scenic_score(current_tree_to_check, trees):
    if trees:
        scenic_score = 0
        for tree in trees:
            tree = int(tree)
            if current_tree_to_check > tree:
                scenic_score += 1
            elif current_tree_to_check <= tree:
                scenic_score += 1
                break
        return scenic_score
    else:
        return 0


with open('input.txt') as f:
    file_content = f.read().split('\n')
    all_tree_rows = [list(row) for row in file_content]
    row_length = len(all_tree_rows[0])
    column_height = len(all_tree_rows)

    for i in range(len(file_content[0])):
        all_tree_columns.append([str(list(row)[i]) for row in file_content])

    for column in range(column_height):
        for row in range(row_length):
            current_tree = int(all_tree_rows[column][row])
            trees_left = all_tree_rows[column][:row]
            trees_right = all_tree_rows[column][row + 1:]
            trees_above = all_tree_columns[row][:column]
            trees_below = all_tree_columns[row][column + 1:]
            trees_to_check = []

            # Reverse list for trees above and to the left so that we start by checking value closest to current tree

            trees_above.reverse()
            trees_left.reverse()

            # Call function to get score for each direction, multiple all directions together, and append to list of all scores

            list_of_scenic_scores.append(get_scenic_score(current_tree, trees_left) *
                                         get_scenic_score(current_tree, trees_right) *
                                         get_scenic_score(current_tree, trees_above) *
                                         get_scenic_score(current_tree, trees_below))


print(f"Highest value: {sorted(list_of_scenic_scores)[-1]}")






