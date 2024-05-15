
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * @author SOURABH KHATRI Streams -> Performing bulk operations over Collections
 */

class MapInsertion {
	int key;
	String value;

	public MapInsertion(int key, String value) {
		super();
		this.key = key;
		this.value = value;
	}
 
	public MapInsertion() {
		
	}
	
	 void Operations() {
		List<MapInsertion> list = new ArrayList<>();
		list.add(new MapInsertion(10, "Sourabh"));
		list.add(new MapInsertion(20, "Rahul"));
		list.add(new MapInsertion(30, "Raj"));
		list.add(new MapInsertion(40, "Rohan"));

		 /* Below stream operation is responsible for sending Arraylist inside Maps
		 * by making the use of JAVA8 streams.
		 *
		 * Output: {20=Rahul, 40=Rohan, 10=Sourabh, 30=Raj}
		 * */
		
		System.out.println(list.stream().collect(Collectors.toMap(i -> i.key, i -> i.value)));
	 }
}

class Employee {
	String name;
	int salary;
	int age;

	public Employee(String name, int salary, int age) {
		super();
		this.name = name;
		this.salary = salary;
		this.age = age;
	}

	public Employee() {
	}

	void EmployeeOperations() {
		List<Employee> list = new ArrayList<>();
		list.add(new Employee("Rakesh", 10000, 23));
		list.add(new Employee("Sourabh", 100000, 28));
		list.add(new Employee("Rajesh", 90000, 27));
		list.add(new Employee("Rohan", 80000, 30));
		list.add(new Employee("Raj", 40000, 34));

		/*
		 * skip(3) - Skip first 3 elements of stream limit(3) - Prints ONLY first 3
		 * elements of stream OUTPUT - skip(3) : Rohan Raj LIMIT - limit(3) : Rakesh
		 * Sourabh Rajesh
		 */
		list.stream().skip(3).forEach(i -> System.out.print(i.name + " "));
		System.out.println();
		list.stream().limit(3).forEach(i -> System.out.print(i.name + " "));
		System.out.println();
		/*
		 * Find employee with Second HIGHEST Salary. How ? Step-1 : Sort by descending
		 * first Step-2 : skip(1) here used to skip the top employee Step-3 :
		 * findFirst() gets 1st element from remaining list findAny() return any element
		 * without specific order
		 * 
		 * OUTPUT : 90000
		 */
		Optional<Integer> salary = list.stream().sorted((o1, o2) -> {
			if (o1.salary > o2.salary)
				return -1;
			else if (o1.salary < o2.salary)
				return 1;
			else
				return 0;
		}).map(i -> i.salary).skip(1).findFirst();
		System.out.println(salary.get());

		/*
		 * Find average salary of employee above the age of 30 average() - mapToint() is
		 * a mandatory function for perform average
		 * 
		 * OUTPUT : 60000.0
		 */
		OptionalDouble average = list.stream().filter(i -> i.age >= 30).mapToInt(i -> i.salary).average();
		System.out.println(average.getAsDouble());

		/*
		 * Both operations below are able to find the SUM of all salaries sum(),
		 * average(), max() or min() must require mapToInt reduce() -> 0 here means
		 * values getting added to zero consecutively
		 * 
		 * Both finding max_salary below. One using mapToInt while other using reduce.
		 */
		int max_salary_1 = list.stream().mapToInt(i -> i.salary).sum();
		System.out.println("Max salary : " + max_salary_1);
		int max_salary_2 = list.stream().map(i -> i.salary).reduce(0, (a, b) -> (a + b));
		System.out.println("max salary: " + max_salary_2);

	}
}

public class Streams {
	List<String> fruits = Arrays.asList("apple", "banana", "apricot", "orange", "apple_pie");

	void filter(List<String> fruits) {
		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * startsWith() -> used inside filter() -> picks up array elements starting with
		 * prefix "a"
		 *
		 * Output: apple apricot apple pie
		 */
		fruits.stream().filter(i -> i.startsWith("a")).forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * contains() -> used inside filter() -> picks elements contains some prefix
		 * 
		 * Output: banana
		 */
		fruits.stream().filter(i -> i.contains("ana")).forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * i.length() -> used inside filter() -> printing elements > 6
		 * 
		 * Output: apricot apple pie
		 */
		fruits.stream().filter(i -> i.length() > 6).forEach(i -> System.out.print(i + " "));
	}

