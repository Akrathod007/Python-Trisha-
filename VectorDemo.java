import java.util.*;

public class VectorDemo {
    public static void main(String[] args) {

        Vector<Integer> v = new Vector<>();

        // add()
        v.add(10);
        v.add(20);
        v.add(30);
        System.out.println("add(): " + v);

        // addElement() (old method)
        v.addElement(40);
        System.out.println("addElement(): " + v);

        // get()
        System.out.println("get(2): " + v.get(2));

        // set()
        v.set(1, 25);
        System.out.println("set(): " + v);

        // remove()
        v.remove(2);
        System.out.println("remove(index): " + v);

        // removeElement()
        v.removeElement(25);
        System.out.println("removeElement(): " + v);

        // size()
        System.out.println("Size: " + v.size());
        v.add(30);
        v.add(30);
        v.add(30);
        v.add(30);
        v.add(30);
        v.add(30);
        v.add(30);
        v.add(30);
        System.out.println("Size: " + v.size());

        // capacity()
        System.out.println("Capacity: " + v.capacity());

        // contains()
        System.out.println("Contains 10? " + v.contains(10));

        // indexOf()
        System.out.println("Index of 10: " + v.indexOf(10));

        // firstElement()
        System.out.println("First: " + v.firstElement());

        // lastElement()
        System.out.println("Last: " + v.lastElement());

        // addAll()
        Vector<Integer> v2 = new Vector<>();
        v2.add(100);
        v2.add(200);

        v.addAll(v2);
        System.out.println("addAll(): " + v);

        // clear()
        v.clear();
        System.out.println("clear(): " + v);
    }
}

