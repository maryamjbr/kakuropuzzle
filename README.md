# Kakuro Puzzle Solver

This Python script solves Kakuro puzzles, a type of logic puzzle that is often referred to as a mathematical crossword. The script employs techniques from constraint satisfaction problems (CSP) and uses backtracking with forward checking to efficiently find solutions.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Script

1. Clone the repository:
    ```bash
    git clone https://github.com/maryamjbr/kakuropuzzle.git
    cd kakuropuzzle
    ```

2. Run the script:
    ```bash
    python kakuro.py
    ```

## How it Works

### Classes

- **Cell**: Represents a single cell in the puzzle.
  - `x`, `y`: Coordinates of the cell in the matrix.
  - `value`: Current value of the cell.

- **Partition**: Represents a row or column partition with a guide number and a list of cells.
  - `guide_num`: The sum that the partition's cells must achieve.
  - `cells`: List of cells in the partition.
  - `is_row`: Boolean indicating if the partition is a row or column.

### Functions

- **find_partition(m, w, h)**: Identifies and returns the partitions and cell list from the matrix.
- **is_solved(cell)**: Checks if the current cell assignment solves the partition.
- **update_partition(cell, value)**: Updates the cell's value in its partition.
- **solve_puzzle(cell_number)**: Recursively solves the puzzle using CSP backtracking and forward checking.
- **printKakuro(matrix)**: Prints the Kakuro puzzle in a readable format.

### Techniques

#### Constraint Satisfaction Problem (CSP)

The Kakuro puzzle is treated as a CSP, where:
- **Variables**: Each empty cell in the puzzle.
- **Domains**: Possible values for each cell (1-9).
- **Constraints**: Each partition must sum to its guide number without repeating values.

#### Backtracking

The `solve_puzzle` function uses backtracking to explore possible values for each cell:
1. Assign a value to a cell.
2. Check if the current assignment is valid (all constraints are satisfied).
3. If valid, proceed to the next cell.
4. If invalid, backtrack by removing the value and trying the next possibility.

#### Forward Checking

Forward checking is used to improve the efficiency of backtracking by:
- Checking constraints as soon as a value is assigned to a cell.
- Preventing assignments that would violate constraints in the future.
- Reducing the search space by eliminating invalid values early.

### Example Matrix

The script includes an example matrix defined as `matrix2`. This matrix represents the Kakuro puzzle to be solved. You can modify this matrix with your own Kakuro puzzle.

```python
matrix2=[
    ["*", "*", "*", [17,"*"], [19,"*"], "*", "*",[7,"*"],[44,"*"],"*"],
    ["*",[3,"*"] , [37, 17], 0, 0,"*", ["*",10],0,0, [23,"*"]],
    [["*",20], 0, 0, 0, 0,[6,"*"],[3,15],0,0, 0],
    [["*",5], 0, 0 ,[3,25],0, 0,0,0,0, 0],
    ["*",["*",8] ,0,0,["*",3] ,0,0,[10,15],0,0],
    ["*", [13,3],0, 0, [7,"*"], [5,"*"],["*",17],0, 0,"*"],
    [["*",9] ,0,0, [10,3],0, 0, [16,6] ,0,0, [11,"*"]],
    [["*",38],0, 0,  0, 0,0, 0,[3,17],0,0],
    [["*",7] ,0,0,0,"*",["*",12] ,0,0,0,0],
    ["*", ["*",4]  , 0 , 0, "*",["*",3] , 0, 0,"*","*"]
]
```
### Output
The script will print the solved Kakuro puzzle and the time taken to solve it.

```python
■	■	■	■\17	■\19	■	■	7\■	44\■	■	
■	3\■	37\17	5	6	■	■\10	4	9	23\■	
■\20	1	2	3	4	■\6	3\15	6	7	8	
■\5	5	6	■\3	7	8	9	■	■	■	
■	■\8	1	2	■\3	6	7	■\10	4	5	
■	13\3	4	5	■\7	■\5	■\17	6	7	■	
■\9	2	3	■\10	4	5	■\16	6	7	■\11	
■\38	4	5	6	7	■	■	■\3	■	■	
■\7	1	2	■	■\12	3	■	■	■	■	
■	■\4	3	■	■	■\3	■	■	■	■
0.20640921592712402
```
