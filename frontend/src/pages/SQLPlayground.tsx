import { Playground } from "../components/playground/Playground";

export const SQLPlayground = () => {
    return (
        <div className="uk-container uk-margin-top">
            <h1>SQL Playground</h1>

            <div className="uk-flex uk-flex-middle uk-flex-center uk-margin-top uk-margin-bottom">
                <div className="uk-card uk-card-default uk-card-body uk-box-shadow-large" style={{ borderRadius: 12 }}>
                    <p>This page will allow you to write and test SQL queries.</p>
                    <Playground />
                </div>
            </div>
        </div>
    );
}