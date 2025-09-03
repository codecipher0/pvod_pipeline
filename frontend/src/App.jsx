import React, { useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/run";

function App() {
  const [output, setOutput] = useState("");

  const runCommand = async (command) => {
    try {
      const res = await axios.post(API_URL, { command });
      setOutput(res.data.output);
    } catch (err) {
      setOutput("Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Linux Command Executor</h1>
      <div>
        <button onClick={() => runCommand("list_dir")}>List Directory</button>
        <button onClick={() => runCommand("show_date")}>Show Date</button>
        <button onClick={() => runCommand("disk_usage")}>Disk Usage</button>
        <button onClick={() => runCommand("uptime")}>System Uptime</button>
      </div>
      <h2>Output:</h2>
      <pre style={{ background: "#111", color: "#0f0", padding: "15px" }}>
        {output}
      </pre>
    </div>
  );
}

export default App;