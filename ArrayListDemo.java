import java.util.*;;

public class ArrayListDemo {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<String>();

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Kiwi");
        fruits.add("Apple");
        fruits.add("Mango");
        fruits.add("Apple");
        fruits.add(1, "Watermelon");

        System.out.println("Fruits : " + fruits);
        System.out.println("Size : " + fruits.size());

        for (int i = 0; i < fruits.size(); i++) {
            System.out.println(fruits.get(i));
        }
        for (String s : fruits) {
            System.out.println(s);
        }

        fruits.set(3, "DragonFruit");
        System.out.println("Fruits : " + fruits);

        int i = fruits.indexOf("Kiwi");
        System.out.println("Index : " + i);

        int li = fruits.lastIndexOf("Apple");
        System.out.println("Last Index : "+li);

        fruits.remove("Apple");
        System.out.println("Fruits : " + fruits);

        fruits.remove(2);
        System.out.println("Fruits : " + fruits);

        System.out.println("Present : "+fruits.contains("Apple"));
        System.out.println("Present : "+fruits.contains("Kiwi"));

        System.out.println(fruits.isEmpty());

        ArrayList<String> copy =(ArrayList<String>)fruits.clone();
        System.out.println("Copy : "+copy);

        ArrayList<String> veg = new ArrayList<String>();
        veg.add("Tomato");
        veg.add("Patato");
        veg.add("Ladyfingers");

        // fruits.addAll(veg);
        // System.out.println("Fruits : "+fruits);
        // fruits.removeAll(veg);
        // System.out.println("Fruits : "+fruits);

        fruits.addAll(veg);
        fruits.retainAll(veg);
        System.out.println("Fruits : "+fruits);

        fruits.clear();
        System.out.println("Fruits : "+fruits);

        ArrayList<String> names = new ArrayList<>();
        names.add("Ansh");
        names.add("Rahul");
        names.add("Jay");

        Object[] arr = names.toArray();
        System.out.println("Array elements:");
        for (Object name : arr) {
            System.out.println(name);
        }

        System.out.println("Using forEach:");
        names.forEach(n -> System.out.println(n));
    }
}