import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.AbstractMap.*;

class Main {
	
	public static void main(String[] args) {
		
		Main m = new Main();

		Vector<String> commands = new Vector<>();
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		while (!input.equals("END")) {
			commands.add(input);
			input = scanner.nextLine();
			//System.out.println(input);
		}
		m.runNCommands(commands, commands.size()+1);
	}
	
	public final Integer MAXCOMS = 1000;

	class Node {
		String program;
		ArrayList<Node> parents;
		ArrayList<Node> children;

		Node(String program, ArrayList<Node> parent, ArrayList<Node> dependencies) {
			this.program = program;
			this.parents = parent;
			this.children = dependencies;
		}
	}

	enum Level {
		PASS,
		CREDIT,
		DISTINCTION_SMALL,
		DISTINCTION_LARGE
	}

	private boolean cancelCommands = false;
	private HashMap<String, Node> dependencies;
	private Set<String> installed;
	private Set<String> explicityInstalled;

	private SimpleEntry<Integer, String> smallestCycle = new SimpleEntry<>(Integer.MAX_VALUE, "");
	private SimpleEntry<Integer, String> largestCycle = new SimpleEntry<>(Integer.MIN_VALUE, "");

	public Main() {
	    dependencies = new HashMap<>();
		installed = new LinkedHashSet<>();
		explicityInstalled = new HashSet<>();
	}

	private void parse(Vector<String> commands, Integer N, Level level) {
		for (String command : commands.subList(0, Math.min(commands.size(), N))) {
			//Echo command
			System.out.println(command);

			String[] args = command.split("\\s+");
			//System.out.println(Arrays.toString(args));
			switch (args[0]) {
				case "DEPEND":
					depends(args[1], Arrays.copyOfRange(args, 2, args.length), level);
					break;

				case "INSTALL":
					if (!cancelCommands) install(args[1]);
					break;

				case "REMOVE":
					if (!cancelCommands) remove(args[1]);
					break;

				case "LIST":
					if (!cancelCommands) list();
					break;
			}
		}
		System.out.println("END");
	}

	//Already seen nodes while traversing the tree
	private Set<String> seen;
	private int[] traverseUp(Node child, int level, String compare) {
		if (child.parents.size() == 0) return new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};

		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		for (Node parent : child.parents) {
			if (parent.program.equals(compare)) return new int[]{level, level};

			if (seen.contains(parent.program)) continue;
			seen.add(parent.program);

			int[] result = traverseUp(parent, level+1, compare);
			min = Math.min(min, result[0]);
			max = Math.max(max, result[1]);
		}
		return new int[]{min, max};
	}

	private void depends(String program, String[] requires, Level level) {
		Node parent = dependencies.get(program);
		if (parent == null) {
			parent = new Node(program, new ArrayList<Node>(), null);
		}
		ArrayList<Node> requirements = new ArrayList<>();

		for (String requirement : requires) {
			Node node = dependencies.get(requirement);
			if (node == null) {
				node = new Node(requirement, new ArrayList<Node>(), new ArrayList<Node>());
				dependencies.put(requirement, node);
			}
			node.parents.add(parent);
			requirements.add(node);
		}
		parent.children = requirements;

		//Reset seen
		seen = new HashSet<>();
		int[] minimax = traverseUp(parent, 0, program);
		
		if ((minimax[0] != Integer.MAX_VALUE && minimax[1] != Integer.MIN_VALUE) || cancelCommands) {
			print("Found cycle in dependencies");

			if (level == Level.DISTINCTION_SMALL || level == Level.DISTINCTION_LARGE) {
				//I'm not sure if we can use Java 8 with String.join()
				if (minimax[0] <= smallestCycle.getKey()) {
					StringBuilder string = new StringBuilder(program);
					for (String i : requires) string.append(" ").append(i);
					smallestCycle = new SimpleEntry<>(minimax[0], string.toString());
				}

				if (minimax[1] >= largestCycle.getKey()) {
					StringBuilder string = new StringBuilder(program);
					for (String i : requires) string.append(" ").append(i);
					largestCycle = new SimpleEntry<>(minimax[1], string.toString());
				}
				print("Suggest removing DEPEND", level == Level.DISTINCTION_SMALL ? smallestCycle.getValue() : largestCycle.getValue());
			}

			cancelCommands = true;
		}

		dependencies.put(program, parent);
	}

	//I wonder if this can be done with a stack?
	private void installHelper(Node root) {
		if (installed.contains(root.program)) return;
	
		if (root.children != null) {
			for (Node requirement : root.children) {
				installHelper(requirement);
			}
		}
		
		print("Installing", root.program);
		installed.add(root.program);
	}
	
	private void install(String program) {
		explicityInstalled.add(program);
		
		if (installed.contains(program)) {
			print(program, "is already installed.");
			return;
		}

		//Get the programs dependencies
		Node node = dependencies.get(program);
		if (node != null) installHelper(node);
		else {
			//If it is not in dependencies, it has no children and can be installed
			print("Installing", program);
			installed.add(program);
		}
	}

	private void remove(String program) {
		//System.out.println(explicityInstalled);
		
		if (!installed.contains(program)) {
			print(program, "is not installed.");
			return;
		}
		
		//First check if it is required
		Node node = dependencies.get(program);
		for (Node parent : node.parents) {
			if (installed.contains(parent.program)) {
				print(program, "is still needed");
				return;
			}
		}
		
		//Start to remove it
		print("Removing", program);
		installed.remove(program);
		explicityInstalled.remove(program);

		Stack<Node> todo = new Stack<>();
		for (Node child : node.children) todo.add(child);
		
		while (!todo.empty()) {
			Node child = todo.pop();
			
			if (explicityInstalled.contains(child.program)) continue;
			
			boolean remove = true;
			for (Node parent : child.parents) {
				if (installed.contains(parent.program)) {
					remove = false;
					break;
				}
			}
			
			for (Node x : child.children) todo.add(x);
			
			if (remove) {
				print("Removing", child.program);
				installed.remove(child.program);
			}
		}
	}

	private void list() {
		for (String program : installed) print(program);
	}

	private void print(String... lines) {
		System.out.print("  ");
		for (String line : lines) System.out.print(" "+line);
		System.out.println();
	}

	public void runNCommands (Vector<String> commands, Integer N) {
		// PRE: commands contains set of commands read in by readCommandsFromFile()
		// POST: executed min(N, all) commands
		parse(commands, N, Level.PASS);
	}
	
	public void runNCommandswCheck (Vector<String> commands, Integer N) {
		// PRE: commands contains set of commands read in by readCommandsFromFile()
		// POST: executed min(N, all) commands, checking for cycles
		parse(commands, N, Level.CREDIT);
	}
	
	public void runNCommandswCheckRecLarge (Vector<String> commands, Integer N) {
		// PRE: commands contains set of commands read in by readCommandsFromFile()
		// POST: executed min(N, all) commands, checking for cycles and 
		//       recommending fix by removing largest cycle
		parse(commands, N, Level.DISTINCTION_LARGE);
	}

	public void runNCommandswCheckRecSmall (Vector<String> commands, Integer N) {
		// PRE: commands contains set of commands read in by readCommandsFromFile()
		// POST: executed min(N, all) commands, checking for cycles and 
		//       recommending fix by removing smallest cycle
		parse(commands, N, Level.DISTINCTION_SMALL);
	}
}
		

