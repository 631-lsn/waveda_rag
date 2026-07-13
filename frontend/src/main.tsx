import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { Button } from "@/components/ui/button";
import { Component as AiLoader } from "@/components/ui/ai-loader";
import { connectDesktopBridge, type DesktopBridgeClient } from "@/lib/bridge";
import "./index.css";
import "katex/dist/katex.min.css";

function DesktopRoot() {
  const [bridge, setBridge] = useState<DesktopBridgeClient | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    connectDesktopBridge().then(setBridge).catch((reason) => setError(reason instanceof Error ? reason.message : String(reason)));
  }, []);

  if (error) {
    return <div className="error-screen"><div className="error-card"><h1>无法连接桌面服务</h1><p>{error}</p><Button onClick={() => window.location.reload()}>重新连接</Button></div></div>;
  }
  if (!bridge) return <AiLoader text="正在载入" />;
  return <App bridge={bridge} />;
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <DesktopRoot />
  </React.StrictMode>,
);
