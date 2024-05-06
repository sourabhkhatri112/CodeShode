import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


class Employee implements Comparable<Employee>{
	int id;
	String name;
	int birthyear;
	
	Employee(int id, String name, int birthyear){
		this.id = id;
		this.name = name;
		this.birthyear = birthyear;
	}
	
	public int compareTo(Employee emp){
		return this.id - emp.id;	// This will sort the IDs in Ascending
		//return emp.id - this.id;		// This will sort the IDs in Descending
		//return this.name.length() - emp.name.length();	// This will sort the names in Ascending
		//return emp.name.length() - this.name.length();	// This will sort the names in Descending
	}
}

class IdComparator implements Comparator<Employee>{
	public int compare(Employee i1,Employee i2){
		if(i1.id > i2.id)
			return 1;
		else if(i1.id < i2.id)
			return -1;
		else return 0;
	}
}

class BirthComparator implements Comparator<Employee>{
	public int compare(Employee i1,Employee i2){
		if(i1.birthyear > i2.birthyear)
			return 1;
		else if(i1.birthyear < i2.birthyear)
			return -1;
		else return 0;
	}
}


class TestMain{
    public static void main(String[] args){
        List<Employee> list = new ArrayList<>();
		list.add(new Employee(4,"Mainampatty", 1982));
		list.add(new Employee(2,"Devvrat", 1981));
		list.add(new Employee(3,"Rajesh", 1975));
		list.add(new Employee(1,"Salma", 1979));
		
		Collections.sort(list);		// Sorting done through Comparable
		
		for(Employee emp : list){
			System.out.println("ID: " + emp.id + " " + "Name: " + emp.name);
		}
		
		IdComparator idComparator = new IdComparator();
		Collections.sort(list, idComparator);		// Sorting done through ID Comparator
		for(Employee emp : list){
			System.out.println("ID: " + emp.id + " Name: " + emp.name + "BirthYear: " + emp.birthyear);
		}
		
		BirthComparator birthComparator = new BirthComparator();
		Collections.sort(list, idComparator);		// Sorting done through ID Comparator
		for(Employee emp : list){
			System.out.println("ID: " + emp.id + " Name: " + emp.name + "BirthYear: " + emp.birthyear);
		}
		
    }
}