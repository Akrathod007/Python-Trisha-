import java.util.*;

public class SetExample {

    public static void main(String[] args) {

        Set<Integer> set = new HashSet<>();

        // 1. add()
        set.add(10);
        set.add(20);
        set.add(30);
        set.add(40);

        // Duplicate
        set.add(20);

        System.out.println("Set: " + set);


        // 2. size()
        System.out.println("Size: " + set.size());


        // 3. contains()
        System.out.println("Contains 30: " + set.contains(30));
        System.out.println("Contains 50: " + set.contains(50));


        // 4. isEmpty()
        System.out.println("Is Empty: " + set.isEmpty());


        // 5. remove()
        set.remove(20);

        System.out.println("After remove(20): " + set);


        // 6. addAll()
        Set<Integer> set2 = new HashSet<>();

        set2.add(30);
        set2.add(40);
        set2.add(50);
        set2.add(60);

        set.addAll(set2);

        System.out.println("After addAll(): " + set);


        // 7. containsAll()
        System.out.println(
            "Contains all set2 elements: "
            + set.containsAll(set2)
        );


        // 8. removeAll()
        Set<Integer> set3 = new HashSet<>();

        set3.add(30);
        set3.add(40);

        set.removeAll(set3);

        System.out.println("After removeAll(): " + set);


        // 9. retainAll()
        Set<Integer> set4 = new HashSet<>();

        set4.add(50);
        set4.add(60);

        set.retainAll(set4);

        System.out.println("After retainAll(): " + set);


        // 10. iterator()
        System.out.println("Using Iterator:");

        Iterator<Integer> itr = set.iterator();

        while (itr.hasNext()) {
            System.out.println(itr.next());
        }


        // 11. toArray()
        Object[] arr = set.toArray();

        System.out.println("Array elements:");

        for (Object value : arr) {
            System.out.println(value);
        }


        // 12. clear()
        set.clear();

        System.out.println("After clear(): " + set);


        // 13. isEmpty() after clear
        System.out.println("Is Empty: " + set.isEmpty());
    }
}
