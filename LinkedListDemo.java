import java.util.*;

public class LinkedListDemo {
    public static void main(String[] args) {

        LinkedList<Integer> list = new LinkedList<>();

        // add()
        list.add(10);
        list.add(20);
        list.add(30);
        System.out.println("add(): " + list);

        // addFirst()
        list.addFirst(5);

        // // addLast()
        list.addLast(40);
        System.out.println("addFirst & addLast: " + list);

        // // get()
        System.out.println("get(2): " + list.get(2));

        // // getFirst()
        System.out.println("First: " + list.getFirst());

        // // getLast()
        System.out.println("Last: " + list.getLast());

        // // set()
        list.set(2, 25);
        System.out.println("set(): " + list);

        // // remove()
        list.remove(2);
        System.out.println("remove(index): " + list);

        // // removeFirst()
        list.removeFirst();

        // // removeLast()
        list.removeLast();
        System.out.println("removeFirst & removeLast: " + list);

        // // size()
        System.out.println("Size: " + list.size());

        // // contains()
        System.out.println("Contains 20? " + list.contains(20));

        // // indexOf()
        System.out.println("Index of 20: " + list.indexOf(20));

        // // addAll()
        LinkedList<Integer> list2 = new LinkedList<>();
        list2.add(100);
        list2.add(200);
        list.addAll(list2);
        System.out.println("addAll(): " + list);

        // // clear()
        list.clear();
        System.out.println("clear(): " + list);

        // // Queue methods
        list.add(10);
        list.add(20);
        list.add(30);

        System.out.println("peek(): " + list.peek()); // first element
        System.out.println("poll(): " + list.poll()); // remove first
        System.out.println("After poll: " + list);

        // // Stack methods
        list.push(5);
        System.out.println("push(): " + list);

        list.pop();
        System.out.println("pop(): " + list);
    }
}