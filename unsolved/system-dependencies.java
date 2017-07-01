import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.AbstractMap.*;

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

class Main {
	
	public static void main(String[] args) {
		Main m = new Main();

		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNextLine()) {
			String input = scanner.nextLine();
			m.parse(input);
		}
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

	private void parse(String command) {
		//Echo command

		String[] args = command.split("\\s+");
		//System.out.println(Arrays.toString(args));
		switch (args[0]) {
			case "DEPEND":
				System.out.println(command);
				depends(args[1], Arrays.copyOfRange(args, 2, args.length));
				break;

			case "INSTALL":
				System.out.println(command);
				if (!cancelCommands) install(args[1]);
				break;

			case "REMOVE":
				System.out.println(command);
				if (!cancelCommands) remove(args[1]);
				break;

			case "LIST":
				System.out.println(command);
				if (!cancelCommands) list();
				break;

			case "END":
				System.out.println(command);
				break;
		}
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

	private void depends(String program, String[] requires) {
		Node parent = dependencies.get(program);
		if (parent == null) {
			parent = new Node(program, new ArrayList<Node>(), null);
		}
		ArrayList<Node> requirements = new ArrayList<>();

		for (String requirement : requires) {
			Node node = dependencies.computeIfAbsent(requirement, r -> new Node(r, new ArrayList<Node>(), new ArrayList<Node>()));
			node.parents.add(parent);
			requirements.add(node);
		}
		parent.children = requirements;

		//Reset seen
		seen = new HashSet<>();
		int[] minimax = traverseUp(parent, 0, program);

		if ((minimax[0] != Integer.MAX_VALUE && minimax[1] != Integer.MIN_VALUE) || cancelCommands) {
			print("Found cycle in dependencies");
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
		if (installed.contains(program)) {
			print(program, "is already installed.");
			return;
		}

		explicityInstalled.add(program);

		//Get the programs dependencies
		Node node = dependencies.get(program);
		if (node != null) installHelper(node);
		else {
			//If it is not in dependencies, it has no children and can be installed
			print("Installing", program);
			installed.add(program);
		}
	}

	private void removeHelper(Node child) {
		if (!installed.contains(child.program)) return;
		if (explicityInstalled.contains(child.program)) return;

		boolean remove = true;
		for (Node parent : child.parents) {
			if (installed.contains(parent.program)) {
				remove = false;
				break;
			}
		}

		if (remove) {
			print("Removing", child.program);
			installed.remove(child.program);
		}

		for (Node node : child.children) {
			removeHelper(node);
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
		if (node != null) {
			for (Node parent : node.parents) {
				if (installed.contains(parent.program)) {
					print(program, "is still needed");
					return;
				}
			}
		}

		explicityInstalled.remove(program);
		if (node != null) removeHelper(node);
	}

	private void list() {
		for (String program : installed) print(program);
	}

	private void print(String... lines) {
		System.out.print("  ");
		for (String line : lines) System.out.print(" "+line);
		System.out.println();
	}
}
		

