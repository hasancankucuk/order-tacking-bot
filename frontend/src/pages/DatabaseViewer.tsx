import { useEffect, useState } from "react";
import { Table } from "../components/table/Table";
import { getTables, getTableData } from "../services";
import { TableModel } from "../models/TableModel";
import UIkit from "uikit/dist/js/uikit";


export const DatabaseViewer = () => {

    const [tableNames, setTableNames] = useState<string[]>([]);
    const [selectedTable, setSelectedTable] = useState<string | null>(null);
    const [tableData, setTableData] = useState<any[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    useEffect(() => {
        const fetchTables = async () => {
            const tables = await getTables();
            setTableNames(tables);
        };
        fetchTables();

    }, []);

    useEffect(() => {
        if (typeof UIkit.update === "function") {
            UIkit.update();
        }
    }, []);


    useEffect(() => {
        const fetchData = async () => {
            if (selectedTable) {
                setIsLoading(true);
                try {
                    const data = await getTableData(selectedTable);
                    setTableData(data);
                } catch (error) {
                    console.error('Error fetching table data:', error);
                    setTableData([]);
                } finally {
                    setIsLoading(false);
                }
            }
        };
        fetchData();
    }, [selectedTable]);

    const handleRefresh = async () => {
        if (selectedTable) {
            setIsLoading(true);
            try {
                const data = await getTableData(selectedTable);
                setTableData(data);
            } catch (error) {
                console.error('Error refreshing table data:', error);
            } finally {
                setIsLoading(false);
            }
        }
    }

    return (
        <div className="uk-container uk-margin-top">
            <h1>Database Viewer</h1>
            <div className="uk-card uk-card-default uk-card-body uk-box-shadow-large" style={{ borderRadius: 12 }}>

                <div className="uk-margin uk-flex uk-flex-middle uk-flex-between">
                    <select
                        className="uk-select uk-border-rounded"
                        aria-label="Select"
                        value={selectedTable ?? ""}
                        onChange={(e) => setSelectedTable(e.target.value)}
                    >
                        <option value="" disabled>Select a table</option>
                        {tableNames && tableNames.map((name, index) => (
                            <option key={index} value={name}>
                                {Object.entries(TableModel).find(([k, v]) => v === name)?.[0] || name}
                            </option>
                        ))}
                    </select>

                    <span
                        data-uk-icon="icon: refresh"
                        style={{ cursor: "pointer" }}
                        onClick={handleRefresh}
                        aria-label="Refresh"
                        role="button"
                    ></span>
                </div>
                
                {/* Table container with responsive wrapper */}
                <div className="uk-overflow-auto" style={{ maxHeight: '600px' }}>
                    <Table tableData={tableData} isLoading={isLoading} />
                </div>
            </div>
        </div>
    )
}