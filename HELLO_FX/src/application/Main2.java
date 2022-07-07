package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;

import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Main2 extends Application {
	
	TextField tf;  // void myClick()에 tf를 쓸려면 전역변수로 바꿔줘야함
	String a;
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main2.fxml"));
			
			Scene scene = new Scene(root,400,400);
			
			tf = (TextField) scene.lookup("#tf");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
//					System.out.println(event);   여러 출력기(sout)를 사용할 수 있으니 void로 만들어둠.
					myclick();
				}
			});
			
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myclick() {
//		System.out.println("myclick()");   실행되나 연습
		// 방법1
//		a = tf.getText();  // 우선 String으로 받고
//		int aa = Integer.parseInt(a); // a를 int로 바꿔줌
		// 방법2
		int aa = Integer.parseInt(tf.getText());
		aa++;
		tf.setText(aa+"");   // setText로 실행하려면 String문자열이 기본 aa가 기존에 숫자라 String으로 바꿔줘야함.
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
