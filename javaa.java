import java.util.ArrayList;
import java.util.Scanner;

class Student {
    int id;
    String name;
    int age;

    Student(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
}

public class StudentManager {

    static ArrayList<Student> students = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    static void addStudent() {
        System.out.print("Enter ID: ");
        int id = Integer.parseInt(scanner.nextLine());

        System.out.print("Enter Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter Age: ");
        int age = Integer.parseInt(scanner.nextLine());

        students.add(new Student(id, name, age));
        System.out.println("Student added successfully.");
    }

    static void listStudents() {
        if (students.isEmpty()) {
            System.out.println("No students available.");
            return;
        }

        System.out.println("\nStudent List:");
        for (Student s : students) {
            System.out.println(
                "ID: " + s.id +
                ", Name: " + s.name +
                ", Age: " + s.age
            );
        }
    }

    static void deleteStudent() {
        System.out.print("Enter Student ID to delete: ");
        int id = Integer.parseInt(scanner.nextLine());

        boolean removed = students.removeIf(s -> s.id == id);
        if (removed) {
            System.out.println("Student removed.");
        } else {
            System.out.println("Student not found.");
        }
    }

    static void showMenu() {
        System.out.println("\n--- Student Manager ---");
        System.out.println("1. Add Student");
        System.out.println("2. List Students");
        System.out.println("3. Delete Student");
        System.out.println("4. Exit");
        System.out.print("Choose an option: ");
    }

    public static void main(String[] args) {
        while (true) {
            showMenu();
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    addStudent();
                    break;
                case "2":
                    listStudents();
                    break;
                case "3":
                    deleteStudent();
                    break;
                case "4":
                    System.out.println("Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }
}
