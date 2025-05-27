import { useState } from "react";
import { runCustomNLUTest } from "../services/customTests";
import { TestResults } from "../components/custom_tests/TestResults";

export const TestCases = () => {
    const [text, setText] = useState("");
    const [expectedIntent, setExpectedIntent] = useState("");

    const [success, setSuccess] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [data, setData] = useState<any>(null);

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setSuccess(null);
        setError(null);
        if (!text || !expectedIntent) {
            setError("Please fill in both fields.");
            return;
        }

        try {
            const response = await runCustomNLUTest(text, expectedIntent);
            setData(response);
            setSuccess("Test case executed successfully!");
        }
        catch (err: any) {
            setError(err.message || "An unexpected error occurred.");
        }
    };

    return (
        <div className="uk-container uk-margin-top">
            <h1>Test Cases</h1>
            <div className="uk-card uk-card-default uk-card-body uk-box-shadow-large" style={{ borderRadius: 12 }}>
                <form onSubmit={handleSubmit}>
                    <div className="uk-grid-small uk-child-width-1-2@m" uk-grid="true">
                        <div>
                            <input
                                className="uk-input uk-form-large"
                                type="text"
                                placeholder="Test Text"
                                value={text}
                                onChange={e => setText(e.target.value)}
                                style={{ borderRadius: 8 }}
                            />
                        </div>
                        <div>
                            <input
                                className="uk-input uk-form-large"
                                type="text"
                                placeholder="Expected Intent"
                                value={expectedIntent}
                                onChange={e => setExpectedIntent(e.target.value)}
                                style={{ borderRadius: 8 }}
                            />
                        </div>
                    </div>
                    <div className="uk-grid-large uk-child-width-1-3@m" uk-grid="true">
                        <div>
                            <button className="uk-button uk-button-primary uk-width-1-1 uk-form-medium" type="submit" style={{ borderRadius: 8 }}>
                                Run Test
                            </button>
                        </div>
                    </div>
                </form>
            </div>

            {error && <div className="uk-alert-danger uk-text-center uk-margin-top" style={{ borderRadius: 8, marginBottom: 12 }}>{error}</div>}
            {success && (
                <>
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
                        <TestResults {...data} />
                    </pre>
                </>
            )}
        </div>
    );
}