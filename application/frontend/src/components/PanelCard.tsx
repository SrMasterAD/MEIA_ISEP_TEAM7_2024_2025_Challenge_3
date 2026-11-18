import { ReactNode } from "react";

type PanelCardProps = {
  title: string;
  children: ReactNode;
};

export default function PanelCard({ title, children }: PanelCardProps) {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-2xl">
      <h2 className="text-xl font-bold text-gray-800 mb-4">{title}</h2>
      <div>{children}</div>
    </div>
  );
}
