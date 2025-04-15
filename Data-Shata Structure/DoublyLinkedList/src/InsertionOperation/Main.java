package InsertionOperation;

// In this page I will provide a simple example on how to create a node
// That's it
class Node {
    int data;   // A node contains data
    Node next;  // A node contains address to the next node

    Node prev;  // A node also contains address to the previous node

    // Next in order to create any node we are supposed to create a constructor
    // Hence our node is finally created.
    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class Main {
    private Node head;

    public void Insert(int data) {
        // Create a train coach before you plan to attach it
        Node new_node = new Node(data);

        // If head is null, it means it is the first coach
        if (head == null) {
            head = new_node;
        } else if (head.next == null) {
            head.next = new_node;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;   // Go the the last coach of train
            }
            temp.next = new_node;   // Attach the coach to that last coach
            new_node.prev = temp;   // Previous now pointing to 2nd last coach
        }
    }

    public void traverseForward() {
        // Algorithm for the forward stays the same as its for the singly linkedlist
        if (head != null) {
            Node temp = head;   // Take a temporary node and go till the end printing nodes
            while (temp != null) {
                System.out.print(temp.data + "<-->");
                temp = temp.next;
            }
        }
    }

    public void traverseBackward() {
        // Algorithm for the backward
        if (head != null) {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }

            while (temp != null) {
                System.out.print(temp.data + " <-> ");
                temp = temp.prev;
            }
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.Insert(10);
        main.Insert(20);
        main.Insert(30);
        main.Insert(40);
        main.Insert(50);

        main.traverseForward();
        System.out.println();
        main.traverseBackward();

    }
}