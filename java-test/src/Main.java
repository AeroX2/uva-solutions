import java.util.*;
import java.util.stream.Collectors;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
	    while (true) {
			int n = Integer.parseInt(input.nextLine());
			if (n == 0) break;

			int total = 0;
			ArrayList<Integer> hoax = new ArrayList<>();
			for (int i = 0; i < n; i++) {
				String[] s = input.nextLine().split(" ");
				List<Integer> t = Arrays.stream(s).skip(1).map(Integer::parseInt).collect(Collectors.toList());
				hoax.addAll(t);
				Collections.sort(hoax);

				total += hoax.get(hoax.size()-1)-hoax.get(0);

				hoax.remove(hoax.size()-1);
				hoax.remove(0);
			}
			System.out.println(total);
		}
	}
}
