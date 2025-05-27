import { useState } from "react"
import { NLUTestModel } from "../../models/NLUTestModel"
import { fetchResults } from "../../services/metrics"

export const NLUMetrics = (data: NLUTestModel) => {
    const [showModal, setShowModal] = useState(false);
    const [zoomedImage, setZoomedImage] = useState<string>("");
    return (
        <div className="uk-card uk-card-default uk-card-body uk-margin-top">
            <h3 className="uk-card-title">NLU Metrics</h3>
            <table className="uk-table uk-table-small uk-table-divider">
                <tbody>
                    <tr>
                        <td><strong>Accuracy</strong></td>
                        <td>{data.report.accuracy.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Entity F1-Score</strong></td>
                        <td>{data.report.entity["f1-score"].toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Precision</strong></td>
                        <td>{data.report.entity.precision.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Recall</strong></td>
                        <td>{data.report.entity.recall.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td><strong>Confusion Matrix</strong></td>
                        <td>
                            <img
                                onClick={() => {
                                    setZoomedImage(fetchResults(data.results.confusion_matrix_image));
                                    setShowModal(true);
                                }}
                                src={fetchResults(data.results.confusion_matrix_image)}
                                alt="Confusion Matrix"
                            ></img>
                        </td>
                    </tr>
                    <tr>
                        <td><strong>DIET Classifier Histogram </strong></td>
                        <td>
                            <img
                                onClick={() => {
                                    setZoomedImage(fetchResults(data.results.histogram_image));
                                    setShowModal(true);
                                }}
                                src={fetchResults(data.results.histogram_image)}
                                alt="DIET Classifier Histogram"
                            ></img>
                        </td>
                    </tr>
                </tbody>
            </table>
            {showModal && zoomedImage && (
                <div
                    className="uk-modal uk-open" style={{ display: "block", background: "rgba(0,0,0,0.6)", position: "fixed", top: 0, left: 0, right: 0, bottom: 0, zIndex: 1000 }}
                    onClick={() => setShowModal(false)}
                >
                    <div
                        className="uk-modal-dialog uk-modal-body"
                        style={{ borderRadius: 12, maxWidth: "80%", margin: "5% auto", background: "#fff", padding: 16, }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <button className="uk-modal-close-default" type="button" onClick={() => setShowModal(false)} style={{ position: "absolute", top: 10, right: 10 }} uk-close="true" />
                        <img src={zoomedImage} alt="Zoomed Result" style={{ width: "100%", borderRadius: 8 }}
                        />
                    </div>
                </div>
            )}
        </div>
    );
}