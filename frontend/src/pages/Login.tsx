import { useState } from "react";
import { login, register } from "../services";

export const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [role, setRole] = useState("");
    const [isRegister, setIsRegister] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setError(null);
        setLoading(true);
        try {
            let result;
            if (isRegister) {
                result = await register(username, password, email, role, 'auth/register');
                if (result && result.message) {
                    setIsRegister(false);
                    setError("Registration successful! Please log in.");
                } else {
                    setError(result?.error || "Registration failed.");
                }
            } else {
                result = await login(username, password, 'auth/login');
                if (result) {
                    localStorage.setItem("user", JSON.stringify(result));
                    localStorage.setItem("user_role", result.user.role || "user");
                    window.location.href = "/";
                } else {
                    setError("Invalid username or password.");
                }
            }
        } catch (e: any) {
            setError(e.message || (isRegister ? "Registration failed." : "Login failed."));
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="uk-flex uk-flex-middle uk-flex-center" style={{ minHeight: '100vh', background: '#f7f7f7' }}>
            <div className="uk-card uk-card-default uk-card-body uk-width-medium uk-box-shadow-large" style={{ borderRadius: 12 }}>
                <h2 className="uk-text-center uk-margin">{isRegister ? "Register" : "Login"}</h2>
                <form onSubmit={handleSubmit} autoComplete="off">
                    <div className="uk-margin">
                        <input
                            className="uk-input uk-form-large"
                            type="text"
                            value={username}
                            onChange={e => setUsername(e.target.value)}
                            placeholder="Username"
                            autoFocus
                            style={{ borderRadius: 8 }}
                        />
                    </div>
                    {isRegister && (
                        <>
                            <div className="uk-margin">
                                <input
                                    className="uk-input uk-form-large"
                                    type="email"
                                    value={email}
                                    onChange={e => setEmail(e.target.value)}
                                    placeholder="Email"
                                    style={{ borderRadius: 8 }}
                                />
                            </div>

                            <div className="uk-margin">
                                <select
                                    className="uk-select uk-form-large uk-border-rounded"
                                    aria-label="Select"
                                    value={role ?? ""}
                                    onChange={(e) => setRole(e.target.value)}
                                >
                                    <option value="" disabled>Select role</option>
                                    <option value="admin">Admin</option>
                                    <option value="user">User</option>
                                </select>
                            </div>
                        </>
                    )}
                    <div className="uk-margin">
                        <input
                            className="uk-input uk-form-large"
                            type="password"
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                            placeholder="Password"
                            style={{ borderRadius: 8 }}
                        />
                    </div>
                    {error && <div className="uk-alert-danger uk-text-center" style={{ borderRadius: 8, marginBottom: 12 }}>{error}</div>}
                    <button className="uk-button uk-button-primary uk-width-1-1 uk-form-large" type="submit" style={{ borderRadius: 8 }} disabled={loading}>
                        {loading ? (isRegister ? "Registering..." : "Logging in...") : (isRegister ? "Register" : "Login")}
                    </button>
                    <div className="uk-text-center uk-margin-small-top">
                        <button
                            type="button"
                            className="uk-button uk-button-link"
                            style={{ padding: 0, border: 'none', background: 'none', color: '#1e87f0', textDecoration: 'underline', cursor: 'pointer' }}
                            onClick={e => {
                                setIsRegister(!isRegister);
                                setError(null);
                            }}
                        >
                            {isRegister ? "Already have an account? Login" : "Don't have an account? Register"}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}