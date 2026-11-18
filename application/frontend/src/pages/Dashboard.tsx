import { useEffect, useRef, useState } from "react";
import ReportGenerator from "../components/ReportGenerator";
import ReportResultPanel from "../components/ReportResultPanel";
import api from "../lib/api";
import { ProgressSpinner } from "primereact/progressspinner";
import { Config } from "../models/user-configuration.model";

export default function Dashboard() {
  const [config, setConfig] = useState<Config | null>(null);
  const [loading, setLoading] = useState(true);
  const [reportResult, setReportResult] = useState<any>(null);

  const resultRef = useRef<HTMLDivElement | null>(null);

  const fetchConfig = async () => {
    try {
      const response = await api.get("/user/configurations");
      setConfig(response.data);
    } catch (error) {
      console.error("Failed to fetch configuration:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchConfig();
  }, []);

  // 👇 Scroll to Report Result when it appears
  useEffect(() => {
    if (reportResult && resultRef.current) {
      resultRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [reportResult]);

  return (
    <div className="min-h-screen bg-gray-50 p-6 flex justify-center items-start">
      {loading ? (
        <div className="flex justify-center items-center h-[300px]">
          <ProgressSpinner />
        </div>
      ) : (
        <div className="w-full max-w-2xl space-y-10">
          <ReportGenerator
            config={config}
            onUpdateConfig={fetchConfig}
            onReportGenerated={(result) => setReportResult(result)}
          />

          {reportResult && (
            <div ref={resultRef} className="w-full transition-all duration-500">
              <ReportResultPanel result={reportResult} />
            </div>
          )}
        </div>
      )}
    </div>
  );
}
