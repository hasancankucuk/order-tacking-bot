interface TableProps {
    tableData: any[];
    tableName?: string;
    showHeader?: boolean;
    isLoading?: boolean;
}

export const Table = ({ tableData, tableName, showHeader, isLoading }: TableProps) => {
    if (isLoading) {
        return (
            <div className="uk-text-center uk-padding">
                <div data-uk-spinner="ratio: 2"></div>
                <p className="uk-margin-small-top">Loading table data...</p>
            </div>
        );
    }

    if (!tableData || tableData.length === 0) {
        return (
            <div className="uk-text-center uk-padding uk-text-muted">
                <span data-uk-icon="icon: database; ratio: 2"></span>
                <p className="uk-margin-small-top">No data available</p>
            </div>
        );
    }

    return (
        <div className="uk-width-1-1">
            <div className="uk-overflow-auto">
                <table className="uk-table uk-table-divider uk-table-justify uk-table-small uk-table-responsive">
                    { showHeader && tableName && (
                        <caption className="uk-text-bold uk-text-uppercase uk-margin-small-bottom">
                            {tableName }
                        </caption>
                    )}
                    <thead>
                        <tr>
                            {Object.keys(tableData[0]).map((col, idx) => (
                                <th key={idx} className="uk-text-nowrap">{col}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {tableData.map((row, idx) => (
                            <tr key={idx}>
                                {Object.values(row).map((cell, i) => (
                                    <td key={i} className="uk-text-break">{String(cell)}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};