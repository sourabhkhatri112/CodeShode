import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Employee implements Comparable<Employee>{
	int id;
	String name;
	
	Employee(int id, String name){
		this.id = id;
		this.name = name;
	}
	
	public int compareTo(Employee emp){
		return this.id - emp.id;	// This will sort the IDs in Ascending
		return emp.id - this.id;		// This will sort the IDs in Descending
		return this.name.length() - emp.name.length();	// This will sort the names in Ascending
		return emp.name.length() - this.name.length();	// This will sort the names in Descending
	}
}

class TestMain{
    public static void main(String[] args){
        List<Employee> list = new ArrayList<>();
		list.add(new Employee(4,"Mainampatty"));
		list.add(new Employee(2,"Devvrat"));
		list.add(new Employee(3,"Rajesh"));
		list.add(new Employee(1,"Salma"));
		
		Collections.sort(list);
		
		for(Employee emp : list){
			System.out.println("ID: " + emp.id + " " + "Name: " + emp.name);
		}
    }
}