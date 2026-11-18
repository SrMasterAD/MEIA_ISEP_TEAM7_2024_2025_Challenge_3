import { useEffect, useState } from "react";
import api from "../lib/api";
import { ProgressSpinner } from "primereact/progressspinner";
import { Button } from "primereact/button";
import { Dialog } from "primereact/dialog";
import { ConfirmDialog, confirmDialog } from "primereact/confirmdialog";
import ConfigurationForm from "../components/ConfigurationForm";

type UserConfiguration = {
  id: number;
  area: number;
  plantation_cost: number;
  expected_yield: number;
  expected_profit: number;
};

export default function Configurations() {
  const [configs, setConfigs] = useState<UserConfiguration[]>([]);
  const [loading, setLoading] = useState(true);
  const [deletingId, setDeletingId] = useState<number | null>(null);
  const [editingConfig, setEditingConfig] = useState<UserConfiguration | null>(null);

  const fetchConfigs = async () => {
    try {
      const response = await api.get("/user/configurations");
      const data = Array.isArray(response.data) ? response.data : [response.data];
      setConfigs(data);
    } catch (error) {
      console.error("Failed to fetch configurations:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    setDeletingId(id);
    try {
      await api.delete(`/user/configurations/${id}`);
      setConfigs((prev) => prev.filter((c) => c.id !== id));
    } catch (error) {
      console.error("Failed to delete configuration:", error);
    } finally {
      setDeletingId(null);
    }
  };

  const confirmDelete = (config: UserConfiguration) => {
    confirmDialog({
      message: `Are you sure you want to delete this configuration?`,
      header: "Delete Confirmation",
      icon: "pi pi-exclamation-triangle",
      acceptLabel: "Yes, delete it",
      rejectLabel: "Cancel",
      acceptClassName: "p-button-danger",
      accept: () => handleDelete(config.id),
    });
  };

  useEffect(() => {
    fetchConfigs();
  }, []);

  return (
    <div className="min-h-screen px-6 py-10 bg-gray-50 flex justify-center">
      <div className="w-full max-w-4xl space-y-8">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          ⚙️ Configurations
        </h2>

        {loading ? (
          <div className="flex justify-center py-20">
            <ProgressSpinner />
          </div>
        ) : configs.length === 0 ? (
          <p className="text-gray-500 text-center">No configurations found.</p>
        ) : (
          <div className="space-y-4">
            {configs.map((config) => (
              <div
                key={config.id}
                className="bg-white rounded-xl shadow px-6 py-4 border border-gray-200 relative"
              >
                <div className="absolute top-4 right-4 flex gap-2">
                  <Button
                    icon="pi pi-pencil"
                    className="p-button-warning p-button-sm"
                    onClick={() => setEditingConfig(config)}
                  />
                  <Button
                    icon="pi pi-trash"
                    className="p-button-danger p-button-sm"
                    onClick={() => confirmDelete(config)}
                    loading={deletingId === config.id}
                  />
                </div>
                <p><strong>Area:</strong> {config.area} m²</p>
                <p><strong>Cost:</strong> ${config.plantation_cost}</p>
                <p><strong>Expected Yield:</strong> {config.expected_yield}</p>
                <p><strong>Expected Profit:</strong> ${config.expected_profit}</p>
              </div>
            ))}
          </div>
        )}

        {/* Edit Modal */}
        <Dialog
          header="Edit Configuration"
          visible={!!editingConfig}
          style={{ width: "500px" }}
          modal
          onHide={() => setEditingConfig(null)}
        >
          {editingConfig && (
            <ConfigurationForm
              initialConfig={editingConfig}
              onClose={() => setEditingConfig(null)}
              onSuccess={fetchConfigs}
            />
          )}
        </Dialog>

        {/* Delete Confirmation Dialog */}
        <ConfirmDialog />
      </div>
    </div>
  );
}
