"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";

export default function Home() {
  const [input, setInput] = useState("");
  const [returnedData, setReturnedData] = useState("");

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const response = await fetch(
      `http://127.0.0.1:5328/modules/google?form-input=${input}`
    );
    const data = await response.json();
    console.log(data);
    setReturnedData(data);
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div
        style={{
          height: "70vh",
          overflow: "auto",
          padding: "50px",
          backgroundColor: "black",
          color: "white",
          border: "1px solid white",
        }}
      >
        <pre style={{ whiteSpace: "pre-wrap" }}>
          {JSON.stringify(returnedData, null, 2)}
        </pre>
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={{
            backgroundColor: "black",
            color: "white",
            border: "1px solid white",
            marginRight: "10px",
          }}
        />
        <button type="submit">Submit</button>
      </form>
    </main>
  );
}
