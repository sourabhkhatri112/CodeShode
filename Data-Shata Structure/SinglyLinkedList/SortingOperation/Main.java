package LinkedListNodeCreation.SortingOperation;


class Node{
    int data;   // A node contains data
    Node next;  // A node contains address to the next node

    // Next in order to create any node we are supposed to create a constructor
    // Hence our node is finally created.
    public Node(int data){
        this.data = data;
        this.next = null;
    }
}
public class Main {
    private Node head;

    public void insert(int data){
        // Create a TRAIN Coach first of all before INSERTING anything.
        Node new_node = new Node(data);

        if(head == null) {  // It means NO COACH present in TRAIN
            head = new_node;
            return;
        }
        else if(head.next == null) {
            // It means there is only 1 coach present. Under such condition,
            // attach the HOOK of new COACH to that already present COACH.
            // HEAD will not change it will stay over that 1st coach itself.
            head.next = new_node;
        } else{
            // This condition will only be triggered if there are more than
            // 2 coaches present. Now, in such condition we cannot move the HEAD POINTER itself.
            Node temp_node = head;      // HEAD always STAYS at 1st COACH. So we take a TEMPORARY POINTER which we start at HEAD.
            while(temp_node.next != null){  // We keep HOPPING that TEMP POINTER until it reaches to the LAST COACH.
                temp_node = temp_node.next; // When the TEMP POINTER reaches to the LAST COACH, WHILE loop finally exits
            }
            temp_node.next = new_node;       // We finally HOOK the new coach behind the LAST CODE.
        }
    }

    public void display(){
        Node temp = head;
        while(temp.next != null){
            System.out.print(temp.data + "-->");
            temp = temp.next;
        }
    }
}
