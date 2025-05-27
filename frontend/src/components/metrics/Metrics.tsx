import React, { useState } from "react";
import { MetricsModel } from "../../models/MetricsModel";
import { fetchNluTest, fetchCoreTest } from "../../services/metrics";
import { SelectMetric } from "./SelectMetric";
import { NLUTestModel } from "../../models/NLUTestModel";
import { NLUMetrics } from "./NLUMetrics";
import { CoreTestModel } from "../../models/CoreTestModel";
import { CoreMetrics } from "./CoreMetrics";

export const Metrics = () => {
  const [selectedMetric, setSelectedMetric] = useState<MetricsModel>(MetricsModel.NULL);
  const [nluTest, setNluTest] = useState<NLUTestModel | null>(null);
  const [coreTest, setCoreTest] = useState<CoreTestModel | null>(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleTest = async (e: React.FormEvent) => {
    e.preventDefault();
    setNluTest(null);
    setError (null);
    setLoading(true);

    try {
      switch (selectedMetric) {
        case MetricsModel.NLU_TEST: {
          const data = await fetchNluTest();
          setNluTest(data);
          break;
        }
        case MetricsModel.CORE_TEST:
          const data = await fetchCoreTest();
          setCoreTest(data);
          break;
        case MetricsModel.STORIES:
          break;
        default:
          setError("Please select an option.");
          break;
      }
    } catch (err: any) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="uk-container uk-margin-top">
      <h1>Evaluation Metrics</h1>
      <div className="uk-card uk-card-default uk-card-body uk-box-shadow-large" style={{ borderRadius: 12 }}>
        <div className="uk-margin">
          <SelectMetric
            selectedMetric={selectedMetric}
            setSelectedMetric={setSelectedMetric}
            loading={loading}
          />

        </div>
        <button
          className="uk-button uk-button-primary uk-width-1-1 uk-form-medium"
          style={{ borderRadius: 8 }}
          type="button"
          onClick={handleTest}
          disabled={loading || selectedMetric === MetricsModel.NULL}
        >
          {loading ? "Running..." : `Run Test`}
        </button>

        {loading && (
          <span className="uk-margin-top" uk-spinner="ratio: 2"></span>
          
        )}

        {selectedMetric === MetricsModel.NLU_TEST && nluTest && (
          <pre
            className="uk-margin-top"
            style={{
              background: "#f4f4f4",
              padding: 16,
              borderRadius: 8,
              maxHeight: 400,
              overflow: "auto",
            }}
          >
            <NLUMetrics {...nluTest} />
          </pre>
        )}

        {selectedMetric === MetricsModel.CORE_TEST && coreTest && (
          <pre
            className="uk-margin-top"
            style={{
              background: "#f4f4f4",
              padding: 16,
              borderRadius: 8,
              maxHeight: 400,
              overflow: "auto",
            }}
          >
            <CoreMetrics {...coreTest} />
          </pre>
        )}

        {error && <div className="uk-alert-danger uk-text-center uk-margin-top" style={{ borderRadius: 8, marginBottom: 12 }}>{error}</div>}

      </div>
    </div>
  );
};