import React from "react";
import ReactDOM from "react-dom/client";
import { Component } from "@/components/ui/ai-loader";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Component text="正在载入" />
  </React.StrictMode>,
);
