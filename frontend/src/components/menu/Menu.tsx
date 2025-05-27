import React from 'react';
import { useNavigate } from 'react-router-dom';
import { MenuItems } from '../../models/MenuModel';

export const Menu = () => {
    const navigate = useNavigate();
    const userRole = localStorage.getItem('user_role');
    const [selectedItem, setSelectedItem] = React.useState<MenuItems>(MenuItems.Introduction);
    const menuList = [
        { id: MenuItems.Introduction, label: 'Introduction', href: '/introduction' },
        { id: MenuItems.BotArchitecture, label: 'Bot Architecture', href: '/bot-architecture' },
        // TODO:  It seems like this page is not feasible right now, future work.
        // { id: MenuItems.EvaluationMetrics, label: 'Evaluation Metrics', href: '/evaluation-metrics' },
        ...(userRole === 'admin' ? [
            { id: MenuItems.DatabaseViewer, label: 'Database Viewer', href: '/database-viewer' },
            { id: MenuItems.SQLPlayground, label: 'SQL Playground', href: '/sql-playground' },
            { id: MenuItems.TestCases, label: 'Test Cases', href: '/test-cases' },
            { id: MenuItems.Settings, label: 'Settings', href: '/settings' },
        ] : [])
    ];

    return (
        <div className="uk-flex uk-flex-middle uk-flex-center uk-margin-top uk-margin-bottom">
            <div className="uk-card uk-card-default uk-card-body uk-box-shadow-large" style={{ borderRadius: 12, height: '-webkit-fill-available' }}>
                <h3 className="uk-card-title">Menu</h3>
                <ul className="uk-nav uk-nav-default uk-margin uk-nav-parent-icon" uk-nav="true" style={{ flex: 1 }}>
                    {menuList.map((item) => (
                        <li
                        key={item.id}
                        className={item.id === selectedItem ? 'uk-active' : ''}
                        style={{ marginBottom: 12 }}
                        >
                            <a
                                href={item.href}
                                className="uk-link-reset uk-padding-small uk-display-block"
                                onClick={e => {
                                    e.preventDefault();
                                    setSelectedItem(item.id);
                                    navigate(item.href);
                                }}
                            >
                                {item.label}
                            </a>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    )
}