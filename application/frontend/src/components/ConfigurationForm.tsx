import { useEffect, useRef, useState } from "react";
import api from "../lib/api";
import { Toast } from "primereact/toast";
import { Config } from "../models/user-configuration.model";


type Props = {
  initialConfig?: Config;
  onClose: () => void;
  onSuccess?: () => void;
};

export default function ConfigurationForm({ initialConfig, onClose, onSuccess }: Props) {
  const toast = useRef<Toast>(null);

  const [config, setConfig] = useState<Config>({
    area: NaN,
    plantation_cost: NaN,
    expected_yield: NaN,
    expected_profit: NaN,
  });

  const [submitted, setSubmitted] = useState(false);

  const isFormValid =
    config.area > 0 &&
    config.plantation_cost > 0 &&
    config.expected_yield > 0 &&
    config.expected_profit > 0;

  useEffect(() => {
    if (initialConfig) {
      setConfig(initialConfig);
    }
  }, [initialConfig]);

  const handleChange = (field: keyof Config, value: number) => {
    setConfig((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    if (!isFormValid) return;

    try {
      if (config.id) {
        await api.put(`/user/configurations/${config.id}`, config);
      } else {
        await api.post("/user/configurations", config);
      }
      onSuccess?.();
      onClose();
    } catch (error: any) {
      console.error("Error submitting configuration:", error);
      toast.current?.show({
        severity: "error",
        summary: "Error",
        detail: error.response?.data?.message || "Failed to save configuration",
        life: 4000,
      });
    }
  };

  return (
    <>
      <Toast ref={toast} />
      <form onSubmit={handleSubmit} className="space-y-4">
        {["area", "plantation_cost", "expected_yield", "expected_profit"].map((field) => (
          <div key={field}>
            <label className="block mb-1 text-sm font-medium text-gray-600 capitalize">
              {field.replace(/_/g, " ")}
            </label>
            <input
              type="number"
              min="0"
              value={config[field as keyof Config] || ""}
              onChange={(e) => {
                const value = Number(e.target.value);
                handleChange(field as keyof Config, value < 0 ? 0 : value);
              }}
              className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 appearance-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"
            />
            {submitted && (config[field as keyof Config] ?? 0) <= 0 && (
              <small className="text-red-500">This field is required</small>
            )}
          </div>
        ))}

        <div className="mt-6 flex justify-end">
          <button
            type="submit"
            disabled={!isFormValid}
            className={`inline-flex items-center px-4 py-2 text-white rounded-xl transition ${isFormValid
              ? "bg-blue-600 hover:bg-blue-700"
              : "bg-gray-400 cursor-not-allowed"
              }`}
          >
            <svg
              className="w-4 h-4 mr-2"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
            </svg>
            {config.id ? "Update" : "Save"}
          </button>
        </div>
      </form>
    </>
  );
}
