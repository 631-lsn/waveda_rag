import * as React from "react";

interface LoaderProps {
  size?: number;
  text?: string;
}

export const Component: React.FC<LoaderProps> = ({ size = 180, text = "Generating" }) => {
  const letters = text.split("");

  return (
    <div
      data-testid="ai-loader-overlay"
      className="fixed inset-0 z-50 flex items-center justify-center overflow-hidden bg-[var(--bg)] text-[var(--text)] transition-colors duration-300"
    >
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 42%, rgba(34, 211, 238, 0.08), transparent 31%), radial-gradient(circle at 50% 100%, rgba(14, 165, 233, 0.05), transparent 43%)",
        }}
      />
      <div
        data-testid="ai-loader-orbit"
        className="relative z-10 flex items-center justify-center font-inter select-none"
        style={{ width: size, height: size }}
      >
        {letters.map((letter, index) => (
          <span
            key={index}
            className="inline-block text-[var(--muted)] opacity-55 animate-loaderLetter"
            style={{ animationDelay: `${index * 0.1}s` }}
          >
            {letter}
          </span>
        ))}

        <div className="absolute inset-0 rounded-full animate-loaderCircle"></div>
      </div>

      <style jsx>{`
        @keyframes loaderCircle {
          0% {
            transform: rotate(90deg);
            box-shadow:
              0 6px 12px 0 #67e8f9 inset,
              0 12px 18px 0 #38bdf8 inset,
              0 34px 38px 0 #155e75 inset,
              0 0 6px 1px rgba(34, 211, 238, 0.18),
              0 0 18px 2px rgba(14, 165, 233, 0.1);
          }
          50% {
            transform: rotate(270deg);
            box-shadow:
              0 6px 12px 0 #a5f3fc inset,
              0 12px 8px 0 #22d3ee inset,
              0 28px 38px 0 #0e7490 inset,
              0 0 6px 1px rgba(34, 211, 238, 0.2),
              0 0 18px 2px rgba(14, 165, 233, 0.11);
          }
          100% {
            transform: rotate(450deg);
            box-shadow:
              0 6px 12px 0 #67e8f9 inset,
              0 12px 18px 0 #38bdf8 inset,
              0 34px 38px 0 #155e75 inset,
              0 0 6px 1px rgba(34, 211, 238, 0.18),
              0 0 18px 2px rgba(14, 165, 233, 0.1);
          }
        }

        @keyframes loaderLetter {
          0%,
          100% {
            opacity: 0.4;
            transform: translateY(0);
          }
          20% {
            opacity: 1;
            transform: scale(1.15);
          }
          40% {
            opacity: 0.7;
            transform: translateY(0);
          }
        }

        .animate-loaderCircle {
          animation: loaderCircle 5s linear infinite;
        }

        .animate-loaderLetter {
          animation: loaderLetter 3s infinite;
        }
      `}</style>
    </div>
  );
};
