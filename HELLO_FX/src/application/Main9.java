package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Main9 extends Application {
	
	TextField tf;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main9.fxml"));

			Scene scene = new Scene(root,400,400);
			
			tf = (TextField) scene.lookup("#tf");
			Button btn1 = (Button) scene.lookup("#btn1");
			Button btn2 = (Button) scene.lookup("#btn2");
			Button btn3 = (Button) scene.lookup("#btn3");
			Button btn4 = (Button) scene.lookup("#btn4");
			Button btn5 = (Button) scene.lookup("#btn5");
			
			Button btn6 = (Button) scene.lookup("#btn6");
			Button btn7 = (Button) scene.lookup("#btn7");
			Button btn8 = (Button) scene.lookup("#btn8");
			Button btn9 = (Button) scene.lookup("#btn9");
			Button btn0 = (Button) scene.lookup("#btn0");
			
			Button btn_call = (Button) scene.lookup("#btn_call");
			
			btn1.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn2.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn3.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn4.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn5.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			
			btn6.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn7.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn8.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn9.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			btn0.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { myclick(event); }	 });
			
			btn_call.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { mycall(); }	 });

			
			

			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void mycall() {
		Alert alert = new Alert(AlertType.NONE);

		alert.setTitle("Warning Dialog");
		alert.setHeaderText("Look, a Warning Dialog");
		alert.setContentText("Careful with the next step!");
		alert.showAndWait();

	}
	
	public void myclick(Event event) {
		String str_old = tf.getText();
		Button imsi = (Button) event.getSource();
		String str_new = imsi.getText();
		
		
		tf.setText(str_old+str_new);


	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
