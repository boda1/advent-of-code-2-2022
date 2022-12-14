column_index = 0
row_index = 0
tree_columns = []
tree_rows = []
all_tree_columns = []
visible_trees = 0

with open('input.txt') as f:
    file_content = f.read().split('\n')
    all_tree_rows = [list(row) for row in file_content]
    row_length = len(all_tree_rows[0])
    column_height = len(all_tree_rows)
    for i in range(len(file_content[0])):
        all_tree_columns.append([str(list(row)[i]) for row in file_content])

    print(f"All tree rows: {all_tree_rows}, All tree columns: {all_tree_columns}, Row length: {row_length}, Column height: {column_height}")

    for column in range(column_height):
        for row in range(row_length):
            current_tree = all_tree_rows[column][row]
            trees_left = all_tree_rows[column][:row]
            trees_right = all_tree_rows[column][row + 1:]
            trees_above = all_tree_columns[row][:column]
            trees_below = all_tree_columns[row][column + 1:]
            trees_to_check = []

            print("Column: ", column, "Row: ", row, "Current tree: ", current_tree, "Trees to the left", trees_left, "Trees to the right: ", trees_right, "Trees above", trees_above, "Trees below", trees_below)

            trees_left.sort()
            trees_right.sort()
            trees_above.sort()
            trees_below.sort()

            if column == 0 or row == 0 or column == column_height - 1 or row == row_length - 1:
                visible_trees += 1
            elif trees_right and current_tree > trees_right[-1]:
                visible_trees += 1
            elif trees_left and current_tree > trees_left[-1]:
                visible_trees += 1
            elif trees_above and current_tree > trees_above[-1]:
                visible_trees += 1
            elif trees_below and current_tree > trees_below[-1]:
                visible_trees += 1


print("Number of visible trees: ", visible_trees)