public class test1{
	public static void main(String[] args){
		byte a = 25;
		byte b = 0;
		while(b < 10){
			a +=(b + 10) * 25;
			b++;
		}
		System.out.println(a);
	}
}