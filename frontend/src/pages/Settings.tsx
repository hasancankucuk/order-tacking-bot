import { useState } from "react";
import { updateUser, dropDatabase, seedDb } from "../services";

export const Settings = () => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [role, setRole] = useState("");
    const [success, setSuccess] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [showModal, setShowModal] = useState(false);

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        const userStr = localStorage.getItem("user");
        if (!userStr) {
            setError("User not found in localStorage");
            return;
        }
        const id = JSON.parse(userStr).user.id;
        const result = await updateUser({id, username, password, email, role}, '/auth/update');
        if(result.code === 200) {
            setSuccess("Settings saved");
            setError(null);
        }
    };
    
    const seedDatabase = async () => {
        setSuccess(null);
        setError(null);
        const role = localStorage.getItem("user_role")!;
        const result = await seedDb(role, 'database/seed');
        if (result.code === 200) {
            setSuccess("Database seeded successfully");
        }
    };

    const handleResetDatabase = async () => {
        setShowModal(false);
        setSuccess(null);
        setError(null);
        const result = await dropDatabase('database/delete');
        if (result.code === 200) {
            setSuccess("Database formatted");
            localStorage.removeItem("user");
            localStorage.removeItem("user_role");
            window.location.reload();
        }
    };

    return (
        <div className="uk-container uk-margin-top ">
            <h1>Settings</h1>
            {success && <div className="uk-alert-success" style={{ borderRadius: 8, marginBottom: 12 }}>{success}</div>}
            {error && <div className="uk-alert-danger" style={{ borderRadius: 8, marginBottom: 12 }}>{error}</div>}
            <div className="uk-card uk-card-default uk-card-body uk-box-shadow-large" style={{ borderRadius: 12 }}>
                <form onSubmit={handleSubmit}>
                    <div className="uk-grid-small uk-child-width-1-2@m" uk-grid="true">
                        <div>
                            <input
                                className="uk-input uk-form-large"
                                type="text"
                                placeholder="Username"
                                value={username}
                                onChange={e => setUsername(e.target.value)}
                                style={{ borderRadius: 8 }}
                            />
                        </div>
                        <div>
                            <input
                                className="uk-input uk-form-large"
                                type="email"
                                placeholder="Email"
                                value={email}
                                onChange={e => setEmail(e.target.value)}
                                style={{ borderRadius: 8 }}
                            />
                        </div>
                    </div>
                    <div className="uk-grid-small uk-child-width-1-2@m" uk-grid="true">
                        <div>
                            <input
                                className="uk-input uk-form-large"
                                type="password"
                                placeholder="Password"
                                value={password}
                                onChange={e => setPassword(e.target.value)}
                                style={{ borderRadius: 8 }}
                            />
                        </div>
                        <div>
                            <input
                                className="uk-input uk-form-large"
                                type="text"
                                placeholder="Role"
                                value={role}
                                onChange={e => setRole(e.target.value)}
                                style={{ borderRadius: 8 }}
                            />
                        </div>
                    </div>
                    <div className="uk-grid-large uk-child-width-1-3@m" uk-grid="true">
                        <div>
                            <button className="uk-button uk-button-primary uk-width-1-1 uk-form-medium" type="submit" style={{ borderRadius: 8 }}>
                                Save Changes
                            </button>
                        </div>

                        <div>
                            <button className="uk-button uk-button-secondary uk-width-1-1 uk-form-medium" type="button" style={{ borderRadius: 8 }} onClick={() => seedDatabase()}>
                                Seed Database
                            </button>
                        </div>
                        
                        <div>
                            <button className="uk-button uk-button-danger uk-width-1-1 uk-form-medium" type="button" style={{ borderRadius: 8 }} onClick={() => setShowModal(true)}>
                                Reset Database
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            {showModal && (
                <div className="uk-modal uk-open" style={{ display: 'block', background: 'rgba(0,0,0,0.3)' }}>
                    <div className="uk-modal-dialog uk-modal-body" style={{ borderRadius: 12 }}>
                        <h2 className="uk-modal-title">Confirm Reset</h2>
                        <p>Are you sure you want to reset the database? This action cannot be undone.</p>
                        <button className="uk-button uk-button-danger" onClick={handleResetDatabase}>Yes, Reset</button>
                        <button className="uk-button uk-button-default uk-modal-close" onClick={() => setShowModal(false)} style={{ marginLeft: 8 }}>Cancel</button>
                    </div>
                </div>
            )}
        </div>
    );
};