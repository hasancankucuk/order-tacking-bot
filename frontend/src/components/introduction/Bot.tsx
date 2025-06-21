export const Bot = () => {
    return (
        <div className="uk-card uk-card-default uk-card-body uk-margin-top">
            <h3 className="uk-card-title">Bot Architecture</h3>
            <div className="uk-text-justify">
                <p>This bot developed with <a href="https://rasa.com/">Rasa</a>. On the backend, <a href="https://www.python.org/">Python</a>  and <a href="https://flask.palletsprojects.com/en/stable/">Flask API </a>used and <a href="https://sqlite.org/">SQLite</a> for the database.</p>
                <p>For the frontend side, <a href="https://react.dev/">React</a> and <a href="https://getuikit.com/">UIKit CSS Framework</a> are used.</p>
                <p>The deployment process leverages <a href="https://www.docker.com/">Docker</a> container technology and is hosted on the <a href="https://www.digitalocean.com/">DigitalOcean</a> platform. 
                    This approach ensures portability, scalability, and ease of management for the application.</p>
            </div>
        </div>
    )
}
