import { useEffect, useState } from "react";
import { customQuery, updateCustomQuery } from "../../services";
import { Table } from "../table/Table";


export const Playground = () => {
    const [result, setResult] = useState<any>(null);
    const [query, setQuery] = useState("");
    const [mode, setMode] = useState<"select" | "update">("select");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        setResult(null);
        setQuery("");
        setError(null);
        setLoading(false);
    }, [mode]);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setError(null);
        setResult(null);
        if (!query) {
            setError("No SQL query provided.");
            return;
        }
        setLoading(true);
        try {
            let data;
            if (mode === "select") {
                data = await customQuery(query);
            } else {
                data = await updateCustomQuery(query);
            }
            setResult(data.table || data);
        } catch (err: any) {
            setError(err.message || "An error occurred.");
        } finally {
            setLoading(false);
        }
    };

    const onEnterPress = (e: any) => {
        if (e.keyCode === 13 && e.shiftKey === false) {
            e.preventDefault();
            handleSubmit(e);
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div className="uk-margin">
                <label className="uk-form-label" htmlFor="form-horizontal-text">Enter your SQL Query</label>
                <div className="uk-form-controls">
                    <textarea
                        className="uk-input"
                        id="form-horizontal-text"
                        placeholder={mode === 'select' ? "SELECT * FROM users" : "UPDATE users SET username = 'admin1' WHERE id = 1"}
                        value={query}
                        onChange={e => setQuery(e.target.value)}
                        onKeyDown={onEnterPress}
                        rows={4}
                        style={{ fontFamily: 'monospace' }}
                    />
                </div>
            </div>
            <div className="uk-margin">
                <label>
                    <input
                        type="radio"
                        name="mode"
                        value="select"
                        checked={mode === "select"}
                        onChange={() => setMode("select")}
                    /> Select
                </label>
                <label style={{ marginLeft: 16 }}>
                    <input
                        type="radio"
                        name="mode"
                        value="update"
                        checked={mode === "update"}
                        onChange={() => setMode("update")}
                    /> Update/Insert/Delete
                </label>
            </div>
            <button className="uk-button uk-button-primary" type="submit" disabled={loading}>
                {loading ? "Running..." : "Submit"}
            </button>
            {error && <div className="uk-alert-danger" style={{ marginTop: 16 }}>{error}</div>}

            {result && Array.isArray(result) && result.length > 0 && (
                <Table tableData={result} tableName="Custom Query Result" showHeader={true} />
            )}
            {result && Array.isArray(result) && result.length === 0 && (
                <div className="uk-alert-warning" style={{ marginTop: 16 }}>No results found.</div>
            )}
            {result && !Array.isArray(result) && (
                <pre style={{ marginTop: 16 }}>{JSON.stringify(result, null, 2)}</pre>
            )}
        </form>
    );
}