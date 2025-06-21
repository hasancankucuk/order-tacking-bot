export const BotArchitecture = () => {
    return (
        <div className="uk-container uk-margin-top">
            <h1 className="uk-heading-primary">Bot Architecture</h1>


            <div className="uk-card uk-card-default uk-card-body uk-margin-large">
                <h2 className="uk-card-title">System Architecture</h2>
                <div className="uk-child-width-1-3@m uk-grid-match" uk-grid="true">
                    <div>
                        <div className="uk-card uk-card-default uk-card-body">
                            <h3 className="uk-card-title">Frontend</h3>
                            <ul className="uk-list uk-list-bullet">
                                <li>React + TypeScript</li>
                                <li>UIKit CSS Framework</li>
                                <li>Real-time Chat Interface</li>
                                <li>Database Viewer</li>
                                <li>Order Management</li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div className="uk-card uk-card-default uk-card-body">
                            <h3 className="uk-card-title">Chatbot</h3>
                            <ul className="uk-list uk-list-bullet">
                                <li>Rasa Framework</li>
                                <li>Natural Language Understanding</li>
                                <li>Intent Classification</li>
                                <li>Entity Extraction</li>
                                <li>Dialogue Management</li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div className="uk-card uk-card-default uk-card-body">
                            <h3 className="uk-card-title">Backend</h3>
                            <ul className="uk-list uk-list-bullet">
                                <li>Flask API</li>
                                <li>SQLite Database</li>
                                <li>Custom Actions</li>
                                <li>Invoice Generator</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div className="uk-card uk-card-default uk-card-body uk-margin-large">
                <h2 className="uk-card-title">Deployment & Services</h2>
                <div className="uk-child-width-1-3@m" uk-grid="true">
                    <div>
                        <div className="uk-card uk-card-default uk-card-body">
                            <h4>Frontend (React)</h4>
                            <p><strong>Port:</strong> 3000</p>
                            <p><strong>Build:</strong> npm run build</p>
                        </div>
                    </div>
                    <div>
                        <div className="uk-card uk-card-default uk-card-body">
                            <h4>Rasa Server</h4>
                            <p><strong>Port:</strong> 5005</p>
                            <p><strong>Command:</strong> rasa run</p>
                        </div>
                    </div>
                    <div>
                        <div className="uk-card uk-card-default uk-card-body">
                            <h4>Action Server</h4>
                            <p><strong>Port:</strong> 5055</p>
                            <p><strong>Command:</strong> rasa run actions</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}