	/*
	 * MAP transforms stream elements. MAP is applied to each element independently.
	 * 
	 */
	void map(List<String> fruits) {
		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * toUpperCase() -> used inside map() -> convert array toUpperCase()
		 * 
		 * Output : APPLE BANANA APRICOT ORANGE APPLE PIE
		 */
		fruits.stream().map(i -> i.toUpperCase()).forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * i.substring(0,1) -> Begin_Index : 0 / End_Index : 1 i.substring(1) ->
		 * Begin_Index : 1 / End_Index : End of String
		 * 
		 * Output : Apple Banana Apricot Orange Apple pie
		 */
		fruits.stream().map(i -> i.substring(0, 1).toUpperCase() + i.substring(1))
				.forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "1", "2", "3", "4", "5" i -> Integer.valueOf(i) -> Converting each
		 * String element in List to Integer
		 * 
		 * Output : 1 2 3 4 5
		 */
		List<String> integerList = Arrays.asList("1", "2", "3", "4", "5");
		integerList.stream().map(i -> Integer.valueOf(i)).forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * mapToInt() -> Convert elements into Integers counterparts
		 * 
		 * Output : 5 6 7 6 9
		 */
		fruits.stream().mapToInt(i -> i.length()).forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * 
		 * .max().orElse(0) -> returns element with highest word length(in number)
		 * 
		 * -> "orElse(0)" is an OPTIONAL here(MANDATORY to declare here)
		 * 
		 * -> FOR EG. When Fruits are empty :- fruits = Arrays.asList(); -> Then,
		 * orElse(0) will run and print 0
		 * 
		 * Output : 9 // Greatest element in stream by length
		 */
		int max = fruits.stream().mapToInt(i -> i.length()).max().orElse(0);
		System.out.println(max);
	}

	void ComparatorOperations() {
		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 *
		 * sorted() -> sorted either naturally or based on comparator based Output :
		 * apple apple_pie apricot banana orange // Sorted naturally
		 */
		fruits.stream().sorted().forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 *
		 * sorted() -> sorted either naturally or based on comparator based Output :
		 * apple, banana, orange, apricot, apple_pie // Sorted comparator(length) based
		 */
		fruits.stream().sorted((o1, o2) -> {
			if (o1.length() > o2.length())
				return 1;
			else if (o1.length() < o2.length())
				return -1;
			else
				return 0;
		}).forEach(i -> System.out.print(i + " "));
		System.out.println();

		/*
		 * LIST : "apple", "banana", "apricot", "arange", "apple pie","asasan"
		 * 
		 * sorted() -> 1st sorting - length wise. If length is equal then 2nd sorting -
		 * done alphabetically
		 * 
		 * Output: apple arange asasan banana apricot apple pie
		 */
		fruits = Arrays.asList("apple", "banana", "apricot", "arange", "apple pie", "asasan");
		fruits.stream().sorted().sorted((o1, o2) -> {
			if (o1.length() > o2.length())
				return 1;
			else if (o1.length() < o2.length())
				return -1;
			else
				return 0;
		}).forEach(i -> System.out.print(i + " "));
	}

	void GroupingBy() {
		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * Collectors.groupingBy(i -> i.length()) -- Grouping words based on length
		 * 
		 * Output : {5=[apple], 6=[banana, orange], 7=[apricot], 9=[apple_pie]}
		 */
		fruits.stream().collect(Collectors.groupingBy(i -> i.length()))
				.forEach((length, wordList) -> System.out.println("Words with length " + length + ": " + wordList));

		/*
		 * LIST : "apple", "banana", "apricot", "orange", "apple pie"
		 * Collectors.groupingBy(i -> i.charAt(0)) -- Grouping based on first character
		 * 
		 * Output : {a=[apple, apricot, apple_pie], b=[banana], o=[orange]}
		 */
		System.out.println(fruits.stream().collect(Collectors.groupingBy(i -> i.charAt(0))));

		/*
		 * chars().mapToObj(i -> (char)i) -- This is mandatory is operation is to be
		 * performed over a String instead of list
		 * 
		 * Collectors.groupingBy(Function.identity(), Collectors.counting()) -- Finds
		 * out occurence of each alphabet
		 * 
		 * Output : {r=1, d=1, e=1, W=1, H=1, l=3, o=2}
		 */
		String str = "HelloWorld";
		System.out.println(str.chars().mapToObj(i -> (char) i)
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting())));

		/*
		 * Output : HELLOWORLD
		 */
		str.chars().mapToObj(ch -> (char) ch).map(ch -> Character.toUpperCase(ch)).forEach(i -> System.out.print(i));
	}

	public static void main(String[] args) {
		new MapInsertion().Operations();
		// new Streams().ComparatorOperations();
		// new Streams().GroupingBy();
		// new Employee().EmployeeOperations();
	}
}
