import { useState } from "react";
import { fetchResults } from "../../services/metrics";
import { CoreTestModel } from "../../models/CoreTestModel";

export const CoreMetrics = (data: CoreTestModel) => {
    const [showModal, setShowModal] = useState(false);
    const [zoomedImage, setZoomedImage] = useState<string>("");

    const report = Object.keys(data.report || {}).length > 0 ? data.report : data.story_report;

    if (!report || Object.keys(report).length === 0) {
        return (
            <div className="uk-card uk-card-default uk-card-body uk-margin-top">
                <h3 className="uk-card-title">Core Model Metrics</h3>
                <p>No report data available.</p>
            </div>
        );
    }

    return (
        <div className="uk-card uk-card-default uk-card-body uk-margin-top">
            <h3 className="uk-card-title">Core Model Metrics</h3>
            <table className="uk-table uk-table-small uk-table-divider">
                <tbody>
                    <tr>
                        <td><strong>Accuracy</strong></td>
                        <td>{report.accuracy?.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Macro Avg F1-Score</strong></td>
                        <td>{report["macro avg"]?.["f1-score"]?.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Weighted Avg Precision</strong></td>
                        <td>{report["weighted avg"]?.precision?.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Micro Avg Recall</strong></td>
                        <td>{report["micro avg"]?.recall?.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Conversation Accuracy</strong></td>
                        <td>
                            {report.conversation_accuracy
                                ? `${report.conversation_accuracy.accuracy.toFixed(2)} (${report.conversation_accuracy.correct}/${report.conversation_accuracy.total})`
                                : "N/A"}
                        </td>
                    </tr>
                    <tr>
                        <td><strong>Confusion Matrix</strong></td>
                        <td>
                            <img
                                onClick={() => {
                                    setZoomedImage(fetchResults(data.results?.story_confusion_matrix));
                                    setShowModal(true);
                                }}
                                src={fetchResults(data.results?.story_confusion_matrix)}
                                alt="Confusion Matrix"
                            />
                        </td>
                    </tr>
                    <tr>
                        <td><strong>DIET Classifier Histogram</strong></td>
                        <td>
                            <img
                                onClick={() => {
                                    setZoomedImage(fetchResults(data.results?.TEDPolicy_confusion_matrix));
                                    setShowModal(true);
                                }}
                                src={fetchResults(data.results?.TEDPolicy_confusion_matrix)}
                                alt="Histogram"
                            />
                        </td>
                    </tr>
                </tbody>
            </table>

            {showModal && zoomedImage && (
                <div
                    className="uk-modal uk-open"
                    style={{
                        display: "block",
                        background: "rgba(0,0,0,0.6)",
                        position: "fixed",
                        top: 0, left: 0, right: 0, bottom: 0,
                        zIndex: 1000
                    }}
                    onClick={() => setShowModal(false)}
                >
                    <div
                        className="uk-modal-dialog uk-modal-body"
                        style={{
                            borderRadius: 12,
                            maxWidth: "80%",
                            margin: "5% auto",
                            background: "#fff",
                            padding: 16,
                        }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <button className="uk-modal-close-default" type="button" onClick={() => setShowModal(false)} style={{ position: "absolute", top: 10, right: 10 }} uk-close="true" />
                        <img src={zoomedImage} alt="Zoomed Result" style={{ width: "100%", borderRadius: 8 }} />
                    </div>
                </div>
            )}
        </div>
    );
};