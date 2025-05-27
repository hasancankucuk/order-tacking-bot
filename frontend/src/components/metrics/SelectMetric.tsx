import { MetricsModel } from "../../models/MetricsModel";

type SelectMetricProps = {
    selectedMetric: MetricsModel;
    setSelectedMetric: (metric: MetricsModel) => void;
    loading: boolean;
}

const metricsOptions = [
    { label: "NLU Test", value: MetricsModel.NLU_TEST },
    { label: "Core Test", value: MetricsModel.CORE_TEST },
    { label: "Stories", value: MetricsModel.STORIES },
];

export const SelectMetric = ({ selectedMetric, setSelectedMetric, loading }: SelectMetricProps) => {
    return (
        <select
            className="uk-select uk-border-rounded"
            aria-label="Select metric"
            value={selectedMetric}
            onChange={(e) => setSelectedMetric(Number(e.target.value))}
            disabled={loading}
        >
            <option value={MetricsModel.NULL} disabled>
                Select a metric
            </option>
            {metricsOptions.map((opt) => (
                <option key={opt.value} value={opt.value}>
                    {opt.label}
                </option>
            ))}
        </select>
    )
}