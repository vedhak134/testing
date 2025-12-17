import React, { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>React Counter App</h1>
      <p>Current count: {count}</p>

      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>

      <button
        onClick={() => setCount(count - 1)}
        style={{ marginLeft: "10px" }}
      >
        Decrement
      </button>
    </div>
  );
}

export default App;
