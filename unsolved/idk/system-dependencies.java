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

	private HashMap<String, Node> dependencies;
	private Set<String> installed;
	private Set<String> explicityInstalled;

	public Main() {
	    dependencies = new HashMap<>();
		installed = new LinkedHashSet<>();
		explicityInstalled = new HashSet<>();
	}

	private void parse(String command) {
		//Echo command
		System.out.println(command);

		String[] args = command.split("\\s+");
		switch (args[0]) {

			case "DEPEND":
				depends(args[1], Arrays.copyOfRange(args, 2, args.length));
				break;

			case "INSTALL":
				install(args[1]);
				break;

			case "REMOVE":
				remove(args[1]);
				break;

			case "LIST":
				list();
				break;
		}
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
					print(program, "is still needed.");
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
		

