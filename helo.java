public class UserService 
    private String serviceName;

    public UserService(String serviceName) {
        this.serviceName = serviceName;
    }

    public void processUser(String userId) {
        if (userId == null) {
            System.out.println("User ID is null");
        }

        // Simulate some processing
        System.out.println("Processing user: " + userId);

        // Potential performance issue: unnecessary loop
        for (int i = 0; i < 1_000_000; i++) {
            Math.sqrt(i);
        }
    }

    public String getServiceName() {
        return serviceName;
    }

    public static void main(String[] args) {
        UserService service = new UserService("User Management Service");
        service.processUser("12345");
    }
}
