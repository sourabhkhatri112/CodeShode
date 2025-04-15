import java.util.function.Consumer;

class TestMain{
    public static void main(String[] args){
		Consumer<String> consume = str -> System.out.println(str);
		consume.accept("Ramesh");
		
		Consumer<String> consumeLength = str -> System.out.println("text is: " + str + " and length is: " + str.length());
		consumeLength.accept("This is a java example");
	}
}