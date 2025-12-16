import java.util.ArrayList;
import java.util.Scanner;

class Task {
    String title;
    boolean done;

    Task(String title) {
        this.title = title;
        this.done = false;
    }
}

public class TaskManager {
    static ArrayList<Task> tasks = new ArrayList<>();

    static void addTask(String title) {
        tasks.add(new Task(title));
    }

    static void listTasks() {
        for (int i = 0; i < tasks.size(); i++) {
            Task t = tasks.get(i);
            String status = t.done ? "✓" : " ";
            System.out.println((i + 1) + ". [" + status + "] " + t.title);
        }
    }

    static void markDone(int index) {
        if (index >= 0 && index < tasks.size()) {
            tasks.get(index).done = true;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("(a)dd (l)ist (d)one (q)uit: ");
            String cmd = sc.nextLine();
            if (cmd.equals("a")) {
                System.out.print("Task title: ");
                addTask(sc.nextLine());
            } else if (cmd.equals("l")) {
                listTasks();
            } else if (cmd.equals("d")) {
                System.out.print("Task number: ");
                markDone(Integer.parseInt(sc.nextLine()) - 1);
            } else if (cmd.equals("q")) {
                break;
            } else {
                System.out.println("Unknown command");
            }
        }
        sc.close();
        System.out.println("Goodbye!");
    }
}
