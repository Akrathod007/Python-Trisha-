import java.util.*;

public class QueueDemo {

    public static void main(String[] args) {

        Queue<Integer> q = new LinkedList<>();

        // Add elements
        q.add(10);
        q.add(20);
        q.add(30);

        System.out.println("Queue: " + q);

        // Offer
        q.offer(40);

        System.out.println("After offer: " + q);

        // Peek
        System.out.println("Front element: " + q.peek());

        // Element
        System.out.println("Element: " + q.element());

        // Poll
        System.out.println("Removed: " + q.poll());

        System.out.println("After poll: " + q);

        // Remove
        System.out.println("Removed: " + q.remove());

        System.out.println("After remove: " + q);

        // Size
        System.out.println("Size: " + q.size());

        // Contains
        System.out.println("Contains 30? " + q.contains(30));

        // Empty
        System.out.println("Is empty? " + q.isEmpty());

        while (!q.isEmpty()) {

            System.out.println(
                    "Printing for " + q.poll());
        }

        System.out.println("Is empty? " + q.isEmpty());

        PriorityQueue<String> pq = new PriorityQueue<>();

        pq.add("Mango");
        pq.add("Apple");
        pq.add("Banana");
        pq.add("Orange");

        while (!pq.isEmpty()) {
            System.out.println(pq.poll());
        }

        PriorityQueue<Integer> pq2 = new PriorityQueue<>();
        pq2.add(20);
        pq2.add(10);
        pq2.add(5);
        pq2.add(2);
        pq2.add(13);

        System.out.println("PQ2 : " + pq2);
        while (!pq2.isEmpty()) {
            System.out.println(pq2.poll());
        }

        PriorityQueue<Integer> pq3 = new PriorityQueue<>(Collections.reverseOrder());

        pq3.add(10);
        pq3.add(50);
        pq3.add(20);
        pq3.add(40);
        pq3.add(30);

        while (!pq3.isEmpty()) {

            System.out.println(pq3.poll());
        }
    }
}
