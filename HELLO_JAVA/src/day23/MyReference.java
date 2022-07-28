package day23;

public class MyReference {
	public static void changeInt(String a) {
		a = "3";
	}
	public static void changeArr(String[] a) {
		a[0]="3";
	}
	public static void main(String[] args) {
		String b ="1";
		String [] bb = {"1"};
		System.out.println(b);
		System.out.println(bb[0]);
		
		changeInt(b);
		changeArr(bb);
		
		System.out.println(b); // 출력시 3이 아니라 1이 뜸
		System.out.println(bb[0]);
	}
}
// reference
// value : int float string