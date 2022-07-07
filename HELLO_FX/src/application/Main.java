package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;


public class Main extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			// VBox가 fxml내부에 있음.
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("hello.fxml"));
			Scene scene = new Scene(root,400,400);
			
			Label lbl = (Label) scene.lookup("#lbl");
			Button btn = (Button) scene.lookup("#btn");
			// javafx button mouse click event으로 검색
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				// setOnMouseClicked 마우스로 클릭시 실행되는 메서드
				// Handler = 이벤트 처리하는 역할?
				@Override
				public void handle(Event event) {
					lbl.setText("Good Evening");
				}
			});
			
			
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
