package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Main4 extends Application {
	
	TextField tf;  // void myClick()에 tf를 쓸려면 전역변수로 바꿔줘야함
	TextArea ta;
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main4.fxml"));
			
			Scene scene = new Scene(root,400,400);
			
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
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
		String a = tf.getText();  // 우선 String으로 받고
		int i = Integer.parseInt(a); // a를 int로 바꿔줌
		String result="";
		
			result = (i+"*"+1+"="+i*1+"\n");
			result += (i+"*"+2+"="+i*2+"\n");
			result += (i+"*"+3+"="+i*3+"\n");
			result += (i+"*"+4+"="+i*4+"\n");
			result += (i+"*"+5+"="+i*5+"\n");
			result += (i+"*"+6+"="+i*6+"\n");
			result += (i+"*"+7+"="+i*7+"\n");
			result += (i+"*"+8+"="+i*8+"\n");
			result += (i+"*"+9+"="+i*9);
			ta.setText(result); 
		
		
	
		
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
