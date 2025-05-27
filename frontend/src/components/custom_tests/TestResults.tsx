import { TestResultsModel } from '../../models/TestResultsModel';

export const TestResults = (data: TestResultsModel) => {
    return (
        <div className="uk-card uk-card-default uk-card-body uk-margin-top">
            <h3 className="uk-card-title">Test Results</h3>
            <>
                <p><strong>Input Text:</strong> {data.text}</p>
                <p><strong>Predicted Intent:</strong> {data.intent}</p>
                <p><strong>Confidence:</strong> {data.confidence}</p>

                {data.entities && data.entities.length > 0 && (
                    <>
                        <h4>Extracted Entities:</h4>
                        <ul className="uk-list uk-list-bullet">
                            {data.entities.map((entity, index) => (
                                <li key={index}>
                                    <strong>{entity.entity}</strong>: "{entity.value}"
                                    (start: {entity.start}, end: {entity.end})
                                </li>
                            ))}
                        </ul>
                    </>
                )}
            </>
        </div>
    );
}