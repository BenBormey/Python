
import java.util.ArrayList;
import java.util.Arrays;



public class HelloWorld {
    public static void main(String[] args) {
        // ArrayList<String> list  = new ArrayList<>();
        // list.add("Bormey");
        // list.add("Sok");
        // list.add("Rith");
        // list.add("Dara");
        // list.add("Vanna");
        // for (String name  : list){
        //     System.out.println("Hello " + name + "!");
        // }
        // HashSet<Integer> set = new HashSet<>();
        // set.add(10);
        // set.add(20);
        // set.add(30);
        // set.add(40);
        // set.add(10);
        
        // for (Integer number : set){
        //     System.out.println(number);
        // }


    // HashMap<Integer, String> map = new HashMap<>();
    // map.put(1, "Bormey");
    // map.put(2, "Sok");
    // map.put(3, "Rith");
    // for (Integer key : map.keySet()){
    //     System.out.println("Key: " + key + ", Value: " + map.get(key));
        
    // }

    ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(5, 1, 9, 2, 7));

    // numbers.sort((a, b) -> a - b);
    numbers.sort(Integer::compareTo);

    for (Integer number : numbers){
        System.out.println(number);
    }
}
}
