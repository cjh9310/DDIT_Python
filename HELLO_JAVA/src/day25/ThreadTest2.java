package day25;

public class ThreadTest2 {
	public static void showNumber() {
		new Thread(new Runnable() {
			public void run() {
				for(int i=1; i<=100000; i++) {
					System.out.println((char)i);
					if(i%100==0) {
						System.out.println();
					}
				}
			}
		}).start();
	}
	public static void showAscii() {
		new Thread(new Runnable() {
			public void run() {
				for(int i=1; i<=100000; i++) {
					System.out.println((char)i);
					if(i%100==0) {
						System.out.println();
					}
				}
	
			}
		});
	}
	
	
	public static void main(String[] args) {
		showNumber();
		showAscii();
	}                                                               
}
