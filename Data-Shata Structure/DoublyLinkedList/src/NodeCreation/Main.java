package NodeCreation;

// In this page I will provide a simple example on how to create a node
// That's it
class Node{
    int data;   // A node contains data
    Node next;  // A node contains address to the next node

    Node prev;  // A node also contains address to the previous node

    // Next in order to create any node we are supposed to create a constructor
    // Hence our node is finally created.
    public Node(int data){
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}