import { useState } from "react";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Example login payload
    const loginData = {
      email,
      password,
    };

    console.log("Login data:", loginData);

    // TODO: send loginData to your API
  };

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <h2>Login</h2>

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
        style={styles.input}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
        style={styles.input}
      />

      <button type="submit" style={styles.button}>
        Login
      </button>
    </form>
  );
}

const styles = {
  form: {
    maxWidth: "300px",
    margin: "50px auto",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "8px",
  },
  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "10px",
  },
  button: {
    width: "100%",
    padding: "10px",
    cursor: "pointer",
  },
};

export default Login;
