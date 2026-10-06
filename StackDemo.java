import java.util.*;

public class StackDemo {
    public static void main(String[] args) {

        Stack<Integer> s = new Stack<>();

        // push() → Add elements
        s.push(10);
        s.push(20);
        s.push(30);
        s.push(40);

        System.out.println("Stack: " + s);

        // peek() → View top element
        System.out.println("Top element: " + s.peek());

        // pop() → Remove top element
        System.out.println("Removed: " + s.pop());
        System.out.println("After pop: " + s);

        // empty() → Check stack empty or not
        System.out.println("Is empty? " + s.empty());

        // search() → Position from top
        System.out.println("Position of 20: " + s.search(20));

        // size()
        System.out.println("Size: " + s.size());

        // contains()
        System.out.println("Contains 10? " + s.contains(10));

        // Iterate stack
        System.out.println("Elements:");
        for (int x : s) {
            System.out.println(x);
        }

        // Clear stack
        s.clear();
        System.out.println("After clear: " + s);
    }
}