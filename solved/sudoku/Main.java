import java.util.*;
import java.util.ArrayList;
import java.util.stream.Collectors;

/**
 * Sudoku checker.
 */
public class Main {
  private static class Sudoku {
    private class Cell {
      ArrayList<Integer> potentials;
      final int i,j;

      Cell(int i, int j) {
        this.potentials = new ArrayList<>();
        this.i = i;
        this.j = j;
      }

      Cell copy() {
        Cell cell = new Cell(i, j);
        cell.potentials = new ArrayList<>(potentials);
        return cell;
      }
    }

    /**
     * Constructor for Sudoku.
     *
     * @param g The grid that defines the sudoku
     */
    public Sudoku(int[][] g) {
      theGrid = g;
      subGridSize = (int) Math.sqrt(g.length);
    }

    /**
     * Secondary constructor for Sudoku.
     *
     * @param g   The grid that defines the sudoku
     * @param e   The value that denotes an empty cell
     */
    public Sudoku(int[][] g, int e) {
      this(g);
      emptyValue = e;
    }

    //The n x m grid that defines the Sudoku.
    private int[][] theGrid;
    //Value denoting an empty cell
    private int emptyValue = -1;
    //Size of grids inside theGrid ((int) sqrt(length))
    private final int subGridSize;
    //Sets
    private int[] rowSet;
    private int[] columnSet;
    private int[] blockSet;

    /**
     * Check validity of a Sudoku grid.
     *
     * @return true if and only if theGrid is a valid Sudoku
     */
    public boolean isValid() {
      //Check size of grid
      int size = theGrid.length;
      if (size == 0) {
        return true;
      }

      //Check if the size is a square number
      if (subGridSize * subGridSize != size) {
        return false;
      }

      rowSet = new int[size];
      columnSet = new int[size];
      blockSet = new int[size];

      for (int i = 0; i < size; i++) {
        //Check if the grid is square
        if (theGrid[i].length != size) {
          return false;
        }

        for (int j = 0; j < size; j++) {
          int number = theGrid[i][j];

          //Check the number are within range
          if (number == emptyValue) {
            continue;
          }

          if (number < 1 || number > size) {
            return false;
          }

          //Check for duplicate numbers
          //This is done by storing each number as a bit in an integer
          int mask = 1 << (number - 1);

          if ((rowSet[i] & mask) > 0) {
            return false;
          }
          rowSet[i] |= mask;

          if ((columnSet[j] & mask) > 0) {
            return false;
          }
          columnSet[j] |= mask;

          //The block is the block number
          //Example of a 9 by 9 grid block values
          // 0 0 0 1 1 1 2 2 2
          // 0 0 0 1 1 1 2 2 2
          // 0 0 0 1 1 1 2 2 2
          // 3 3 3 4 4 4 5 5 5
          // 3 3 3 4 4 4 5 5 5
          // 3 3 3 4 4 4 5 5 5
          // 6 6 6 7 7 7 8 8 8
          // 6 6 6 7 7 7 8 8 8
          // 6 6 6 7 7 7 8 8 8

          int block = getBlock(i, j);
          if ((blockSet[block] & mask) > 0) {
            return false;
          }
          blockSet[block] |= mask;
        }
      }

      return true;
    }

    /**
     *   Attempt to efficiently compute a solution to the Sudoku.
     *
     *   @return  A grid with possibly less empty cells than in theGrid (but not more)
     *
     *   @note    If there is no empty cell in the result, then the Sudoku is solved,
     *            otherwise it is not
     */
    public boolean fastSolve() {
      if (!isValid()) {
        return false;
      }

      return fastSolveHelper();
    }

    private boolean fastSolveHelper() {

      ArrayList<Cell> potentials;
      boolean guessingTime = false;
      do {
        //Find all the potential values for every cell
        potentials = markPotentials();

        outer: {
          //If there is a cell with only one potential, mark that cell
          //and redo the potentials
          for (Cell cell : potentials) {
            if (cell.potentials.size() == 1) {
              theGrid[cell.i][cell.j] = cell.potentials.get(0);
              break outer;
            }
          }
          guessingTime = true;
        }

      } while (!guessingTime);

      return backtrackFast(0,potentials);
    }

    private ArrayList<Cell> markPotentials() {
      //Calculate the grids sets
      isValid();

      ArrayList<Cell> potentials = new ArrayList<>();

      int size = theGrid.length;
      for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
          if (theGrid[i][j] != emptyValue) {
            continue;
          }

          int block = getBlock(i, j);
          int potential = ~(rowSet[i] | columnSet[j] | blockSet[block]);

          Cell cell = new Cell(i, j);

          //Convert binary positions to numbers
          for (int s = 0; s < size; s++) {
            if ((potential & (0b1 << s)) > 0) {
              cell.potentials.add(s+1);
            }
          }

          if (cell.potentials.size() > 0) {
            potentials.add(cell);
          }
        }
      }

      return potentials;
    }

    private boolean backtrackFast(int depth, ArrayList<Cell> potentials) {
      //When there are no more potential values left we are done
      if (potentials.size() <= 0) {
        return true;
      }

      //Find the cell with the lowest amount of potentials, keep it and remove it from the array
      Cell cell = potentials.stream().min(Comparator.comparingInt((c) -> c.potentials.size())).orElseGet(null);
      potentials.remove(cell);

      for (int num : cell.potentials) {

        theGrid[cell.i][cell.j] = num;

        //Make a copy of the partial solution
        //copyGridToPrevious();

        //Remove all the same potentials from other cells
        ArrayList<Cell> potentialsCopy = new ArrayList<>();
        for (Cell otherCell : potentials) {

          int block = getBlock(cell.i, cell.j);
          int otherBlock = getBlock(otherCell.i, otherCell.j);

          Cell other = otherCell.copy();
          if (cell.i == otherCell.i ||
              cell.j == otherCell.j ||
              block == otherBlock) {
            other.potentials.remove(Integer.valueOf(num));
          }

          if (cell.potentials.size() > 0) {
            potentialsCopy.add(other);
          }
        }

        //Attempt new grid
        if (backtrackFast(depth+1, potentialsCopy)) {
          return true;
        }

        //Revert grid
        theGrid[cell.i][cell.j] = emptyValue;
      }

      return false;
    }

    /**
     * Prints out theGrid to stdout in human readable form.
     */
    public void prettyPrint() {
      for (int[] arr : theGrid) {
        String string = Arrays.stream(arr)
      	  			.mapToObj(String::valueOf)
      				.collect(Collectors.joining(" "));
        System.out.println(string);
      }
      System.out.println();
    }

    private int getBlock(int i, int j) {
      //Integer division, don't remove /subGridSize*subGridSize
      return i / subGridSize * subGridSize + j / subGridSize;
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String line;
    do {
      line = scanner.nextLine();
      int n = Integer.parseInt(line.trim());
      int grid[][] = new int[n*n][];

      for (int i = 0; i < n * n; i++) {
        line = scanner.nextLine();
        grid[i] = Arrays.stream(line.split(" "))
          .map(String::trim)
          .map(Integer::parseInt)
          .mapToInt(Integer::intValue)
          .toArray();
      }

      Sudoku sudoku = new Sudoku(grid,0);
      if (sudoku.fastSolve()) {
		  sudoku.prettyPrint();
	  } else {
		  System.out.println("NO SOLUTION");
	  }

	  line = null;
	  if (scanner.hasNextLine()) {
        line = scanner.nextLine();
	  }
    } while (line != null);
  }

}

