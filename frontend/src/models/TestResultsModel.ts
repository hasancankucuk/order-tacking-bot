export interface Entity {
    entity: string;
    value: string;
    start: number;
    end: number;
    confidence_entity?: number;
}

export interface TestResultsModel {
    text: string;
    intent: string;
    confidence: number;
    entities: Entity[];
    error?: string;
}