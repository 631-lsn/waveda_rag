import * as React from "react";

import { cn } from "@/lib/utils";

export const Input = React.forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  ({ className, ...props }, ref) => (
    <input
      ref={ref}
      className={cn(
        "h-10 w-full rounded-xl border border-[var(--border)] bg-[var(--surface-2)] px-3 text-sm text-[var(--text)] outline-none placeholder:text-[var(--subtle)] focus:border-[var(--accent)] focus:ring-2 focus:ring-cyan-400/10",
        className,
      )}
      {...props}
    />
  ),
);
Input.displayName = "Input";
