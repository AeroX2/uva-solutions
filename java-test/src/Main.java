import java.util.*;

public class Main {
	private static List<List<String>> recursion(List<String> letters, String[] constraints, List<String> blub) {
		for (String constraint : constraints) {
			int a = blub.indexOf(String.valueOf(constraint.charAt(0)));
			int b = blub.indexOf(String.valueOf(constraint.charAt(2)));
			if (a == -1 || b == -1) continue;
			if (a > b) return null;
		}

		if (letters.size() <= 0) {
		    ArrayList<List<String>> a = new ArrayList<>();
		    a.add(blub);
		    return a;
		}

		ArrayList<List<String>> output = new ArrayList<>();

		for (int i = 0; i < letters.size(); i++) {

			List<String> letters_copy = new ArrayList<>(letters);
			letters_copy.remove(i);

			List<String> blub_copy = new ArrayList<>(blub);
			blub_copy.add(letters.get(i));

			List<List<String>> result = recursion(letters_copy,constraints,blub_copy);
			if (result != null && result.size() > 0) {
				output.addAll(result);
			}
		}

		return output;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = Integer.valueOf(input.nextLine());
		for (int i=0; i<n; i++) {
			input.nextLine();
			List<String> letters = Arrays.asList(input.nextLine().split(" "));
			String[] constraints = input.nextLine().split(" ");

			Collections.sort(letters);
			for (List<String> s : recursion(letters, constraints, new ArrayList<>())) {
				System.out.println(String.join(" ", s));
			}
			if (i != n-1) System.out.println();
		}
	}
}
