import java.util.*;

public class DequeDemo {

    public static void main(String[] args) {

        Deque<Integer> dq = new ArrayDeque<>();

        // Add at first
        dq.addFirst(20);
        dq.addFirst(10);
        dq.addFirst(10);


        // Add at last
        dq.addLast(30);
        dq.addLast(40);

        System.out.println("Deque: " + dq);

        // First and last
        System.out.println("First: " + dq.peekFirst());
        System.out.println("Last: " + dq.peekLast());

        // Remove first
        System.out.println(
            "Removed first: " + dq.removeFirst()
        );

        // Remove last
        System.out.println(
            "Removed last: " + dq.removeLast()
        );

        System.out.println("Final Deque: " + dq);

    }
}
