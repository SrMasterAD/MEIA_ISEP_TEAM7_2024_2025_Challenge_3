import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import { ReportResult } from "../models/report-result.model";


type Props = {
  result: ReportResult;
};

export default function ReportResultPanel({ result }: Props) {
  const isHealthy = result.wheat_disease === "Healthy";

  const handleDownloadPDF = () => {
    const doc = new jsPDF();

    doc.setFontSize(16);
    doc.text("DeepWheat - Wheat Health Report", 14, 20);
    doc.setFontSize(12);
    doc.text(`Detected Disease: ${result.wheat_disease}`, 14, 30);

    if (!isHealthy) {
      autoTable(doc, {
        startY: 40,
        head: [["Day", "Infected Area", "Yield Loss", "Profit Loss", "Plantation Loss"]],
        body: result.infection_by_day.map((entry) => [
          entry.day,
          entry.infected_area,
          entry.yield_loss,
          entry.economic_impact.profit_loss,
          entry.economic_impact.plantation_loss,
        ]),
      });

      doc.text("Treatment:", 14, doc.lastAutoTable.finalY + 10);
      doc.setFontSize(11);
      doc.text(result.disease_treatment, 14, doc.lastAutoTable.finalY + 18);
      doc.setFontSize(12);
      doc.text("Cause:", 14, doc.lastAutoTable.finalY + 26);
      doc.setFontSize(11);
      doc.text(result.disease_cause, 14, doc.lastAutoTable.finalY + 34);
      doc.setFontSize(12);
      doc.text("Management:", 14, doc.lastAutoTable.finalY + 42);
      doc.setFontSize(11);
      doc.text(result.disease_management, 14, doc.lastAutoTable.finalY + 50);
    } else {
      doc.setFontSize(12);
      doc.text("No disease was detected. The wheat is healthy.", 14, 40);
    }

    doc.save("wheat_report.pdf");
  };

  return (
    <div className="bg-white border border-gray-200 shadow-md rounded-xl p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-blue-700">🧬 Wheat Health Report</h2>
        <button
          onClick={handleDownloadPDF}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-xl text-sm"
        >
          📄 Download PDF
        </button>
      </div>

      {isHealthy ? (
        <div className="bg-green-50 border-l-4 border-green-500 text-green-800 p-4 rounded-lg">
          <h3 className="text-xl font-semibold mb-1">✅ No Disease Detected</h3>
          <p className="text-sm">Your wheat crop appears to be healthy and free from disease. Keep monitoring regularly for early detection!</p>
        </div>
      ) : (
        <>
          <h3 className="text-lg font-semibold text-gray-700">
            🦠 Detected Disease: {result.wheat_disease}
          </h3>

          <div>
            <h4 className="text-md font-medium text-gray-700 mb-2">📊 Infection Timeline</h4>
            <div className="overflow-x-auto">
              <table className="min-w-full text-sm text-left border">
                <thead className="bg-blue-50 text-blue-700">
                  <tr>
                    <th className="px-4 py-2 border">Day</th>
                    <th className="px-4 py-2 border">Infected Area</th>
                    <th className="px-4 py-2 border">Yield Loss</th>
                    <th className="px-4 py-2 border">Profit Loss</th>
                    <th className="px-4 py-2 border">Plantation Loss</th>
                  </tr>
                </thead>
                <tbody>
                  {result.infection_by_day.map((entry, index) => (
                    <tr key={index} className="even:bg-gray-50">
                      <td className="px-4 py-2 border">{entry.day}</td>
                      <td className="px-4 py-2 border">{entry.infected_area}</td>
                      <td className="px-4 py-2 border">{entry.yield_loss}</td>
                      <td className="px-4 py-2 border">{entry.economic_impact.profit_loss}</td>
                      <td className="px-4 py-2 border">{entry.economic_impact.plantation_loss}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="mt-6">
            <h4 className="text-md font-medium text-gray-700 mb-2">💊 Treatment</h4>
            <p className="text-sm">{result.disease_treatment}</p>
          </div>
          <div className="mt-6">
            <h4 className="text-md font-medium text-gray-700 mb-2">🧪 Cause of Disease</h4>
            <p className="text-sm">{result.disease_cause}</p>
          </div>
          <div className="mt-6">
            <h4 className="text-md font-medium text-gray-700 mb-2">💼 Disease Management</h4>
            <p className="text-sm">{result.disease_management}</p>
          </div>

        </>
      )}
    </div>
  );
}
